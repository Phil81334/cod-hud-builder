import os

from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PySide6.QtWidgets import QLineEdit

class BackgroundImgDrop(QLineEdit):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)

        self.main_window = main_window

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            try:
                event.acceptProposedAction()
            except Exception as e:
                event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            filename, extension = os.path.splitext(url.path())
            if extension in ['.png', '.jpg', '.jpeg', '.tga', '.dds']:
                try:
                    path = url.path()[1:]
                    img_name = os.path.splitext(os.path.basename(path))[0]

                    if self.main_window.propertyEditor.background_material_type.currentText() == "background":
                        self.setText(img_name)
                    else:
                        self.setText(f'dvarString( "{img_name}" )')

                    self.main_window.propertyEditor.manualAttributeOverride("background_material_text")
                except Exception as e:
                    print(f"Something went wrong when trying to update elem.background_material_text attr\n{e}")
            else:
                print("Tried to drop an invalid item (accepted extension types['.png', '.jpg', '.jpeg', '.tga', '.dds'])")
