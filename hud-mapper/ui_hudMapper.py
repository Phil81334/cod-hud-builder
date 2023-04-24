# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hudMapperXTDVYY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QDockWidget, QFrame, QGraphicsView, QHBoxLayout, QLabel,
                               QLineEdit, QListView, QPlainTextEdit, QPushButton, QRadioButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QToolButton, QVBoxLayout, QWidget)

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1703, 743)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(206, 206, 206);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #191E21;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(1343, 743))
        self.graphicsView.setMaximumSize(QSize(1343, 743))
        self.graphicsView.setStyleSheet(u"background-color: rgb(64, 65, 72);")
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.elems = QDockWidget(MainWindow)
        self.elems.setObjectName(u"elems")
        self.elems.setMinimumSize(QSize(179, 100))
        self.elems.setMaximumSize(QSize(524287, 524287))
        self.elems.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.elems_c = QWidget()
        self.elems_c.setObjectName(u"elems_c")
        self.elems_c.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.elems_c)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.elems_list = QListView(self.elems_c)
        self.elems_list.setObjectName(u"elems_list")
        self.elems_list.setFocusPolicy(Qt.NoFocus)
        self.elems_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_5.addWidget(self.elems_list)

        self.elems.setWidget(self.elems_c)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.elems)
        self.misc = QDockWidget(MainWindow)
        self.misc.setObjectName(u"misc")
        self.misc_c = QWidget()
        self.misc_c.setObjectName(u"misc_c")
        self.verticalLayout = QVBoxLayout(self.misc_c)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.misc_scroll_area = QScrollArea(self.misc_c)
        self.misc_scroll_area.setObjectName(u"misc_scroll_area")
        self.misc_scroll_area.setFocusPolicy(Qt.NoFocus)
        self.misc_scroll_area.setWidgetResizable(True)
        self.misc_scroll_area_c = QWidget()
        self.misc_scroll_area_c.setObjectName(u"misc_scroll_area_c")
        self.misc_scroll_area_c.setGeometry(QRect(0, 0, 212, 701))
        self.verticalLayout_7 = QVBoxLayout(self.misc_scroll_area_c)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.misc_scroll_area_c)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"text-decoration: underline;")

        self.verticalLayout_12.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.grid = QCheckBox(self.frame_15)
        self.grid.setObjectName(u"grid")
        self.grid.setFocusPolicy(Qt.NoFocus)
        self.grid.setChecked(True)

        self.verticalLayout_13.addWidget(self.grid, 0, Qt.AlignHCenter)

        self.background = QCheckBox(self.frame_15)
        self.background.setObjectName(u"background")
        self.background.setFocusPolicy(Qt.NoFocus)
        self.background.setChecked(False)

        self.verticalLayout_13.addWidget(self.background, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame_15)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.background_image_btn = QToolButton(self.frame_7)
        self.background_image_btn.setObjectName(u"background_image_btn")
        self.background_image_btn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.background_image_btn)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignHCenter)

        self.quadrant_label = QCheckBox(self.frame_15)
        self.quadrant_label.setObjectName(u"quadrant_label")
        sizePolicy1.setHeightForWidth(self.quadrant_label.sizePolicy().hasHeightForWidth())
        self.quadrant_label.setSizePolicy(sizePolicy1)
        self.quadrant_label.setFocusPolicy(Qt.NoFocus)
        self.quadrant_label.setChecked(False)

        self.verticalLayout_13.addWidget(self.quadrant_label, 0, Qt.AlignHCenter)

        self.quadrant_grid = QCheckBox(self.frame_15)
        self.quadrant_grid.setObjectName(u"quadrant_grid")
        self.quadrant_grid.setFocusPolicy(Qt.NoFocus)
        self.quadrant_grid.setChecked(True)

        self.verticalLayout_13.addWidget(self.quadrant_grid, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_15)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.snap_to_grid_enabled = QCheckBox(self.frame)
        self.snap_to_grid_enabled.setObjectName(u"snap_to_grid_enabled")
        self.snap_to_grid_enabled.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.snap_to_grid_enabled)

        self.snap_to_grid_size = QLineEdit(self.frame)
        self.snap_to_grid_size.setObjectName(u"snap_to_grid_size")
        self.snap_to_grid_size.setMaximumSize(QSize(50, 16777215))
        self.snap_to_grid_size.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.snap_to_grid_size)

        self.snap_to_grid_label = QLabel(self.frame)
        self.snap_to_grid_label.setObjectName(u"snap_to_grid_label")

        self.horizontalLayout_3.addWidget(self.snap_to_grid_label)


        self.verticalLayout_13.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_15)

        self.clear_scene = QPushButton(self.frame_14)
        self.clear_scene.setObjectName(u"clear_scene")
        sizePolicy1.setHeightForWidth(self.clear_scene.sizePolicy().hasHeightForWidth())
        self.clear_scene.setSizePolicy(sizePolicy1)
        self.clear_scene.setMinimumSize(QSize(150, 0))
        self.clear_scene.setMaximumSize(QSize(250, 16777215))
        self.clear_scene.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(rf"{os.getcwd()}\icons\trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_scene.setIcon(icon)

        self.verticalLayout_12.addWidget(self.clear_scene, 0, Qt.AlignHCenter)

        self.open_file = QPushButton(self.frame_14)
        self.open_file.setObjectName(u"open_file")
        sizePolicy1.setHeightForWidth(self.open_file.sizePolicy().hasHeightForWidth())
        self.open_file.setSizePolicy(sizePolicy1)
        self.open_file.setMinimumSize(QSize(150, 0))
        self.open_file.setMaximumSize(QSize(250, 16777215))
        self.open_file.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(rf"{os.getcwd()}\icons\file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_file.setIcon(icon1)

        self.verticalLayout_12.addWidget(self.open_file, 0, Qt.AlignHCenter)

        self.save_file = QPushButton(self.frame_14)
        self.save_file.setObjectName(u"save_file")
        sizePolicy1.setHeightForWidth(self.save_file.sizePolicy().hasHeightForWidth())
        self.save_file.setSizePolicy(sizePolicy1)
        self.save_file.setMinimumSize(QSize(150, 0))
        self.save_file.setMaximumSize(QSize(250, 16777215))
        self.save_file.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(rf"{os.getcwd()}\icons\save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_file.setIcon(icon2)

        self.verticalLayout_12.addWidget(self.save_file, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.line = QFrame(self.misc_scroll_area_c)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.misc_scroll_area_c)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"text-decoration: underline;")

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.elem_label = QCheckBox(self.frame_3)
        self.elem_label.setObjectName(u"elem_label")
        self.elem_label.setFocusPolicy(Qt.NoFocus)
        self.elem_label.setChecked(True)

        self.verticalLayout_6.addWidget(self.elem_label, 0, Qt.AlignHCenter)

        self.x_pos_indicator = QCheckBox(self.frame_3)
        self.x_pos_indicator.setObjectName(u"x_pos_indicator")
        sizePolicy1.setHeightForWidth(self.x_pos_indicator.sizePolicy().hasHeightForWidth())
        self.x_pos_indicator.setSizePolicy(sizePolicy1)
        self.x_pos_indicator.setFocusPolicy(Qt.NoFocus)
        self.x_pos_indicator.setChecked(True)

        self.verticalLayout_6.addWidget(self.x_pos_indicator, 0, Qt.AlignHCenter)

        self.quadrant_indicator = QCheckBox(self.frame_3)
        self.quadrant_indicator.setObjectName(u"quadrant_indicator")
        sizePolicy1.setHeightForWidth(self.quadrant_indicator.sizePolicy().hasHeightForWidth())
        self.quadrant_indicator.setSizePolicy(sizePolicy1)
        self.quadrant_indicator.setFocusPolicy(Qt.NoFocus)
        self.quadrant_indicator.setChecked(True)

        self.verticalLayout_6.addWidget(self.quadrant_indicator, 0, Qt.AlignHCenter)

        self.fill_background = QCheckBox(self.frame_3)
        self.fill_background.setObjectName(u"fill_background")
        self.fill_background.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_6.addWidget(self.fill_background, 0, Qt.AlignHCenter)

        self.manipulator_handle = QCheckBox(self.frame_3)
        self.manipulator_handle.setObjectName(u"manipulator_handle")
        self.manipulator_handle.setFocusPolicy(Qt.NoFocus)
        self.manipulator_handle.setChecked(False)

        self.verticalLayout_6.addWidget(self.manipulator_handle, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.copy_elem_start_pos = QRadioButton(self.frame_5)
        self.copy_elem_start_pos.setObjectName(u"copy_elem_start_pos")
        self.copy_elem_start_pos.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.copy_elem_start_pos)

        self.copy_elem_current_pos = QRadioButton(self.frame_5)
        self.copy_elem_current_pos.setObjectName(u"copy_elem_current_pos")
        self.copy_elem_current_pos.setFocusPolicy(Qt.NoFocus)
        self.copy_elem_current_pos.setChecked(True)

        self.horizontalLayout_8.addWidget(self.copy_elem_current_pos)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.inside_padding_area = QRadioButton(self.frame_4)
        self.inside_padding_area.setObjectName(u"inside_padding_area")
        self.inside_padding_area.setFocusPolicy(Qt.NoFocus)
        self.inside_padding_area.setChecked(False)

        self.horizontalLayout_7.addWidget(self.inside_padding_area)

        self.outside_padding_area = QRadioButton(self.frame_4)
        self.outside_padding_area.setObjectName(u"outside_padding_area")
        self.outside_padding_area.setFocusPolicy(Qt.NoFocus)
        self.outside_padding_area.setChecked(True)

        self.horizontalLayout_7.addWidget(self.outside_padding_area)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.verticalSpacer_8 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.line_4 = QFrame(self.misc_scroll_area_c)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.frame_16 = QFrame(self.misc_scroll_area_c)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"text-decoration: underline;")

        self.verticalLayout_3.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setMaximumSize(QSize(16777215, 35))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)

        self.txt_ext = QRadioButton(self.frame_17)
        self.txt_ext.setObjectName(u"txt_ext")
        sizePolicy1.setHeightForWidth(self.txt_ext.sizePolicy().hasHeightForWidth())
        self.txt_ext.setSizePolicy(sizePolicy1)
        self.txt_ext.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.txt_ext)

        self.menu_ext = QRadioButton(self.frame_17)
        self.menu_ext.setObjectName(u"menu_ext")
        sizePolicy1.setHeightForWidth(self.menu_ext.sizePolicy().hasHeightForWidth())
        self.menu_ext.setSizePolicy(sizePolicy1)
        self.menu_ext.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_12.addWidget(self.menu_ext)

        self.inc_ext = QRadioButton(self.frame_17)
        self.inc_ext.setObjectName(u"inc_ext")
        sizePolicy1.setHeightForWidth(self.inc_ext.sizePolicy().hasHeightForWidth())
        self.inc_ext.setSizePolicy(sizePolicy1)
        self.inc_ext.setFocusPolicy(Qt.NoFocus)
        self.inc_ext.setChecked(True)

        self.horizontalLayout_12.addWidget(self.inc_ext)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMaximumSize(QSize(16777215, 35))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.code_output_console = QRadioButton(self.frame_18)
        self.code_output_console.setObjectName(u"code_output_console")
        sizePolicy1.setHeightForWidth(self.code_output_console.sizePolicy().hasHeightForWidth())
        self.code_output_console.setSizePolicy(sizePolicy1)
        self.code_output_console.setFocusPolicy(Qt.NoFocus)
        self.code_output_console.setChecked(True)

        self.horizontalLayout_13.addWidget(self.code_output_console)

        self.code_output_file = QRadioButton(self.frame_18)
        self.code_output_file.setObjectName(u"code_output_file")
        sizePolicy1.setHeightForWidth(self.code_output_file.sizePolicy().hasHeightForWidth())
        self.code_output_file.setSizePolicy(sizePolicy1)
        self.code_output_file.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.code_output_file)

        self.code_output_both = QRadioButton(self.frame_18)
        self.code_output_both.setObjectName(u"code_output_both")
        sizePolicy1.setHeightForWidth(self.code_output_both.sizePolicy().hasHeightForWidth())
        self.code_output_both.setSizePolicy(sizePolicy1)
        self.code_output_both.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.code_output_both)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.clear_console = QPushButton(self.frame_16)
        self.clear_console.setObjectName(u"clear_console")
        self.clear_console.setMinimumSize(QSize(150, 0))
        self.clear_console.setMaximumSize(QSize(250, 16777215))
        self.clear_console.setFocusPolicy(Qt.NoFocus)
        self.clear_console.setIcon(icon)

        self.verticalLayout_3.addWidget(self.clear_console, 0, Qt.AlignHCenter)

        self.generate_code = QPushButton(self.frame_16)
        self.generate_code.setObjectName(u"generate_code")
        sizePolicy1.setHeightForWidth(self.generate_code.sizePolicy().hasHeightForWidth())
        self.generate_code.setSizePolicy(sizePolicy1)
        self.generate_code.setMinimumSize(QSize(150, 0))
        self.generate_code.setMaximumSize(QSize(250, 16777215))
        self.generate_code.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(rf"{os.getcwd()}\icons\code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generate_code.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.generate_code, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.frame_16)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.frame_8 = QFrame(self.frame_16)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.help_btn = QToolButton(self.frame_8)
        self.help_btn.setObjectName(u"help_btn")

        self.horizontalLayout_6.addWidget(self.help_btn)


        self.verticalLayout_3.addWidget(self.frame_8, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.misc_scroll_area.setWidget(self.misc_scroll_area_c)

        self.verticalLayout.addWidget(self.misc_scroll_area)

        self.misc.setWidget(self.misc_c)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.misc)
        self.property_editor = QDockWidget(MainWindow)
        self.property_editor.setObjectName(u"property_editor")
        sizePolicy1.setHeightForWidth(self.property_editor.sizePolicy().hasHeightForWidth())
        self.property_editor.setSizePolicy(sizePolicy1)
        self.property_editor.setMaximumSize(QSize(524287, 524287))
        self.property_editor_c = QWidget()
        self.property_editor_c.setObjectName(u"property_editor_c")
        self.property_editor.setWidget(self.property_editor_c)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.property_editor)
        self.console = QDockWidget(MainWindow)
        self.console.setObjectName(u"console")
        sizePolicy1.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy1)
        self.console_c = QWidget()
        self.console_c.setObjectName(u"console_c")
        self.verticalLayout_4 = QVBoxLayout(self.console_c)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.console_text_area = QPlainTextEdit(self.console_c)
        self.console_text_area.setObjectName(u"console_text_area")
        self.console_text_area.setEnabled(True)
        self.console_text_area.setFocusPolicy(Qt.NoFocus)
        self.console_text_area.setStyleSheet(u"background-color: rgb(38, 39, 41);\n"
"color: rgb(255, 255, 255);")
        self.console_text_area.setUndoRedoEnabled(False)
        self.console_text_area.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.console_text_area.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.console_text_area)

        self.console.setWidget(self.console_c)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.console)
        self.object_inspector = QDockWidget(MainWindow)
        self.object_inspector.setObjectName(u"object_inspector")
        self.object_inspector_c = QWidget()
        self.object_inspector_c.setObjectName(u"object_inspector_c")
        self.horizontalLayout_4 = QHBoxLayout(self.object_inspector_c)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.object_inspector_list = QListView(self.object_inspector_c)
        self.object_inspector_list.setObjectName(u"object_inspector_list")
        self.object_inspector_list.setFocusPolicy(Qt.NoFocus)
        self.object_inspector_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout_4.addWidget(self.object_inspector_list)

        self.frame_6 = QFrame(self.object_inspector_c)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.move_elem_up_list = QPushButton(self.frame_6)
        self.move_elem_up_list.setObjectName(u"move_elem_up_list")
        self.move_elem_up_list.setMaximumSize(QSize(250, 16777215))
        self.move_elem_up_list.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(rf"{os.getcwd()}\icons\chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.move_elem_up_list.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.move_elem_up_list)

        self.move_elem_down_list = QPushButton(self.frame_6)
        self.move_elem_down_list.setObjectName(u"move_elem_down_list")
        self.move_elem_down_list.setMaximumSize(QSize(250, 16777215))
        self.move_elem_down_list.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile(rf"{os.getcwd()}\icons\chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.move_elem_down_list.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.move_elem_down_list)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.object_inspector.setWidget(self.object_inspector_c)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.object_inspector)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.elems.setWindowTitle(QCoreApplication.translate("MainWindow", u"Elem", None))
        self.misc.setWindowTitle(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Scene", None))
        self.grid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.background.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Background Image", None))
        self.background_image_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.quadrant_label.setText(QCoreApplication.translate("MainWindow", u"Quadrant Label", None))
        self.quadrant_grid.setText(QCoreApplication.translate("MainWindow", u"Quadrant Grid", None))
        self.snap_to_grid_enabled.setText(QCoreApplication.translate("MainWindow", u"Snap-To-Grid", None))
        self.snap_to_grid_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1-50", None))
        self.snap_to_grid_label.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.clear_scene.setText(QCoreApplication.translate("MainWindow", u"Clear Scene", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open Scene", None))
        self.save_file.setText(QCoreApplication.translate("MainWindow", u"Save Scene", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Elem", None))
        self.elem_label.setText(QCoreApplication.translate("MainWindow", u"Elem Label", None))
        self.x_pos_indicator.setText(QCoreApplication.translate("MainWindow", u"X Pos Indicator", None))
        self.quadrant_indicator.setText(QCoreApplication.translate("MainWindow", u"Quadrant Indicator", None))
        self.fill_background.setText(QCoreApplication.translate("MainWindow", u"Fill Background", None))
        self.manipulator_handle.setText(QCoreApplication.translate("MainWindow", u"Manipulator Handle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Copy Elem", None))
        self.copy_elem_start_pos.setText(QCoreApplication.translate("MainWindow", u"Start Pos", None))
        self.copy_elem_current_pos.setText(QCoreApplication.translate("MainWindow", u"Curr Pos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resize Area", None))
        self.inside_padding_area.setText(QCoreApplication.translate("MainWindow", u"Inside", None))
        self.outside_padding_area.setText(QCoreApplication.translate("MainWindow", u"Outside", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.txt_ext.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.menu_ext.setText(QCoreApplication.translate("MainWindow", u".menu", None))
        self.inc_ext.setText(QCoreApplication.translate("MainWindow", u".inc", None))
        self.code_output_console.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.code_output_file.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.code_output_both.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.clear_console.setText(QCoreApplication.translate("MainWindow", u"Clear Console", None))
        self.generate_code.setText(QCoreApplication.translate("MainWindow", u"Generate Code", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Tips", None))
        self.property_editor.setWindowTitle(QCoreApplication.translate("MainWindow", u"Property Editor", None))
        self.console.setWindowTitle(QCoreApplication.translate("MainWindow", u"Console", None))
        self.console_text_area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code will output here upon submission", None))
        self.object_inspector.setWindowTitle(QCoreApplication.translate("MainWindow", u"Object Inspector", None))
        self.move_elem_up_list.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.move_elem_down_list.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
    # retranslateUi

