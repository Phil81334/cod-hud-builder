########################################################################
## START

# AUTHOR: -Phil81334
# COMMUNITY: CME (CoD Modding Elite)
# DESCRIPTION: hud builder

## END
############################## ---/--/--- ##############################

from PySide6.QtCore import QModelIndex, QRectF
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PySide6.QtWidgets import QApplication, QDockWidget, QMainWindow, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QSizePolicy, QScrollArea, QWidget

from ui_hudMapper import Ui_MainWindow
from scene import Scene
from objectInspector import ObjectInspector
from propertyEditor import PropertyEditor
import icons

import os
from os.path import exists
import sys
import random

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = Scene(self)

        self.graphicsView = self.ui.graphicsView
        self.graphicsView.setScene(self.scene)

        self.initItemDefsList()
        self.objectInspector = ObjectInspector(self, self.scene)
        self.propertyEditor = PropertyEditor(self, self.scene)

        # remove the dock widget close btns
        self.ui.object_inspector.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)# | QDockWidget.DockWidgetVerticalTitleBar)
        self.ui.property_editor.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.ui.elems.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.ui.console.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        self.tabifyDockWidget(self.ui.object_inspector, self.ui.property_editor)
        self.tabifyDockWidget(self.ui.object_inspector, self.ui.console)
        self.ui.object_inspector.raise_()

        self.ui.clear_console.clicked.connect(self.clear_console)
        self.ui.generate_code.clicked.connect(self.generateCode)

        self.ui.help_btn.clicked.connect(self.openHelpDialog)

    def openHelpDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Keyboard Shortcuts")
        dialog.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        dialog.setMaximumWidth(1000)
        dialog.setMaximumHeight(500)

        scroll_area = QScrollArea(dialog)
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        text = (
            "CTRL + O: Open Scene\n"
            "CTRL + S: Save Scene\n\n"

            "DELETE: Delete Elem\n"
            "SPACE: Copy Elem\n\n"

            "CTRL + H: Split Elem Horizontally\n"
            "CTRL + V: Split Elem Vetically\n\n"

            "CTRL + Right-Arrow Key: Mirrow Elem (to right)\n"
            "CTRL + LEFT-Arrow Key: Mirrow Elem (to left)\n"
            "CTRL + UP-Arrow Key: Mirrow Elem (to up)\n"
            "CTRL + DOWN-Arrow Key: Mirrow Elem (to down)\n\n"

            "SHIFT + Right-Arrow Key: Move elem by snap-to-grid size[default = 10] (to right)\n"
            "SHIFT + LEFT-Arrow Key: Move Elem (to left)\n"
            "SHIFT + UP-Arrow Key: Move Elem (to up)\n"
            "SHIFT + DOWN-Arrow Key: Move Elem (to down)\n"

            "Note: Mirror Elem only has 2 allowed directions.\nThese directions depend on which quadrant the elem resides in.\n\n"

            "When manually entering values into the text boxes you will need to hit enter for the value to be applied.\n\n"

            "Note: When clicking off the scene(on a checkbox or btn etc), the focus will remain on the active(selected) elem.\nMeaning keyboard shortcuts will still work with the exception of clicking on text areas. So in this case you will need to click back on the active elem for shortcuts to work."
        )
        label_text = QLabel(text)
        content_layout.addWidget(label_text)

        current_dir = os.getcwd()
        pixmap1 = QPixmap(rf"{current_dir}\img\text-alignment-noWidth_noHeight-example.png")
        label_img1 = QLabel()
        label_img1.setPixmap(pixmap1)
        content_layout.addWidget(label_img1)

        pixmap2 = QPixmap(rf"{current_dir}\img\text-alignment-Width_Height-example.png")
        label_img2 = QLabel()
        label_img2.setPixmap(pixmap2)
        content_layout.addWidget(label_img2)

        scroll_area.setWidget(content_widget)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(dialog.reject)

        layout = QVBoxLayout(dialog)
        layout.addWidget(scroll_area)
        layout.addWidget(buttonBox)

        dialog.exec()

    def initItemDefsList(self):
        self.listView = self.ui.elems_list

        self.listViewModel = QStandardItemModel()
        self.listView.setModel(self.listViewModel)

        values = ['Text', 'Material', 'Button']
        for i in values:
            self.listViewModel.appendRow(QStandardItem(i))
        
        self.listView.clicked[QModelIndex].connect(self.itemDefsOnClick)
    
    def itemDefsOnClick(self, index):
        item = self.listViewModel.itemFromIndex(index)
        elemType = item.text()
        self.scene.addElem(QRectF(10.0, 10.0, 150.0, 30.0), elemType, False)

    def clear_console(self) -> None:
        self.ui.console_text_area.clear()

    def generateCode(self):
        if not len(self.scene.elems) > 0:
            return
        
        self.ui.console_text_area.clear()

        header = (
            "menuDef\n"
            "{\n"
            '   name        "placeholder"\n'
            "   fullScreen  0\n"
            "   visible     1\n"
        )

        eof = (
            "\n"
            "}"
        )

        itemDefs = ""

        itemDefStart = (
            "\n"
            "   itemDef\n"
		    "   {\n"
        )

        itemDefEnd = "   }"

        elems = self.objectInspector.getSceneItemsInObjectInspectorOrder()
        for elem in elems:
            elem.info = []
            elem.info.append(f'name¬"{elem.name}"')
            elem.info.append(f"rect¬{elem.menu_rect_x} {elem.menu_rect_y} {elem.menu_rect_w} {elem.menu_rect_h} {elem.rect_h_align} {elem.rect_v_align}")
            elemType = elem.elemType
            if elemType == "Text":
                elem.info.append(f"type¬{elem._type_}")
                elem.info.append(f"forecolor¬{elem.forecolor}")
                if elem.text_type == "text":
                    elem.info.append(f'text¬"{elem.text}"')
                else:
                    elem.info.append(f'exp text¬ dvarString( "{elem.text}" )')
                elem.info.append(f"textfont¬{elem.textfont}")
                elem.info.append(f"textscale¬{elem.textscale}")
                elem.info.append(f"textstyle¬{elem.textstyle}")
                elem.info.append(f"textalign¬{elem.textalign}")
                elem.info.append(f"visible¬{elem.visible}")
                if elem.decoration:
                    elem.info.append(f"decoration¬")
            elif elemType == "Material":
                elem.info.append(f"style¬{elem.style}")
                elem.info.append(f"forecolor¬{elem.forecolor}")
                if elem.background_material_text_type == "background":
                    elem.info.append(f'background¬"{elem.background_material_text}"')
                else:
                    elem.info.append(f'exp material¬ dvarString( "{elem.background_material_text}" )')
                elem.info.append(f"visible¬{elem.visible}")
            elif elemType == "Button":
                elem.info.append(f"type¬{elem._type_}")
                elem.info.append(f"visible¬{elem.visible}")
                elem.info.append(f"action¬{elem.action}")
                elem.info.append(f"mouseEnter¬{elem.mouseEnter}")
                elem.info.append(f"mouseExit¬{elem.mouseExit}")

            itemDefs += itemDefStart
            for j in range(len(elem.info)):
                info = elem.info[j]
                if info.split('¬')[0] == "action" or info.split('¬')[0] == "mouseEnter" or info.split('¬')[0] == "mouseExit":
                    itemDefs += (
                        f"      {info.split('¬')[0]}\n"
                        "      {\n"
                        f"        {info.split('¬')[1]}\n"
                        "      }\n"
                    )
                else:
                    itemDefs += f"      {info.split('¬')[0]}    {info.split('¬')[1]}\n"
            itemDefs += itemDefEnd

            elem.info.clear()
            elem.info = None
        
        footer = '\n\n\n/*\nAdd:\nmenufile,ui/filename.extension to mod.csv\n#include "ui/file.extension" to hud.menu'+"(you'll have to figure out where exactly).\n*/"
        code = f"{header}{itemDefs}{eof}{footer}"
        which = "console" if self.ui.code_output_console.isChecked() else 'file' if self.ui.code_output_file.isChecked() else 'both'
        actions = {
            "console": self.ui.console_text_area.insertPlainText,
            "file": self.init_file
        }

        for option in ("console", "file"):
            if which in (option, "both"):
                actions[option](code)
    
    def init_file(self, code):
        ext = "txt" if self.ui.txt_ext.isChecked() else 'inc' if self.ui.inc_ext.isChecked() else 'menu'
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        path = rf"{desktop}\cod_hud_layout.{ext}"
        if not os.path.exists(path):
            self.write_to_file(path, code)
        else:
            # find a name that doesnt exist
            while os.path.exists(f"{path}"):
                path = rf"{path.split('.')[0]}_{random.randint(0, 1000)}.{ext}"
            self.write_to_file(path, code)
    
    def write_to_file(self, path, code) -> None:
        f = open(path, "w+")
        f.write(code)
        f.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        pass
