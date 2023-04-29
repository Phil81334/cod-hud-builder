from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QBrush, QColor, QFont, QPixmap, QPen, QMouseEvent
from PySide6.QtWidgets import QMainWindow, QGraphicsItem, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem

from manipulatorHandle import ManipulatorHandle

import os
import sys
from pathlib import Path

class Elem(QGraphicsRectItem):
    def __init__(self, main_window: QMainWindow, scene: QGraphicsScene, rect: QRectF, elemType: str) -> None:
        super().__init__()

        self.main_window = main_window
        self.scene = scene

        self.setRect(rect)

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        self.elemType = elemType

        match self.elemType:
            case "Text":
                self.id = self.scene.textElemID
                self.scene.textElemID += 1                
            case "Material":
                self.id = self.scene.materialElemID
                self.scene.materialElemID += 1
            case "Button":
                self.id = self.scene.buttonElemID
                self.scene.buttonElemID += 1  

        self.name = f"{self.elemType} {self.id}"

        self.selected_edge = self.click_pos = self.click_rect = None

        self.backgroundFilled = False

        self.xPosIndicatorSize = 20.0
        self.xPosIndicatorOffset = self.xPosIndicatorSize / 2

        self.quadrandIndicatorSize = 10.0
        self.quadrandIndicatorOffset = self.quadrandIndicatorSize / 2

        self.assignOutline()
        
        if self.elemType == 'Text':
            self.textItemFontSize = 10
            self.textItemOffset = 5.0
            self.addTextItem()

        self.addXPosIndicator()
        self.addQuadrantIndicator()
        self.addManipulatorHandle()

        self.setSelected(True)

        self.movingElemViaMouse = False

        # these are what get outputted to file
        self.assignMenuAttributes()

    def assignOutline(self):
        match self.elemType:
            case "Text":
                self.col = "red"
            case "Material":
                self.col = "green"
            case "Button":
                self.col = "blue"
        self.setPen(QPen(QBrush(QColor(self.col)), 1.5))

    def addTextItem(self):
        self.textItem = QGraphicsTextItem(self)
        self.textItem.setDefaultTextColor(Qt.white)
        self.textItem.setVisible(self.main_window.ui.elem_label.isChecked())

        self.textItem.setPos(QPointF(self.rect().x() + self.textItemOffset, self.rect().y() + self.textItemOffset))

        font = QFont("Cascade Mono", self.textItemFontSize)

        self.textItem.setFont(font)

        # Set the thickness of the text item
        # self.textItem_pen = QPen(QColor(Qt.cyan))
        # self.textItem_pen.setWidth(2)
        # self.textItem.setPen(self.textItem_pen)

        self.textItem.setPlainText(f"{self.elemType} {self.id}")
    
    def addXPosIndicator(self):
        self.xPosIndicator = QGraphicsEllipseItem(QRectF(self.rect().x()-self.xPosIndicatorOffset, self.rect().y()-self.xPosIndicatorOffset, self.xPosIndicatorSize, self.xPosIndicatorSize), self)
        penRed = QPen(QColor(Qt.red))
        penRed.setWidth(1.5)
        self.xPosIndicator.setPen(penRed)
        self.xPosIndicator.setVisible(self.main_window.ui.x_pos_indicator.isChecked())

    def addQuadrantIndicator(self):
        self.quadrantIndicator = QGraphicsEllipseItem(QRectF(self.rect().x()-self.quadrandIndicatorOffset, self.rect().y()-self.quadrandIndicatorOffset, self.quadrandIndicatorSize, self.quadrandIndicatorSize), self)
        penCyan = QPen(QColor(Qt.cyan))
        penCyan.setWidth(1.5)
        self.quadrantIndicator.setPen(penCyan)
        self.quadrantIndicator.setVisible(self.main_window.ui.quadrant_indicator.isChecked())

    def addManipulatorHandle(self):
        curr_dir = Path(f"{os.getcwd()}/icons/others/")
        pixmap_path = curr_dir / "manipulator_handle.png"
        print(f"pixmap path: {pixmap_path}")

        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # pixmap_path = os.path.join(script_dir, "icons\others\manipulator_handle.png")

        # pixmap_path = self.get_resource_path("icons\others\manipulator_handle.png")

        pixmap = QPixmap(pixmap_path)
        self.manipulatorHandle = ManipulatorHandle(self.main_window, self.scene, pixmap, parent=self)
        self.manipulatorHandle.setVisible(False)

    # cause .exe is being a slag and causing directory issues
    def get_resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def assignMenuAttributes(self):
        self.rect_x = str(self.rect().x())
        self.rect_y = str(self.rect().y())
        self.rect_w = str(self.rect().width())
        self.rect_h = str(self.rect().height())

        quadrant = self.scene.getQuadrant(self)
        match quadrant:
            case 1:
                self.menu_rect_x = str(self.rect().x())
                self.menu_rect_y = str(self.rect().y())
            case 2:
                self.menu_rect_x = str(self.rect().x() - self.scene.width)
                self.menu_rect_y = str(self.rect().y())
            case 3:
                self.menu_rect_x = str(self.rect().x())
                self.menu_rect_y = str(self.rect().y() - self.scene.height)
            case 4:
                self.menu_rect_x = str(self.rect().x() - self.scene.width)
                self.menu_rect_y = str(self.rect().y() - self.scene.height)

        self.menu_rect_w = str(self.rect().width())
        self.menu_rect_h = str(self.rect().height())

        match quadrant:
            case 1:
                self.rect_h_align    = "HORIZONTAL_ALIGN_LEFT"
                self.rect_v_align    = "VERTICAL_ALIGN_TOP"
            case 2:
                self.rect_h_align    = "HORIZONTAL_ALIGN_RIGHT"
                self.rect_v_align    = "VERTICAL_ALIGN_TOP"
            case 3:
                self.rect_h_align    = "HORIZONTAL_ALIGN_LEFT"
                self.rect_v_align    = "VERTICAL_ALIGN_BOTTOM"
            case 4:
                self.rect_h_align    = "HORIZONTAL_ALIGN_RIGHT"
                self.rect_v_align    = "VERTICAL_ALIGN_BOTTOM"

        match self.elemType:
            case "Text":
                self._type_          = "ITEM_TYPE_TEXT"
                self.forecolor       = "1 1 1 1"
                self.text            = self.name
                self.text_type       = "text"
                self.textfont        = "UI_FONT_OBJECTIVE"
                self.textscale       = "0.2"
                self.textstyle       = "ITEM_TEXTSTYLE_NORMAL"

                if quadrant in (1, 3):
                    self.textalign = "ITEM_ALIGN_MIDDLE_LEFT"
                elif quadrant in (2, 4):
                    self.textalign = "ITEM_ALIGN_MIDDLE_RIGHT"
                
                self.visible         = "1"
                self.decoration      = True
            case "Material":
                self.style           = "WINDOW_STYLE_SHADER"
                self.forecolor       = "1 1 1 1"
                self.background_material_text = self.name
                self.background_material_text_type = "background"
                self.visible         = "1"
            case "Button":
                self._type_          = "ITEM_TYPE_BUTTON"
                self.visible         = "1"
                self.action          = 'play "mouse_click";'
                self.mouseEnter      = 'play "mouse_over";'
                self.mouseExit       = ""

    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            self.movingElemViaMouse = False

    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.movingElemViaMouse = True

            self.click_pos = event.pos()
            rect = self.rect()
            
            # disable inside resizing if outside resizing option is True
            if self.scene.is_resizing_inside():
                threshold = self.scene.resize_threshold
                if abs(rect.left() - self.click_pos.x()) < threshold:
                    self.selected_edge = 'left'
                elif abs(rect.right() - self.click_pos.x()) < threshold:
                    self.selected_edge = 'right'
                elif abs(rect.top() - self.click_pos.y()) < threshold:
                    self.selected_edge = 'top'
                elif abs(rect.bottom() - self.click_pos.y()) < threshold:
                    self.selected_edge = 'bottom'
                else:
                    self.selected_edge = None
            else:
                self.selected_edge = None

            self.click_pos = event.pos()
            self.click_rect = rect

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = event.pos()

        snap_to_grid = self.scene.is_snap_to_grid_enabled()
        if snap_to_grid:
            blockSize = self.scene.getBlockSize()

            # Calculate the position on the grid that the mouse is closest to.
            x = round(pos.x() / blockSize) * blockSize
            y = round(pos.y() / blockSize) * blockSize
            dx = x - pos.x()
            dy = y - pos.y()

            # If the mouse is not exactly on a grid line, adjust the position to snap to the grid.
            if abs(dx) <= blockSize / 2:
                pos.setX(x)
            if abs(dy) <= blockSize / 2:
                pos.setY(y)

        # Calculate how much the mouse has moved since the click.
        x_diff = pos.x() - self.click_pos.x()
        y_diff = pos.y() - self.click_pos.y()

        # Start with the rectangle as it was when clicked.
        rect = QRectF(self.click_rect)

        if self.selected_edge is None:
            if snap_to_grid:
                # Move the rectangle by a fixed increment of 10 pixels
                x_diff = x_diff // blockSize * blockSize or blockSize
                y_diff = y_diff // blockSize * blockSize or blockSize
            rect.translate(x_diff, y_diff)
        elif self.selected_edge == 'top':
            rect.adjust(0, y_diff, 0, 0)
        elif self.selected_edge == 'left':
            rect.adjust(x_diff, 0, 0, 0)
        elif self.selected_edge == 'bottom':
            rect.adjust(0, 0, 0, y_diff)
        elif self.selected_edge == 'right':
            rect.adjust(0, 0, x_diff, 0)

        # Figure out the limits of movement. I did it by updating the scene's rect after the window resizes.
        scene_rect = self.scene.sceneRect()
        view_left = scene_rect.left()
        view_top = scene_rect.top()
        view_right = scene_rect.right()
        view_bottom = scene_rect.bottom()

        # Next, check if the rectangle has been dragged out of bounds
        if rect.top() < view_top:
            if self.selected_edge is None:
                rect.translate(0, view_top-rect.top())
            else:
                rect.setTop(view_top)
        if rect.left() < view_left:
            if self.selected_edge is None:
                rect.translate(view_left-rect.left(), 0)
            else:
                rect.setLeft(view_left)
        if view_bottom < rect.bottom():
            if self.selected_edge is None:
                rect.translate(0, view_bottom - rect.bottom())
            else:
                rect.setBottom(view_bottom)
        if view_right < rect.right():
            if self.selected_edge is None:
                rect.translate(view_right - rect.right(), 0)
            else:
                rect.setRight(view_right)

        # Also check if the rectangle has been dragged inside out.
        if rect.width() < 5:
            if self.selected_edge == 'left':
                rect.setLeft(rect.right() - 5)
            else:
                rect.setRight(rect.left() + 5)
        if rect.height() < 5:
            if self.selected_edge == 'top':
                rect.setTop(rect.bottom() - 5)
            else:
                rect.setBottom(rect.top() + 5)

        self.setRect(rect)
        self.scene.updateMenuAttributesAndElem_partsPos(self)