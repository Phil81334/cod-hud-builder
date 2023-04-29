from PySide6.QtCore import QRectF, QPointF
from PySide6.QtWidgets import QFileDialog, QMainWindow, QGraphicsScene, QComboBox

from ui_customPropertyEditor import Ui_Form
from elem import Elem

import os
import re

class PropertyEditor(Ui_Form):
    def __init__(self, main_window: QMainWindow, scene: QGraphicsScene) -> None:
        super().__init__(main_window)

        self.main_window = main_window
        self.scene = scene

        # property_editor_c = QWidget, which is auto created when you add a QDockWidget
        self.setupUi(self.main_window.ui.property_editor_c)
        
        # hide widget upon initial load. this will be shown/hidden based on elem count/selected status.
        self.scrollArea.hide()

        # lineEdit
        self.rect_x.returnPressed.connect(lambda: self.manualAttributeOverride("rect_x"))
        self.rect_y.returnPressed.connect(lambda: self.manualAttributeOverride("rect_y"))
        self.rect_w.returnPressed.connect(lambda: self.manualAttributeOverride("rect_w"))
        self.rect_h.returnPressed.connect(lambda: self.manualAttributeOverride("rect_h"))
        self.forecolor.returnPressed.connect(lambda: self.manualAttributeOverride("forecolor"))

        self.text.returnPressed.connect(lambda: self.manualAttributeOverride("text"))
        self.background_material_text.returnPressed.connect(lambda: self.manualAttributeOverride("background_material_text"))

        self.textscale.returnPressed.connect(lambda: self.manualAttributeOverride("textscale"))
        self.visible.returnPressed.connect(lambda: self.manualAttributeOverride("visible"))
        self.action.returnPressed.connect(lambda: self.manualAttributeOverride("action"))
        self.mouseEnter.returnPressed.connect(lambda: self.manualAttributeOverride("mouseEnter"))
        self.mouseExit.returnPressed.connect(lambda: self.manualAttributeOverride("mouseExit"))

        # comboBox
        self.init_combo_box_values()
        self.combo_box_widgets = [self.rect_h_align, self.rect_v_align, self.text_type, self.textfont, self.textstyle, self.textalign, self.style, self.background_material_type]
        self.combo_box_widget_names = ['rect_h_align', 'rect_v_align', 'text_type', 'textfont', 'textstyle', 'textalign', 'style', 'background_material_type']

        # checkBox
        self.decoration.stateChanged.connect(lambda: self.manualAttributeOverride("decoration"))

        # btn
        self.material_selector_btn.clicked.connect(self.select_material)

        # inform user they cant use the '¬' symbol for text elems, text
        self.text.setPlaceholderText("The `¬' symbol is reserved, do not use!")

        self.text_align_default_values = ['ITEM_ALIGN_MIDDLE_LEFT', 'ITEM_ALIGN_MIDDLE_RIGHT']

    def set_text_placeholder_text(self) -> None:

        elem = self.scene.activeElem
        if self.text_type.currentText() == "text":
            self.text.setText(elem.text)
            elem.text_type = "text"
        else:
            self.text.setText(f'dvarString( "{elem.text}" )')
            elem.text_type = "exp text"

    def set_material_placeholder_text(self) -> None:

        elem = self.scene.activeElem
        if self.background_material_type.currentText() == "background":
            self.background_material_text.setText(elem.background_material_text)
            elem.background_material_text_type = "background"
        else:
            self.background_material_text.setText(f'dvarString( "{elem.background_material_text}" )')
            elem.background_material_text_type = "exp material"
  
    def select_material(self) -> None:

        file_path, _ = QFileDialog.getOpenFileName(None, "Select Material", "", "All Files (*)")
        if file_path:
            material_name = os.path.splitext(os.path.basename(file_path))[0]
            if material_name:
                self.background.setText(material_name)
                self.manualAttributeOverride("background")

    def init_combo_box_values(self) -> None:
        """ Called count: 1 """

        self.rect_h_align.addItems([
            # 'HORIZONTAL_ALIGN_SUBLEFT',
            'HORIZONTAL_ALIGN_LEFT',
            # 'HORIZONTAL_ALIGN_CENTER',
            'HORIZONTAL_ALIGN_RIGHT'#,
            # 'HORIZONTAL_ALIGN_FULLSCREEN',
            # 'HORIZONTAL_ALIGN_NOSCALE',
            # 'HORIZONTAL_ALIGN_TO640',
            # 'HORIZONTAL_ALIGN_CENTER_SAFEAREA',
            # 'HORIZONTAL_ALIGN_MAX',
            # 'HORIZONTAL_ALIGN_DEFAULT'
        ])
        
        self.rect_v_align.addItems([
            # 'VERTICAL_ALIGN_SUBTOP',
            'VERTICAL_ALIGN_TOP',
            # 'VERTICAL_ALIGN_CENTER',
            'VERTICAL_ALIGN_BOTTOM'#,
            # 'VERTICAL_ALIGN_FULLSCREEN',
            # 'VERTICAL_ALIGN_NOSCALE',
            # 'VERTICAL_ALIGN_TO480',
            # 'VERTICAL_ALIGN_CENTER_SAFEAREA',
            # 'VERTICAL_ALIGN_MAX',
            # 'VERTICAL_ALIGN_DEFAULT'
        ])

        self.text_type.addItems([
            'text',
            'exp text'
        ])

        self.textfont.addItems([
            'UI_FONT_NORMAL',
            'UI_FONT_BIG',
            'UI_FONT_SMALL',
            'UI_FONT_BOLD',
            'UI_FONT_CONSOLE',
            'UI_FONT_OBJECTIVE',
            'UI_FONT_MAX'
        ])
        
        self.textstyle.addItems([
            'ITEM_TEXTSTYLE_NORMAL',
            'ITEM_TEXTSTYLE_BLINK',
            'ITEM_TEXTSTYLE_SHADOWED',
            'ITEM_TEXTSTYLE_SHADOWEDMORE',
            'ITEM_TEXTSTYLE_MONOSPACE'
        ])
    
        self.textalign.addItems([
            # 'ITEM_ALIGN_LEGACY_LEFT',
            # 'ITEM_ALIGN_LEGACY_CENTER',
            # 'ITEM_ALIGN_LEGACY_RIGHT',
            'ITEM_ALIGN_TOP_LEFT',
            'ITEM_ALIGN_TOP_CENTER',
            'ITEM_ALIGN_TOP_RIGHT',
            'ITEM_ALIGN_MIDDLE_LEFT',
            'ITEM_ALIGN_MIDDLE_CENTER',
            'ITEM_ALIGN_MIDDLE_RIGHT',
            'ITEM_ALIGN_BOTTOM_LEFT',
            'ITEM_ALIGN_BOTTOM_CENTER',
            'ITEM_ALIGN_BOTTOM_RIGHT'
        ])

        self.style.addItems([
            # 'WINDOW_STYLE_EMPTY',
            # 'WINDOW_STYLE_FILLED',
            # 'WINDOW_STYLE_GRADIENT',
            'WINDOW_STYLE_SHADER'#,
            # 'WINDOW_STYLE_TEAMCOLOR',
            # 'WINDOW_STYLE_DVAR_SHADER',
            # 'WINDOW_STYLE_LOADBAR'
        ])

        self.background_material_type.addItems([
            'background',
            'exp material'
        ])

        self.set_combo_box_face_value()
        self.connect_combo_box_signals()

    # this basically means the text you see when drop down list is closed
    # created this method as these values will need to be reset when clearing/opening scene
    def set_combo_box_face_value(self) -> None:

        # this basically means the text you see when drop down list is closed
        # created this method as these values will need to be reset when clearing/opening scene

        self.rect_h_align.setCurrentText("HORIZONTAL_ALIGN_LEFT")
        # this: self.rect_h_align.setCurrentIndex(0), does the same thing as the above line. as that above str is at index 0

        self.rect_v_align.setCurrentText("VERTICAL_ALIGN_TOP")
        # this: self.rect_h_align.setCurrentIndex(self.rect_h_align.findText("HORIZONTAL_ALIGN_LEFT")), does the same thing as the above line

        self.text_type.setCurrentText("text")
        self.textfont.setCurrentText("UI_FONT_OBJECTIVE") # 5
        self.textstyle.setCurrentText("ITEM_TEXTSTYLE_NORMAL")
        self.textalign.setCurrentText("ITEM_ALIGN_MIDDLE_LEFT") # 3
        self.style.setCurrentText("WINDOW_STYLE_SHADER")
        self.background_material_type.setCurrentText("background")
    
    def connect_combo_box_signals(self) -> None:
        """ Called count: 1 """

        self.rect_h_align.currentIndexChanged.connect(lambda: self.manualAttributeOverride("rect_h_align"))
        self.rect_v_align.currentIndexChanged.connect(lambda: self.manualAttributeOverride("rect_v_align"))
        self.text_type.currentIndexChanged.connect(lambda: self.manualAttributeOverride("text_type"))
        self.textfont.currentIndexChanged.connect(lambda: self.manualAttributeOverride("textfont"))
        self.textstyle.currentIndexChanged.connect(lambda: self.manualAttributeOverride("textstyle"))
        self.textalign.currentIndexChanged.connect(lambda: self.manualAttributeOverride("textalign"))
        self.style.currentIndexChanged.connect(lambda: self.manualAttributeOverride("style"))
        self.background_material_type.currentIndexChanged.connect(lambda: self.manualAttributeOverride("background_material_type"))

        self.text_type.currentIndexChanged.connect(self.set_text_placeholder_text)
        self.background_material_type.currentIndexChanged.connect(self.set_material_placeholder_text)

    def change_specific_combo_box_signal_state(self, widget: QComboBox, widget_name: str, enabled: bool) -> None:
        # if hasattr(self, widget_name) and isinstance(widget, QComboBox):
        widget.blockSignals(enabled)
    
    def change_all_combo_box_signals_state(self, enabled: bool) -> None:
        for i in range(len(self.combo_box_widgets)):
            # if hasattr(self, self.combo_box_widget_names[i]) and isinstance(self.combo_box_widgets[i], QComboBox):
            self.combo_box_widgets[i].blockSignals(enabled)

    def update(self, elem: Elem) -> None:
        """
        Called:
        When elem attributes get dynamically updated this method will need to be called to reflect the new values
        Or if a new/diff elem is selected.
        """
        elemType = elem.elemType
        
        # all types use rect.
        self.rect_x.setText(elem.rect_x)
        self.rect_y.setText(elem.rect_y)
        self.rect_w.setText(elem.rect_w)
        self.rect_h.setText(elem.rect_h)

        self.menu_rect_x.setText(elem.menu_rect_x)
        self.menu_rect_y.setText(elem.menu_rect_y)
        self.menu_rect_w.setText(elem.menu_rect_w)
        self.menu_rect_h.setText(elem.menu_rect_h)

        self.rect_h_align.setCurrentText(elem.rect_h_align)
        self.rect_v_align.setCurrentText(elem.rect_v_align)
        
        if elemType == "Text":
            # 'elem.[type] is a predefined python keyword. so cant use that.
            self.typeFrame.show()
            self.type.setText(elem._type_)

            # text doesnt use 'style' so hide that
            self.styleFrame.hide()

            self.forecolorFrame.show()
            self.forecolor.setText(elem.forecolor)

            # text doesnt use 'background' so hide that
            self.backgroundFrame.hide()

            self.textFrame.show()
            if elem.text_type == "text":
                self.text.setText(elem.text)
                self.text_type.setCurrentText("text")
            else:
                self.text.setText(f'dvarString( "{elem.text}" )')
                self.text_type.setCurrentText("exp text")

            self.textfontFrame.show()
            self.textfont.setCurrentText(elem.textfont)

            self.textscaleFrame.show()
            self.textscale.setText(elem.textscale)

            self.textstyleFrame.show()
            self.textstyle.setCurrentText(elem.textstyle)

            self.textalignFrame.show()
            self.textalign.setCurrentText(elem.textalign)

            self.visible.setText(elem.visible)

            self.decorationFrame.show()
            self.decoration.setChecked(elem.decoration)
         
            self.actionFrame.hide()
            self.mouseEnterFrame.hide()
            self.mouseExitFrame.hide()
        elif elemType == "Material":
            self.typeFrame.hide()

            self.styleFrame.show()
            self.style.setCurrentText(elem.style)

            self.forecolorFrame.show()
            self.forecolor.setText(elem.forecolor)

            self.backgroundFrame.show()
            if elem.background_material_text_type == "background":
                self.background_material_text.setText(elem.background_material_text)
                self.background_material_type.setCurrentText("background")
            else:
                self.background_material_text.setText(f'dvarString( "{elem.background_material_text}" )')
                self.background_material_type.setCurrentText("exp material")

            self.textFrame.hide()
            self.textfontFrame.hide()
            self.textscaleFrame.hide()
            self.textstyleFrame.hide()
            self.textalignFrame.hide()

            self.visible.setText(elem.visible)

            self.decorationFrame.hide()

            self.actionFrame.hide()
            self.mouseEnterFrame.hide()
            self.mouseExitFrame.hide()
        elif elemType == "Button":
            self.typeFrame.show()
            self.type.setText(elem._type_)

            self.styleFrame.hide()

            self.forecolorFrame.hide()

            self.backgroundFrame.hide()

            self.textFrame.hide()
            self.textfontFrame.hide()
            self.textscaleFrame.hide()
            self.textstyleFrame.hide()
            self.textalignFrame.hide()

            self.visible.setText(elem.visible)

            self.decorationFrame.hide()

            self.actionFrame.show()
            self.action.setText(elem.action)

            self.mouseEnterFrame.show()
            self.mouseEnter.setText(elem.mouseEnter)

            self.mouseExitFrame.show()
            self.mouseExit.setText(elem.mouseExit)

        self.scrollArea.show()

    def manualAttributeOverride(self, which):
        """
        This updates elems attributes (scene & menu), and if any value is of rect, then it will also physically move the elem
        No need to call the update() method at the end of this method cause once the user manually changes the widget value, it auto-saves so to speak
        """

        scene = self.scene
        elem = scene.activeElem

        # if elem is None:
        #     return
        
        elemType = elem.elemType

        match which:
            case "forecolor":
                elem.forecolor = self.forecolor.text()
            case "background_material_text":
                text = self.background_material_text.text()
                if elem.background_material_text_type == "exp material":
                    match = re.search(r'"([^"]*)"', text)
                    if match:
                        text = match.group(1)
                    else:
                        # user removed double quotes when they shouldnt have
                        text = elem.name

                elem.background_material_text = text

            case "text":
                text = self.text.text()
                if elem.text_type == "exp text":
                    match = re.search(r'"([^"]*)"', text)
                    if match:
                        text = match.group(1)
                    else:
                        # user removed double quotes when they shouldnt have
                        text = elem.name

                elem.text = text
                elem.textItem.setPlainText(elem.text)
            case "textalign":
                elem.textalign = self.textalign.currentText()
                if elem.textalign not in self.text_align_default_values and not elem.text_align_overridden:
                    elem.text_align_overridden = True
            case "textscale":
                elem.textscale = self.textscale.text()
            case "visible":
                elem.visible = self.visible.text()
            case "action":
                elem.action = self.action.text()
            case "mouseEnter":
                elem.mouseEnter = self.mouseEnter.text()
            case "mouseExit":
                elem.mouseExit = self.mouseExit.text()
            case "style":
                elem.style = self.style.currentText()
            case "textfont":
                elem.textfont = self.textfont.currentText()
            case "textstyle":
                elem.textstyle = self.textstyle.currentText()
            case "decoration":
                elem.decoration = self.decoration.isChecked() # type: bool
            case _:
                # elem rect(x,y,w,y), quadrant, rect_h_align, rect_v_align, textalign & menu_rect(x,y,w,h)
                elem.rect_x = float(self.rect_x.text())
                elem.rect_y = float(self.rect_y.text())
                elem.rect_w = float(self.rect_w.text())
                elem.rect_h = float(self.rect_h.text())

                # update rect, text item, x-pos & quadrant indicator if user isnt moving elem via mouse
                if not elem.movingElemViaMouse:
                    elem.setRect(elem.rect_x, elem.rect_y, elem.rect_w, elem.rect_h)

                    elem.xPosIndicator.setRect(QRectF(elem.rect().x()-elem.xPosIndicatorOffset, elem.rect().y()-elem.xPosIndicatorOffset, elem.xPosIndicatorSize, elem.xPosIndicatorSize))

                    if elem.elemType == 'Text':
                        elem.textItem.setPos(QPointF(elem.rect().x() + elem.textItemOffset, elem.rect().y() + elem.textItemOffset))

                # elem rect attributes need to be stores as a str but in order to determine which quadrant elem is in, values need to be float. 
                # so convert property editor values to float, mphysically adjust elem, do the calculations, then set rect attributes back to str
                match scene.getQuadrant(elem):
                    case 1:
                        if not elem.movingElemViaMouse:
                            elem.quadrantIndicator.setRect(QRectF(elem.rect().x()-elem.quadrandIndicatorOffset, elem.rect().y()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                        elem.rect_h_align = "HORIZONTAL_ALIGN_LEFT"
                        elem.rect_v_align = "VERTICAL_ALIGN_TOP"
                        if elemType == "Text":
                            # check if user has overridden the default(auto adjusted) value. if so, leave as is.
                            if not elem.text_align_overridden:
                                elem.textalign = "ITEM_ALIGN_MIDDLE_LEFT"
                        elem.menu_rect_x = str(elem.rect_x)
                        elem.menu_rect_y = str(elem.rect_y)

                        if not elem.manipulatorHandle.movingViaHandle:
                            handle = elem.manipulatorHandle
                            x = elem.rect().x() + elem.rect().width() + handle.Offset
                            y = elem.rect().y() + elem.rect().height() + handle.Offset
                            handle.setPos(QPointF(x, y))
                    case 2:
                        if not elem.movingElemViaMouse:
                            elem.quadrantIndicator.setRect(QRectF(elem.rect().x()+elem.rect().width()-elem.quadrandIndicatorOffset, elem.rect().y()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                        elem.rect_h_align = "HORIZONTAL_ALIGN_RIGHT"
                        elem.rect_v_align = "VERTICAL_ALIGN_TOP"
                        if elemType == "Text":
                            if not elem.text_align_overridden:
                                elem.textalign = "ITEM_ALIGN_MIDDLE_RIGHT"
                        elem.menu_rect_x = str(elem.rect_x - scene.width)
                        elem.menu_rect_y = str(elem.rect_y)

                        if not elem.manipulatorHandle.movingViaHandle:
                            handle = elem.manipulatorHandle
                            x = elem.rect().x() - (handle.Offset *2)
                            y = elem.rect().y() + elem.rect().height() + handle.Offset
                            handle.setPos(QPointF(x, y))
                    case 3:
                        if not elem.movingElemViaMouse:
                            elem.quadrantIndicator.setRect(QRectF(elem.rect().x()-elem.quadrandIndicatorOffset, elem.rect().y()+elem.rect().height()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                        elem.rect_h_align = "HORIZONTAL_ALIGN_LEFT"
                        elem.rect_v_align = "VERTICAL_ALIGN_BOTTOM"
                        if elemType == "Text":
                            if not elem.text_align_overridden:
                                elem.textalign = "ITEM_ALIGN_MIDDLE_LEFT"
                        elem.menu_rect_x = str(elem.rect_x)
                        elem.menu_rect_y = str(elem.rect_y - scene.height)

                        if not elem.manipulatorHandle.movingViaHandle:
                            handle = elem.manipulatorHandle
                            x = elem.rect().x() + elem.rect().width() + handle.Offset
                            y = elem.rect().y() - (handle.Offset *2)
                            handle.setPos(QPointF(x, y))
                    case 4:
                        if not elem.movingElemViaMouse:
                            elem.quadrantIndicator.setRect(QRectF(elem.rect().x()+elem.rect().width()-elem.quadrandIndicatorOffset, elem.rect().y()+elem.rect().height()-elem.quadrandIndicatorOffset, elem.quadrandIndicatorSize, elem.quadrandIndicatorSize))
                        elem.rect_h_align = "HORIZONTAL_ALIGN_RIGHT"
                        elem.rect_v_align = "VERTICAL_ALIGN_BOTTOM"
                        if elemType == "Text":
                            if not elem.text_align_overridden:
                                elem.textalign = "ITEM_ALIGN_MIDDLE_RIGHT"
                        elem.menu_rect_x = str(elem.rect_x - scene.width)
                        elem.menu_rect_y = str(elem.rect_y - scene.height)

                        if not elem.manipulatorHandle.movingViaHandle:
                            handle = elem.manipulatorHandle
                            x = elem.rect().x() - (handle.Offset *2)
                            y = elem.rect().y() - (handle.Offset *2)
                            handle.setPos(QPointF(x, y))
                
                elem.menu_rect_w = str(elem.rect_w)
                elem.menu_rect_h = str(elem.rect_h)
                
                elem.rect_x = str(elem.rect_x)
                elem.rect_y = str(elem.rect_y)
                elem.rect_w = str(elem.rect_w)
                elem.rect_h = str(elem.rect_h)
