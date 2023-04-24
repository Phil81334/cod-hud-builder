from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QCursor, QPixmap, QMouseEvent
from PySide6.QtWidgets import QMainWindow, QGraphicsItem, QGraphicsScene, QGraphicsPixmapItem

class ManipulatorHandle(QGraphicsPixmapItem):
    def __init__(self, main_window: QMainWindow, scene: QGraphicsScene, pixmap: QPixmap, parent=None):
        super().__init__(pixmap, parent=parent)

        self.main_window = main_window
        self.scene = scene
        self.parent = parent
        self.pixmap = pixmap

        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.setAcceptHoverEvents(True)
        self.hoverEnterEvent = lambda event: self.setCursor(Qt.PointingHandCursor)
        self.hoverLeaveEvent = lambda event: self.setCursor(Qt.ArrowCursor)

        self.aspectRatioMode = Qt.KeepAspectRatio

        self.origWidth = self.pixmap.width()
        self.origHeight = self.pixmap.height()

        self.Size = 30.0
        self.Offset = self.Size

        rect = QRectF(
            self.parent.rect().x() + self.parent.rect().width() + self.Offset,
            self.parent.rect().y() + self.parent.rect().height() + self.Offset,
            self.Size,
            self.Size
        )
        self.rect = rect
        
        self.setPos(QPointF(
            self.rect.x(),
            self.rect.y())
        )
        
        self.setScale(self.rect.width() / self.origWidth)
        self.setScale(self.rect.height() / self.origHeight)

        self.click_pos = None
        self.movingViaHandle = False

    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.click_pos = self.pos()
            self.movingViaHandle = True

    def mouseMoveEvent(self, event: QMouseEvent):
        # center pixmap with cursor
        pos = self.scene.views()[0].mapFromGlobal(QCursor.pos())
        x = pos.x()-self.Offset / 2
        y = pos.y()-self.Offset / 2
        pos = QPointF(x, y)
        self.setPos(pos)

        # prevent pixmap from going out of scene bounds
        scene_rect = self.scene.sceneRect()
        x = self.qBound(scene_rect.left(), self.pos().x(), scene_rect.right()-self.Size)
        y = self.qBound(scene_rect.top(), self.pos().y(), scene_rect.bottom()-self.Size)
        pos = QPointF(x, y)
        self.setPos(pos)

        elem = self.parent
        elemType = elem.elemType
        quadrant = self.scene.getQuadrant(elem)
    
        coords = {
            1: (self.pos().x() - (elem.rect().width() + self.Size), self.pos().y() - (elem.rect().height() + self.Size)),
            2: (self.pos().x() + (self.Size * 2), self.pos().y() - (elem.rect().height() + self.Size)),
            3: (self.pos().x() - (elem.rect().width() + self.Size), self.pos().y() + (self.Size * 2)),
            4: (self.pos().x() + (self.Size * 2), self.pos().y() + (self.Size * 2))
        }
        # get coordinates for current quadrant
        x, y = coords.get(quadrant, (0, 0))
        rect = QRectF(x, y, elem.rect().width(), elem.rect().height())
        elem.setRect(rect)

        # prevent elem from going out of scene bounds (when being moved via handle)
        x = self.qBound(scene_rect.left(), elem.rect().x(), scene_rect.right()-elem.rect().width())
        y = self.qBound(scene_rect.top(), elem.rect().y(), scene_rect.bottom()-elem.rect().height())
        rect = QRectF(x, y, elem.rect().width(), elem.rect().height())
        elem.setRect(rect)

        self.scene.updateMenuAttributesAndElem_partsPos(elem)
    
    def qBound(self, lowerBound, value, upperBound):
        return max(lowerBound, min(value, upperBound))

    def mouseReleaseEvent(self, event: QMouseEvent):
        super().mouseReleaseEvent(event)
        self.setCursor(Qt.OpenHandCursor)
        self.movingViaHandle = False

        elem = self.parent
        handle = elem.manipulatorHandle
        match self.scene.getQuadrant(elem):
            case 1:
                x = elem.rect().x() + elem.rect().width() + handle.Offset
                y = elem.rect().y() + elem.rect().height() + handle.Offset
                handle.setPos(QPointF(x, y))
            case 2:
                x = elem.rect().x() - (handle.Offset *2)
                y = elem.rect().y() + elem.rect().height() + handle.Offset
                handle.setPos(QPointF(x, y))
            case 3:
                x = elem.rect().x() + elem.rect().width() + handle.Offset
                y = elem.rect().y() - (handle.Offset *2)
                handle.setPos(QPointF(x, y))
            case 4:
                x = elem.rect().x() - (handle.Offset *2)
                y = elem.rect().y() - (handle.Offset *2)
                handle.setPos(QPointF(x, y))