from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtWidgets import QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QSizePolicy, QToolButton, QVBoxLayout, QWidget
from backgroundImgDrop import BackgroundImgDrop

class Ui_Form(object):
    def __init__(self, main_window):
        self.main_window = main_window

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(528, 765)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -35, 491, 780))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.frame_47 = QFrame(self.frame_5)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy4)
        self.frame_47.setMaximumSize(QSize(16777215, 50))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_47)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(50, 0))
        self.label_52.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.label_52)

        self.rect_x = QLineEdit(self.frame_47)
        self.rect_x.setObjectName(u"rect_x")
        self.rect_x.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout_9.addWidget(self.rect_x)


        self.verticalLayout_2.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_5)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy4.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy4)
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_48)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(50, 0))
        self.label_53.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_60.addWidget(self.label_53)

        self.rect_y = QLineEdit(self.frame_48)
        self.rect_y.setObjectName(u"rect_y")

        self.horizontalLayout_60.addWidget(self.rect_y)


        self.verticalLayout_2.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_5)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy4.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy4)
        self.frame_49.setMaximumSize(QSize(16777215, 50))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_49)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(50, 0))
        self.label_54.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_61.addWidget(self.label_54)

        self.rect_w = QLineEdit(self.frame_49)
        self.rect_w.setObjectName(u"rect_w")

        self.horizontalLayout_61.addWidget(self.rect_w)


        self.verticalLayout_2.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_5)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy4.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy4)
        self.frame_50.setMaximumSize(QSize(16777215, 50))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_50)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(50, 0))
        self.label_55.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_62.addWidget(self.label_55)

        self.rect_h = QLineEdit(self.frame_50)
        self.rect_h.setObjectName(u"rect_h")

        self.horizontalLayout_62.addWidget(self.rect_h)


        self.verticalLayout_2.addWidget(self.frame_50)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.menu_rect_x = QLineEdit(self.frame_2)
        self.menu_rect_x.setObjectName(u"menu_rect_x")
        self.menu_rect_x.setFocusPolicy(Qt.NoFocus)
        self.menu_rect_x.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.menu_rect_x)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 0))
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.menu_rect_y = QLineEdit(self.frame_3)
        self.menu_rect_y.setObjectName(u"menu_rect_y")
        self.menu_rect_y.setFocusPolicy(Qt.NoFocus)
        self.menu_rect_y.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.menu_rect_y)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 0))
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.menu_rect_w = QLineEdit(self.frame_4)
        self.menu_rect_w.setObjectName(u"menu_rect_w")
        self.menu_rect_w.setFocusPolicy(Qt.NoFocus)
        self.menu_rect_w.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.menu_rect_w)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(50, 0))
        self.label_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_7.addWidget(self.label_10)

        self.menu_rect_h = QLineEdit(self.frame_6)
        self.menu_rect_h.setObjectName(u"menu_rect_h")
        self.menu_rect_h.setFocusPolicy(Qt.NoFocus)
        self.menu_rect_h.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.menu_rect_h)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_7)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy4.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy4)
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_51)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(50, 0))
        self.label_56.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_63.addWidget(self.label_56)

        self.rect_h_align = QComboBox(self.frame_51)
        self.rect_h_align.setObjectName(u"rect_h_align")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.rect_h_align.sizePolicy().hasHeightForWidth())
        self.rect_h_align.setSizePolicy(sizePolicy5)

        self.horizontalLayout_63.addWidget(self.rect_h_align)


        self.verticalLayout.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_7)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy4.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy4)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_52)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(50, 0))
        self.label_57.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_64.addWidget(self.label_57)

        self.rect_v_align = QComboBox(self.frame_52)
        self.rect_v_align.setObjectName(u"rect_v_align")
        sizePolicy5.setHeightForWidth(self.rect_v_align.sizePolicy().hasHeightForWidth())
        self.rect_v_align.setSizePolicy(sizePolicy5)

        self.horizontalLayout_64.addWidget(self.rect_v_align)


        self.verticalLayout.addWidget(self.frame_52)

        self.typeFrame = QFrame(self.frame_7)
        self.typeFrame.setObjectName(u"typeFrame")
        sizePolicy4.setHeightForWidth(self.typeFrame.sizePolicy().hasHeightForWidth())
        self.typeFrame.setSizePolicy(sizePolicy4)
        self.typeFrame.setFrameShape(QFrame.StyledPanel)
        self.typeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.typeFrame)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.typeFrame)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(50, 0))
        self.label_58.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_65.addWidget(self.label_58)

        self.type = QLineEdit(self.typeFrame)
        self.type.setObjectName(u"type")
        self.type.setReadOnly(True)

        self.horizontalLayout_65.addWidget(self.type)


        self.verticalLayout.addWidget(self.typeFrame)

        self.styleFrame = QFrame(self.frame_7)
        self.styleFrame.setObjectName(u"styleFrame")
        sizePolicy4.setHeightForWidth(self.styleFrame.sizePolicy().hasHeightForWidth())
        self.styleFrame.setSizePolicy(sizePolicy4)
        self.styleFrame.setFrameShape(QFrame.StyledPanel)
        self.styleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.styleFrame)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.styleFrame)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(50, 0))
        self.label_67.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_74.addWidget(self.label_67)

        self.style = QComboBox(self.styleFrame)
        self.style.setObjectName(u"style")
        sizePolicy5.setHeightForWidth(self.style.sizePolicy().hasHeightForWidth())
        self.style.setSizePolicy(sizePolicy5)

        self.horizontalLayout_74.addWidget(self.style)


        self.verticalLayout.addWidget(self.styleFrame)

        self.forecolorFrame = QFrame(self.frame_7)
        self.forecolorFrame.setObjectName(u"forecolorFrame")
        sizePolicy4.setHeightForWidth(self.forecolorFrame.sizePolicy().hasHeightForWidth())
        self.forecolorFrame.setSizePolicy(sizePolicy4)
        self.forecolorFrame.setFrameShape(QFrame.StyledPanel)
        self.forecolorFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.forecolorFrame)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.forecolorFrame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(50, 0))
        self.label_59.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_66.addWidget(self.label_59)

        self.forecolor = QLineEdit(self.forecolorFrame)
        self.forecolor.setObjectName(u"forecolor")

        self.horizontalLayout_66.addWidget(self.forecolor)


        self.verticalLayout.addWidget(self.forecolorFrame)

        self.backgroundFrame = QFrame(self.frame_7)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.backgroundFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.background_material_type = QComboBox(self.backgroundFrame)
        self.background_material_type.setObjectName(u"background_material_type")
        self.background_material_type.setMinimumSize(QSize(100, 0))
        self.background_material_type.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.background_material_type)

        self.background_material_text = BackgroundImgDrop(self.main_window, self.backgroundFrame)
        self.background_material_text.setObjectName(u"background_material_text")

        self.horizontalLayout_4.addWidget(self.background_material_text)

        self.material_selector_btn = QToolButton(self.backgroundFrame)
        self.material_selector_btn.setObjectName(u"material_selector_btn")

        self.horizontalLayout_4.addWidget(self.material_selector_btn)


        self.verticalLayout.addWidget(self.backgroundFrame)

        self.textFrame = QFrame(self.frame_7)
        self.textFrame.setObjectName(u"textFrame")
        sizePolicy4.setHeightForWidth(self.textFrame.sizePolicy().hasHeightForWidth())
        self.textFrame.setSizePolicy(sizePolicy4)
        self.textFrame.setFrameShape(QFrame.StyledPanel)
        self.textFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.textFrame)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.text_type = QComboBox(self.textFrame)
        self.text_type.setObjectName(u"text_type")
        self.text_type.setMinimumSize(QSize(100, 0))
        self.text_type.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_67.addWidget(self.text_type)

        self.text = QLineEdit(self.textFrame)
        self.text.setObjectName(u"text")

        self.horizontalLayout_67.addWidget(self.text)


        self.verticalLayout.addWidget(self.textFrame)

        self.textfontFrame = QFrame(self.frame_7)
        self.textfontFrame.setObjectName(u"textfontFrame")
        sizePolicy4.setHeightForWidth(self.textfontFrame.sizePolicy().hasHeightForWidth())
        self.textfontFrame.setSizePolicy(sizePolicy4)
        self.textfontFrame.setFrameShape(QFrame.StyledPanel)
        self.textfontFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.textfontFrame)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.textfontFrame)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(50, 0))
        self.label_61.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_68.addWidget(self.label_61)

        self.textfont = QComboBox(self.textfontFrame)
        self.textfont.setObjectName(u"textfont")
        sizePolicy5.setHeightForWidth(self.textfont.sizePolicy().hasHeightForWidth())
        self.textfont.setSizePolicy(sizePolicy5)

        self.horizontalLayout_68.addWidget(self.textfont)


        self.verticalLayout.addWidget(self.textfontFrame)

        self.textscaleFrame = QFrame(self.frame_7)
        self.textscaleFrame.setObjectName(u"textscaleFrame")
        sizePolicy4.setHeightForWidth(self.textscaleFrame.sizePolicy().hasHeightForWidth())
        self.textscaleFrame.setSizePolicy(sizePolicy4)
        self.textscaleFrame.setFrameShape(QFrame.StyledPanel)
        self.textscaleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.textscaleFrame)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.textscaleFrame)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(50, 0))
        self.label_62.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_69.addWidget(self.label_62)

        self.textscale = QLineEdit(self.textscaleFrame)
        self.textscale.setObjectName(u"textscale")

        self.horizontalLayout_69.addWidget(self.textscale)


        self.verticalLayout.addWidget(self.textscaleFrame)

        self.textstyleFrame = QFrame(self.frame_7)
        self.textstyleFrame.setObjectName(u"textstyleFrame")
        sizePolicy4.setHeightForWidth(self.textstyleFrame.sizePolicy().hasHeightForWidth())
        self.textstyleFrame.setSizePolicy(sizePolicy4)
        self.textstyleFrame.setFrameShape(QFrame.StyledPanel)
        self.textstyleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.textstyleFrame)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.textstyleFrame)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(50, 0))
        self.label_63.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_70.addWidget(self.label_63)

        self.textstyle = QComboBox(self.textstyleFrame)
        self.textstyle.setObjectName(u"textstyle")
        sizePolicy5.setHeightForWidth(self.textstyle.sizePolicy().hasHeightForWidth())
        self.textstyle.setSizePolicy(sizePolicy5)

        self.horizontalLayout_70.addWidget(self.textstyle)


        self.verticalLayout.addWidget(self.textstyleFrame)

        self.textalignFrame = QFrame(self.frame_7)
        self.textalignFrame.setObjectName(u"textalignFrame")
        sizePolicy4.setHeightForWidth(self.textalignFrame.sizePolicy().hasHeightForWidth())
        self.textalignFrame.setSizePolicy(sizePolicy4)
        self.textalignFrame.setFrameShape(QFrame.StyledPanel)
        self.textalignFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.textalignFrame)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.textalignFrame)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(50, 0))
        self.label_64.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_71.addWidget(self.label_64)

        self.textalign = QComboBox(self.textalignFrame)
        self.textalign.setObjectName(u"textalign")
        sizePolicy5.setHeightForWidth(self.textalign.sizePolicy().hasHeightForWidth())
        self.textalign.setSizePolicy(sizePolicy5)

        self.horizontalLayout_71.addWidget(self.textalign)


        self.verticalLayout.addWidget(self.textalignFrame)

        self.visibleFrame = QFrame(self.frame_7)
        self.visibleFrame.setObjectName(u"visibleFrame")
        sizePolicy4.setHeightForWidth(self.visibleFrame.sizePolicy().hasHeightForWidth())
        self.visibleFrame.setSizePolicy(sizePolicy4)
        self.visibleFrame.setFrameShape(QFrame.StyledPanel)
        self.visibleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.visibleFrame)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.visibleFrame)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(50, 0))
        self.label_65.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_72.addWidget(self.label_65)

        self.visible = QLineEdit(self.visibleFrame)
        self.visible.setObjectName(u"visible")

        self.horizontalLayout_72.addWidget(self.visible)


        self.verticalLayout.addWidget(self.visibleFrame)

        self.actionFrame = QFrame(self.frame_7)
        self.actionFrame.setObjectName(u"actionFrame")
        self.actionFrame.setFrameShape(QFrame.StyledPanel)
        self.actionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.actionFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.actionFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.action = QLineEdit(self.actionFrame)
        self.action.setObjectName(u"action")

        self.horizontalLayout.addWidget(self.action)


        self.verticalLayout.addWidget(self.actionFrame)

        self.mouseEnterFrame = QFrame(self.frame_7)
        self.mouseEnterFrame.setObjectName(u"mouseEnterFrame")
        self.mouseEnterFrame.setFrameShape(QFrame.StyledPanel)
        self.mouseEnterFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mouseEnterFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.mouseEnterFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.mouseEnter = QLineEdit(self.mouseEnterFrame)
        self.mouseEnter.setObjectName(u"mouseEnter")

        self.horizontalLayout_2.addWidget(self.mouseEnter)


        self.verticalLayout.addWidget(self.mouseEnterFrame)

        self.mouseExitFrame = QFrame(self.frame_7)
        self.mouseExitFrame.setObjectName(u"mouseExitFrame")
        self.mouseExitFrame.setFrameShape(QFrame.StyledPanel)
        self.mouseExitFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.mouseExitFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.mouseExitFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.mouseExit = QLineEdit(self.mouseExitFrame)
        self.mouseExit.setObjectName(u"mouseExit")

        self.horizontalLayout_3.addWidget(self.mouseExit)


        self.verticalLayout.addWidget(self.mouseExitFrame)

        self.decorationFrame = QFrame(self.frame_7)
        self.decorationFrame.setObjectName(u"decorationFrame")
        sizePolicy4.setHeightForWidth(self.decorationFrame.sizePolicy().hasHeightForWidth())
        self.decorationFrame.setSizePolicy(sizePolicy4)
        self.decorationFrame.setFrameShape(QFrame.StyledPanel)
        self.decorationFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.decorationFrame)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.decorationFrame)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(70, 0))
        self.label_66.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_73.addWidget(self.label_66)

        self.decoration = QCheckBox(self.decorationFrame)
        self.decoration.setObjectName(u"decoration")
        sizePolicy5.setHeightForWidth(self.decoration.sizePolicy().hasHeightForWidth())
        self.decoration.setSizePolicy(sizePolicy5)
        self.decoration.setFocusPolicy(Qt.NoFocus)
        self.decoration.setChecked(True)

        self.horizontalLayout_73.addWidget(self.decoration)


        self.verticalLayout.addWidget(self.decorationFrame)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Scene", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"H", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"H", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"H Align", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"V Align", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"type", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"style", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"forecolor", None))
        self.material_selector_btn.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"textfont", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"textscale", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"textstyle", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"textalign", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"visible", None))
        self.label.setText(QCoreApplication.translate("Form", u"action", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"mouseEnter", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"mouseExit", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"decoration", None))
        self.decoration.setText(QCoreApplication.translate("Form", u"apply?", None))
    # retranslateUi

