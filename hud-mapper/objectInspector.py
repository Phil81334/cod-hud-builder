from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem

from elem import Elem

class ObjectInspector:
    def __init__(self, main_window, scene):

        self.main_window = main_window
        self.scene = scene

        self.objectInspector = self.main_window.ui.object_inspector_list

        self.objectInspectorListModel = QStandardItemModel(self.objectInspector)

        self.objectInspector.setModel(self.objectInspectorListModel)

        self.main_window.ui.move_elem_up_list.clicked.connect(self.moveItemUp)
        self.main_window.ui.move_elem_down_list.clicked.connect(self.moveItemDown)
        self.main_window.ui.object_inspector_list.clicked.connect(self.itemClicked)
    
    def moveItemUp(self):
        index = self.objectInspector.currentIndex()
        row = index.row()
        if row > 0:
            item = self.objectInspectorListModel.takeRow(row)
            self.objectInspectorListModel.insertRow(row - 1, item)
            self.objectInspector.setCurrentIndex(item[0].index())

    def moveItemDown(self):
        index = self.objectInspector.currentIndex()
        row = index.row()
        if row < self.objectInspectorListModel.rowCount() - 1:
            item = self.objectInspectorListModel.takeRow(row)
            self.objectInspectorListModel.insertRow(row + 1, item)
            self.objectInspector.setCurrentIndex(item[0].index())
    
    def itemClicked(self, index: QModelIndex):
        elem_name = index.data()

        self.selectSceneItemFromList(index)
    
    def selectSceneItemFromList(self, index: QModelIndex):
        elem_name = index.data()

        for elem in self.scene.items():
            if isinstance(elem, Elem) and elem.name == elem_name:
                if not elem.isSelected():
                    self.scene.clearSelection()
                    elem.setSelected(True)
                    break

    def addItem(self, text: str):
        item = QStandardItem(text)
        self.objectInspectorListModel.appendRow(item)
    
    def removeItem(self, text: str):
        items = self.objectInspectorListModel.findItems(text, Qt.MatchExactly)
        if items:
            self.objectInspectorListModel.removeRow(items[0].row())
    
    def clearList(self):
        self.objectInspectorListModel.clear()
    
    def getSceneItemsInObjectInspectorOrder(self):
        elems = []
        for row in range(self.objectInspectorListModel.rowCount()):
            index = self.objectInspectorListModel.index(row, 0)
            text = index.data(Qt.DisplayRole)
            for elem in self.scene.items():
                if isinstance(elem, Elem) and elem.name == text:
                    elems.append(elem)
        return elems