from PySide6.QtCore import QRect, Qt, QRectF, QLine, QPointF
from PySide6.QtGui import QBrush, QColor, QCursor, QImage, QPainter, QPen, QKeyEvent
from PySide6.QtWidgets import QGraphicsScene, QFileDialog, QGraphicsSceneMouseEvent

from elem import Elem

import os
import math
import json
import re

class Scene(QGraphicsScene):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.width, self.height = 1340.0, 740.0
        self.setSceneRect(0.0, 0.0, self.width, self.height)

        # stores elems (elem == rect, text, x2 ellipses)
        self.elems = []

        # these are used to assign a unique id to each elem
        self.textElemID = 0
        self.materialElemID = 0
        self.buttonElemID = 0

        # active = currently selected
        self.activeElem = None

        self.background_color = QColor('#404148')
        self.background_image = None

        self.drawGrid = True
        self.drawQuadrantGrid = True
        self.drawQuadrantLabel = False

        self.gridSize = 10
        self.gridSquares = 5

        self.grid_pen = QPen(QColor("#000040"))
        self.grid_pen.setWidth(1)

        self.quadrant_pen = QPen(QColor(Qt.cyan))
        self.quadrant_pen.setWidth(1)

        self.main_window.ui.background.stateChanged.connect(self.toggleBackground)
        self.main_window.ui.background_image_btn.clicked.connect(self.selectBackgroundImage)

        self.main_window.ui.grid.stateChanged.connect(self.toggleGrid)
        self.main_window.ui.quadrant_grid.stateChanged.connect(self.toggleQuadrantGrid)
        self.main_window.ui.quadrant_label.stateChanged.connect(self.toggleQuadrantLabel)

        self.main_window.ui.clear_scene.clicked.connect(self.clearScene)

        self.main_window.ui.open_file.clicked.connect(self.openScene)
        self.main_window.ui.save_file.clicked.connect(self.saveScene)

        self.main_window.ui.elem_label.stateChanged.connect(self.toggleElemLabel)
        self.main_window.ui.x_pos_indicator.stateChanged.connect(self.toggleXPosIndicator)
        self.main_window.ui.quadrant_indicator.stateChanged.connect(self.toggleQuadrantIndicator)
    
        self.main_window.ui.fill_background.clicked.connect(self.fillBackground)
        
        self.manipulatorHandle = False
        self.main_window.ui.manipulator_handle.stateChanged.connect(self.toggleManipulatorHandle)

        self.selectionChanged.connect(self.sceneWatcher)

        self.selected_edge = self.click_pos = self.click_rect = None
        self.resize_threshold = 5
        self.cursor_within_dist = False

    def setBackgroundColor(self):
        self.setBackgroundBrush(self.background_color)

    def toggleBackground(self):
        if self.main_window.ui.background.isChecked():
            if self.background_image != None:
                img_path = self.background_image
            else:
                img_path = rf"{os.getcwd()}\img\bg_img_template.png"
            image = QImage(img_path)
            image = image.scaled(self.sceneRect().size().toSize())
            self.setBackgroundBrush(QBrush(image))
        else:
            self.setBackgroundColor()
    
    def selectBackgroundImage(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Select Background Image", "", "Image Files (*.png *.jpg)")
        if filename:
            self.background_image = filename
            self.toggleBackground()

    def addElem(self, rect: QRectF, elemType, qbool: bool=False) -> bool:
        self.clearSelection()
        elem = Elem(self.main_window, self, rect, elemType)
        self.elems.append(elem)

        if self.main_window.ui.fill_background.isChecked():
            self.fillBackground()

        self.addItem(elem)
        self.main_window.objectInspector.addItem(elem.name)

        if qbool:
            return elem

    def deleteElem(self):
        self.main_window.objectInspector.removeItem(self.activeElem.name)
        self.elems.pop(self.elems.index(self.activeElem, 0, len(self.elems)))
        self.removeItem(self.activeElem)

    def copyElem(self):
        elem = self.activeElem
        if self.main_window.ui.copy_elem_current_pos.isChecked():
            x, y = elem.rect().x(), elem.rect().y()
            
        else:
            x, y = 10.0, 10.0
        
        self.addElem(QRectF(x, y, elem.rect().width(), elem.rect().height()), elem.elemType, False)

    def splitElem(self, elem, which):
        original_rect = elem.rect()
        elemType = elem.elemType

        match which:
            case "horizontal":
                half_height = original_rect.height() / 2
                halfway_point = original_rect.y() + half_height
                first_half_rect = QRectF(original_rect.x(), original_rect.y(), original_rect.width(), half_height)
                second_half_rect = QRectF(original_rect.x(), halfway_point, original_rect.width(), half_height)
            case "vertical":
                half_width = original_rect.width() / 2
                halfway_point = original_rect.x() + half_width
                first_half_rect = QRectF(original_rect.x(), original_rect.y(), half_width, original_rect.height())
                second_half_rect = QRectF(halfway_point, original_rect.y(), half_width, original_rect.height())
                
        self.deleteElem()

        for i in range(2):
            rect = first_half_rect if i == 0 else second_half_rect
            self.addElem(rect, elemType, False)
            # None = match:case:rect
            self.main_window.propertyEditor.manualAttributeOverride(None)

    def mirrorElem(self, elem, direction):
        rect, elemType, quadrant = elem.rect(), elem.elemType, self.getQuadrant(elem)

        right_dir = QRectF(self.width - (rect.x() + rect.width()), rect.y(), rect.width(), rect.height())
        left_dir = QRectF(self.width - rect.x() - rect.width(), rect.y(), rect.width(), rect.height())
        up_dir = QRectF(rect.x(), self.height - rect.y() - rect.height(), rect.width(), rect.height())
        down_dir = QRectF(rect.x(), self.height - (rect.y() + rect.height()), rect.width(), rect.height())

        # calculate rect for mirrored elem, based off quadrant
        match quadrant:
            case 1:
                allowed_directions = ['right', 'down']
                if not direction in allowed_directions:
                    return
                match direction:
                    case "right":
                        mirrored_rect = right_dir
                    case "down":
                        mirrored_rect = down_dir
            case 2:
                allowed_directions = ['left', 'down']
                if not direction in allowed_directions:
                    return
                match direction:
                    case "left":
                        mirrored_rect = left_dir
                    case "down":
                        mirrored_rect = down_dir
            case 3:
                allowed_directions = ['right', 'up']
                if not direction in allowed_directions:
                    return
                match direction:
                    case "right":
                        mirrored_rect = right_dir
                    case "up":
                        mirrored_rect = up_dir
            case 4:
                allowed_directions = ['left', 'up']
                if not direction in allowed_directions:
                    return
                match direction:
                    case "left":
                        mirrored_rect = left_dir
                    case "up":
                        mirrored_rect = up_dir
        
        self.addElem(mirrored_rect, elemType, False)
        self.main_window.propertyEditor.manualAttributeOverride(None)
        self.setFocus()

    def getQuadrant(self, elem):
        if elem.rect().x() <= self.width/2 and elem.rect().y() <= self.height/2:
            return 1
        elif elem.rect().x() >= self.width/2 and elem.rect().y() <= self.height/2:
            return 2
        elif elem.rect().x() <= self.width/2 and elem.rect().y() >= self.height/2:
            return 3
        elif elem.rect().x() >= self.width/2 and elem.rect().y() >= self.height/2:
            return 4

    def openScene(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Open Scene", "", "JSON Files (*.json)")
        if filename:

            if self.elems != None:
                self.elems.clear()

            if self.main_window.ui.console_text_area.toPlainText():
                self.main_window.ui.console_text_area.clear()
            
            self.clear()

            self.main_window.objectInspector.clearList()

            self.main_window.propertyEditor.scrollArea.hide()

            if os.path.getsize(filename) > 0:
                with open(filename, "r") as file:
                    data = json.load(file)
                    for item_id, item_data in data.items():

                        elem = self.addElem(QRectF(item_data["pos"]["x"], item_data["pos"]["y"],
                                            item_data["width"], item_data["height"]),
                                            item_data["elemType"], True)
                        # override text and text_type
                        if elem.elemType == "Text":
                            elem.text = item_data["text"]
                            elem.text_type = item_data["text_type"]
                            elem.textItem.setPlainText(elem.text)

                            elem.textfont = item_data["textfont"]
                            elem.textscale = item_data["textscale"]
                            elem.textstyle = item_data["textstyle"]

                            elem.textalign = item_data["textalign"]
                            if elem.textalign not in self.main_window.propertyEditor.text_align_default_values and not elem.text_align_overridden:
                                elem.text_align_overridden = True
                            
                            elem.decoration = item_data["decoration"]
                            elem.forecolor = item_data["forecolor"]

                        elif elem.elemType == "Material":
                            elem.background_material_text = item_data["background_material_text"]
                            elem.background_material_text_type = item_data["background_material_text_type"]
                        
                        elem.visible = item_data["visible"]
                        elem.forecolor = item_data["forecolor"]
                        
                        self.main_window.propertyEditor.update(elem)
                print(f"successfully opened file '{filename}")
            else:
                print(f"The file '{filename}' is empty.")

    def saveScene(self):
        sceneCount = len(self.elems)
        if not sceneCount > 0:
            print("no items in scene")
            return

        print("saving scene")

        # Create a dictionary to store the data for each item
        item_data = {}
        for elem in self.elems:
            # Get the position of the object in the scene
            pos = QPointF(elem.rect().x(), elem.rect().y())
            # Convert the position to a dictionary with x and y keys
            pos = {"x": pos.x(), "y": pos.y()}

            # Get elem attr
            width = elem.rect().width()
            height = elem.rect().height()
            elemType = elem.elemType

            # Add the ResizableRect attributes to the item_data dictionary
            if elemType == 'Text':
                item_data[str(elem.name)] = {
                    "pos": pos,
                    "width": width,
                    "height": height,
                    "elemType": elemType,
                    "text": elem.text,
                    "text_type": elem.text_type,
                    "visible": elem.visible,
                    "textfont": elem.textfont,
                    "textscale": elem.textscale,
                    "textstyle": elem.textstyle,
                    "textalign": elem.textalign,
                    "decoration": elem.decoration,
                    "forecolor": elem.forecolor
                }
            elif elemType == "Material":
                item_data[str(elem.name)] = {
                    "pos": pos,
                    "width": width,
                    "height": height,
                    "elemType": elemType,
                    "background_material_text": elem.background_material_text,
                    "background_material_text_type": elem.background_material_text_type,
                    "visible": elem.visible,
                    "forecolor": elem.forecolor
                }
            else:
                item_data[str(elem.name)] = {
                    "pos": pos,
                    "width": width,
                    "height": height,
                    "elemType": elemType,
                    "visible": elem.visible
                }

        json_path = os.path.join(os.getcwd(), "scene.json")

        # Write the item data to a JSON file
        with open(json_path, 'w') as json_file:
            json.dump(item_data, json_file, indent=4)

        print("scene successfully saved")

    def clearScene(self):
        if not len(self.elems) > 0:
            print("nothing in scene to clear")
            return

        # clear console
        if self.main_window.ui.console_text_area.toPlainText():
            self.main_window.ui.console_text_area.clear()

        self.clear()

        self.elems.clear()

        self.main_window.objectInspector.clearList()

        self.main_window.propertyEditor.scrollArea.hide()
        
        self.textElemID = 0
        self.materialElemID = 0
        self.buttonElemID = 0

        print("scene cleared")

    def toggleGrid(self):
        self.drawGrid = not self.drawGrid
        self.update()

    def toggleQuadrantGrid(self):
        self.drawQuadrantGrid = not self.drawQuadrantGrid
        self.update()

    def toggleQuadrantLabel(self):
        self.drawQuadrantLabel = not self.drawQuadrantLabel
        self.update()

    def toggleElemLabel(self):
        sceneObjects = self.elems
        for elem in sceneObjects:
            if elem.elemType == 'Text':
                elem.textItem.setVisible(self.main_window.ui.elem_label.isChecked())
                    
    def toggleXPosIndicator(self):
        sceneObjects = self.elems
        for elem in sceneObjects:
            elem.xPosIndicator.setVisible(self.main_window.ui.x_pos_indicator.isChecked())
    
    def toggleQuadrantIndicator(self):
        sceneObjects = self.elems
        for elem in sceneObjects:
            elem.quadrantIndicator.setVisible(self.main_window.ui.quadrant_indicator.isChecked())

    def fillBackground(self):
        if self.activeElem is None:
            return
        elem = self.activeElem
        if self.main_window.ui.fill_background.isChecked():
            brush = elem.brush()
            brush.setColor(QColor(elem.col))
            brush.setStyle(Qt.SolidPattern)
            elem.setBrush(brush)
            elem.backgroundFilled = True
            return
        self.removeFillFromBackground(elem)
    
    def removeFillFromBackground(self, elem):
        elem.setBrush(Qt.NoBrush)
        elem.backgroundFilled = False

    def toggleManipulatorHandle(self):
        if not len(self.elems) > 0:
            return
        
        elems = self.elems
        for elem in elems:
            if elem.isSelected():
                elem.manipulatorHandle.setVisible(self.main_window.ui.manipulator_handle.isChecked())

    def getDistanceFromItemEdge(self, elem):
        """Returns the distance from the edge of the selected item to the mouse cursor position."""
        pos = self.views()[0].mapFromGlobal(QCursor.pos())

        bounds = elem.rect()
        left = bounds.left()
        right = bounds.right()
        top = bounds.top()
        bottom = bounds.bottom()
        x = pos.x()
        y = pos.y()

        # Check if the position is inside the bounding rect
        if left <= x <= right and top <= y <= bottom:
            return 0

        # Otherwise, calculate the distances to the edges of the bounding rect
        distances = [
            abs(x - left),
            abs(x - right),
            abs(y - top),
            abs(y - bottom)
        ]

        return min(distances)

    def sceneWatcher(self):
        """
        Prevent multi-elem selection
        Change self.activeElem to the selected elem, or None
        Hide the property editor if no elem is selected    
        Never assign self.activeElem outside of this method. That is the purpose of this method. Among other things.

        Note: the try/except blocks are to prevent error when elem(more importantly the handle) gets deleted
        """

        # return if user has 2 elem's selected
        selectedElems = self.selectedItems()
        totalSelectedElems = len(selectedElems)

        # Hide property editor widget if nothing is selected
        # User clicked on empty scene space, therefore qt by default deselects any selected items
            # So therefore need to set self.activeElem to None
        if totalSelectedElems < 1:
            if not self.is_resizing_inside():
                try:
                    dist = self.getDistanceFromItemEdge(self.activeElem)
                    if dist < 5:
                        self.selectionChanged.disconnect(self.sceneWatcher)
                        self.cursor_within_dist = True
                        self.activeElem.setSelected(True)
                        return
                except Exception:
                    pass

            # default behaviour
            if self.activeElem != None:
                try:
                    if self.main_window.ui.manipulator_handle.isChecked():
                        self.activeElem.manipulatorHandle.setVisible(False)
                except Exception:
                    pass

                self.activeElem = None

                self.main_window.propertyEditor.scrollArea.hide()

                self.main_window.ui.fill_background.setChecked(False)
            return

        # prevent multi-selection
        if totalSelectedElems > 1:
            for idx, elem in enumerate(selectedElems):
                if self.activeElem != elem:
                    elem.setSelected(False)
                    return
    
        if totalSelectedElems == 1:
            if selectedElems[0] != self.activeElem:
                try:
                    # changing active elem so hide handle for previous elem
                    if self.main_window.ui.manipulator_handle.isChecked():
                        self.activeElem.manipulatorHandle.setVisible(False)
                except Exception:
                    pass

                self.activeElem = selectedElems[0]

            self.main_window.propertyEditor.update(self.activeElem)

            # set the elem background filled checkbox state to match the elem background state
            self.main_window.ui.fill_background.setChecked(self.activeElem.backgroundFilled if self.activeElem.backgroundFilled else False)

            if self.main_window.ui.manipulator_handle.isChecked():
                self.activeElem.manipulatorHandle.setVisible(True)

    def is_snap_to_grid_enabled(self):
        return self.main_window.ui.snap_to_grid_enabled.isChecked()

    def is_resizing_inside(self):
        return self.main_window.ui.inside_padding_area.isChecked()

    def getBlockSize(self):
        try:
            return int(self.main_window.ui.snap_to_grid_size.text())
        except ValueError:
            return 10.0

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        if event.isAutoRepeat():
            return
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_O:
            self.openScene()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_S:
            self.saveScene()
        elif event.key() == Qt.Key_Delete:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.deleteElem()
        elif event.key() == Qt.Key_Space:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.copyElem()

        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_H:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.splitElem(self.activeElem, "horizontal")

        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_V:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.splitElem(self.activeElem, "vertical")

        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Left:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.mirrorElem(self.activeElem, "left")
        
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Right:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.mirrorElem(self.activeElem, "right")
        
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Up:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.mirrorElem(self.activeElem, "up")
        
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Down:
            if self.activeElem is not None and self.getDistanceFromItemEdge(self.activeElem) > 5:
                self.mirrorElem(self.activeElem, "down")
        
        # move elem via arrow keys
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_Left:
            if self.activeElem is not None:
                self.moveElem(self.activeElem, self.activeElem.rect(), self.getQuadrant(self.activeElem), "left")
        
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_Right:
            if self.activeElem is not None:
                self.moveElem(self.activeElem, self.activeElem.rect(), self.getQuadrant(self.activeElem), "right")
        
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_Up:
            if self.activeElem is not None:
                self.moveElem(self.activeElem, self.activeElem.rect(), self.getQuadrant(self.activeElem), "up")
        
        elif event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_Down:
            if self.activeElem is not None:
                self.moveElem(self.activeElem, self.activeElem.rect(), self.getQuadrant(self.activeElem), "down")
        event.accept()
    
    def moveElem(self, *args):
        elem, elem_rect, quadrant, dir = args

        blockSize = self.getBlockSize()
        w = elem_rect.width()
        h = elem_rect.height()

        match dir:
            case "left":
                if elem_rect.x()-blockSize >= 0.0:
                    elem.setRect(QRectF(elem_rect.x()-blockSize, elem_rect.y(), w, h))
            case "right":
                if (elem_rect.x() + w + blockSize) <= self.width:
                    elem.setRect(QRectF(elem.rect().x()+blockSize, elem.rect().y(), w, h))
            case "up":
                if elem_rect.y()-blockSize >= 0.0:
                    elem.setRect(QRectF(elem_rect.x(), elem_rect.y()-blockSize, w, h))
            case "down":
                if (elem_rect.y() + h + blockSize) <= self.height:
                    elem.setRect(QRectF(elem_rect.x(), elem_rect.y()+blockSize, w, h))
            case _:
                print("default")
                pass
    
        self.updateMenuAttributesAndElem_partsPos(elem)

    def updateMenuAttributesAndElem_partsPos(self, elem: Elem) -> None:
        rect = elem.rect()
        elemType = elem.elemType
        if elemType == 'Text':
            elem.textItem.setPos(QPointF(elem.rect().x() + elem.textItemOffset, elem.rect().y() + elem.textItemOffset))

        elem.xPosIndicator.setRect(QRectF(elem.rect().x()-elem.xPosIndicatorOffset, elem.rect().y()-elem.xPosIndicatorOffset, elem.xPosIndicatorSize, elem.xPosIndicatorSize))

        # update attributes based on quadrant
        quadrant = self.getQuadrant(elem)

        match quadrant:
            case 1:
                elem.quadrantIndicator.setRect(QRectF(elem.rect().x()-elem.quadrandIndicatorOffset, elem.rect().y()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                elem.rect_h_align = "HORIZONTAL_ALIGN_LEFT"
                elem.rect_v_align = "VERTICAL_ALIGN_TOP"
                if elemType == "Text":
                    if not elem.text_align_overridden:
                        elem.textalign = "ITEM_ALIGN_MIDDLE_LEFT"
                
                if not elem.manipulatorHandle.movingViaHandle:
                    handle = elem.manipulatorHandle
                    x = elem.rect().x() + elem.rect().width() + handle.Offset
                    y = elem.rect().y() + elem.rect().height() + handle.Offset
                    handle.setPos(QPointF(x, y))
                    
            case 2:
                elem.quadrantIndicator.setRect(QRectF(elem.rect().x() + elem.rect().width()-elem.quadrandIndicatorOffset, elem.rect().y()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                elem.rect_h_align = "HORIZONTAL_ALIGN_RIGHT"
                elem.rect_v_align = "VERTICAL_ALIGN_TOP"
                if elemType == "Text":
                    if not elem.text_align_overridden:
                        elem.textalign = "ITEM_ALIGN_MIDDLE_RIGHT"
        
                if not elem.manipulatorHandle.movingViaHandle:
                    handle = elem.manipulatorHandle
                    x = elem.rect().x() - (handle.Offset *2)
                    y = elem.rect().y() + elem.rect().height() + handle.Offset
                    handle.setPos(QPointF(x, y))
            case 3:
                elem.quadrantIndicator.setRect(QRectF(elem.rect().x()-elem.quadrandIndicatorOffset, elem.rect().y() + elem.rect().height()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                elem.rect_h_align = "HORIZONTAL_ALIGN_LEFT"
                elem.rect_v_align = "VERTICAL_ALIGN_BOTTOM"
                if elemType == "Text":
                    if not elem.text_align_overridden:
                        elem.textalign = "ITEM_ALIGN_MIDDLE_LEFT"

                if not elem.manipulatorHandle.movingViaHandle:
                    handle = elem.manipulatorHandle
                    x = elem.rect().x() + elem.rect().width() + handle.Offset
                    y = elem.rect().y() - (handle.Offset *2)
                    handle.setPos(QPointF(x, y))
            case 4:
                elem.quadrantIndicator.setRect(QRectF(elem.rect().x() + elem.rect().width()-elem.quadrandIndicatorOffset, elem.rect().y() + elem.rect().height()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                elem.rect_h_align = "HORIZONTAL_ALIGN_RIGHT"
                elem.rect_v_align = "VERTICAL_ALIGN_BOTTOM"
                if elemType == "Text":
                    if not elem.text_align_overridden:
                        elem.textalign = "ITEM_ALIGN_MIDDLE_RIGHT"
                
                if not elem.manipulatorHandle.movingViaHandle:
                    handle = elem.manipulatorHandle
                    x = elem.rect().x() - (handle.Offset *2)
                    y = elem.rect().y() - (handle.Offset *2)
                    handle.setPos(QPointF(x, y))

        # update elem (menu) attributes
        x = rect.x()
        y = rect.y()
        w = rect.width()
        h = rect.height()

        elem.rect_x = str(x)
        elem.rect_y = str(y)
        elem.rect_w = str(w)
        elem.rect_h = str(h)

        # menu
        match quadrant:
            case 1:
                elem.menu_rect_x = elem.rect_x
                elem.menu_rect_y = elem.rect_y
            case 2:
                elem.menu_rect_x = str(x - self.width)
                elem.menu_rect_y = elem.rect_y
            case 3:
                elem.menu_rect_x = elem.rect_x
                elem.menu_rect_y = str(y - self.height)
            case 4:
                elem.menu_rect_x = str(x - self.width)
                elem.menu_rect_y = str(y - self.height)

        elem.menu_rect_w = elem.rect_w
        elem.menu_rect_h = elem.rect_h

        self.main_window.propertyEditor.update(elem)
  
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            if self.activeElem is not None:
                if self.cursor_within_dist and not self.is_resizing_inside():
                    self.click_pos = event.scenePos()
                    rect = self.activeElem.rect()

                    elem_pos = self.activeElem.rect()
                    elem_width = self.activeElem.boundingRect().width()
                    elem_height = self.activeElem.boundingRect().height()
                    if event.scenePos().x() < elem_pos.x() + self.resize_threshold and \
                        elem_pos.y() < event.scenePos().y() < elem_pos.y() + elem_height:
                        self.selected_edge = "left"
                    elif event.scenePos().x() > elem_pos.x() + elem_width - self.resize_threshold and \
                        elem_pos.y() < event.scenePos().y() < elem_pos.y() + elem_height:
                        self.selected_edge = "right"
                    elif event.scenePos().y() < elem_pos.y() + self.resize_threshold and \
                        elem_pos.x() < event.scenePos().x() < elem_pos.x() + elem_width:
                        self.selected_edge = "top"
                    elif event.scenePos().y() > elem_pos.y() + elem_height - self.resize_threshold and \
                        elem_pos.x() < event.scenePos().x() < elem_pos.x() + elem_width:
                        self.selected_edge = "bottom"
                    else:
                        self.selected_edge = None
                    
                    self.click_pos = event.scenePos()
                    self.click_rect = rect
    
    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if self.activeElem is not None and self.cursor_within_dist and not self.is_resizing_inside() and self.selected_edge is not None:

            """ Continue tracking movement while the mouse is pressed. """
            pos = event.scenePos()
            snap_to_grid = self.is_snap_to_grid_enabled()
            if snap_to_grid:
                blockSize = self.getBlockSize()

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

            # Then adjust by the distance the mouse moved.
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
            scene_rect = self.sceneRect()
            view_left = scene_rect.left()
            view_top = scene_rect.top()
            view_right = scene_rect.right()
            view_bottom = scene_rect.bottom()

            # Next, check if the rectangle has been dragged out of
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

            # update elem rect
            self.activeElem.setRect(rect)
            
            self.updateMenuAttributesAndElem_partsPos(self.activeElem)
        
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            if self.cursor_within_dist:
                # Re-enable sceneSelectionChanged signal
                self.selectionChanged.connect(self.sceneWatcher)
                self.cursor_within_dist = False

    def drawBackground(self, painter: QPainter, rect: QRect):
        """Draw background scene grid"""
        super().drawBackground(painter, rect)

        if self.drawGrid:
            # here we create our grid
            left = int(math.floor(rect.left()))
            right = int(math.ceil(rect.right()))
            top = int(math.floor(rect.top()))
            bottom = int(math.ceil(rect.bottom()))

            first_left = left - (left % self.gridSize)
            first_top = top - (top % self.gridSize)

            # compute all lines to be drawn
            lines = []
            # left to right
            for x in range(first_left, right, self.gridSize):
                lines.append(QLine(x, top, x, bottom))
            # top to bottom
            for y in range(first_top, bottom, self.gridSize):
                lines.append(QLine(left, y, right, y))

            # grid
            painter.setPen(self.grid_pen)
            painter.drawLines(lines)

        # quadrant grid
        if self.drawQuadrantGrid:
            painter.setPen(self.quadrant_pen)

            painter.drawLine(0.0, self.height/2, self.width, self.height/2)
            painter.drawLine(self.width/2, 0.0, self.width/2, self.height)

        # top left quadrant
        if self.drawQuadrantLabel:
            painter.setPen(self.quadrant_pen)

            painter.drawText(15, 10, 275, 15, Qt.AlignHCenter, 'HORIZONTAL_ALIGN_LEFT   VERTICAL_ALIGN_TOP')

            painter.drawText(87, 32, 15, 15, Qt.AlignHCenter, '0+')
            painter.drawLine(22, 40, 82, 40)
            painter.drawLine(67, 33, 82, 40)
            painter.drawLine(67, 47, 82, 41)

            painter.drawText(19, 105, 15, 15, Qt.AlignHCenter, '0+')
            painter.drawLine(21, 40, 21, 100)
            painter.drawLine(14, 85, 21, 100)
            painter.drawLine(28, 85, 22, 100)
