# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Base_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):      
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1452, 854)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/GL.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget { background-color: rgb(255, 255, 255); }\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(36)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(1, -1, -1, 8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Label_GL = QtWidgets.QLabel(self.frame)
        self.Label_GL.setMinimumSize(QtCore.QSize(50, 0))
        self.Label_GL.setStyleSheet("image: url(:/icons/icons/GL.png);")
        self.Label_GL.setText("")
        self.Label_GL.setScaledContents(False)
        self.Label_GL.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_GL.setObjectName("Label_GL")
        self.horizontalLayout_2.addWidget(self.Label_GL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title_Label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Jost SemiBold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_Label.setFont(font)
        self.Title_Label.setStyleSheet("font: 16pt;\n"                                     
"color: rgb(255, 255, 255);")
        self.Title_Label.setObjectName("Title_Label")
        self.horizontalLayout.addWidget(self.Title_Label)
        spacerItem = QtWidgets.QSpacerItem(1018, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.help_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)
        self.help_btn.setFont(font)
        self.help_btn.setToolTip("")
        self.help_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_btn.setIcon(icon1)
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        self.btn_order_Layout = QtWidgets.QHBoxLayout()
        self.btn_order_Layout.setContentsMargins(17, -1, 10, -1)
        self.btn_order_Layout.setObjectName("btn_order_Layout")
        self.order_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.order_label.setFont(font)
        self.order_label.setObjectName("order_label")
        self.btn_order_Layout.addWidget(self.order_label)
        spacerItem1 = QtWidgets.QSpacerItem(758, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_order_Layout.addItem(spacerItem1)
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.setSpacing(6)
        self.btnLayout.setObjectName("btnLayout")
        self.order_btn = QtWidgets.QPushButton(self.centralwidget)
        self.order_btn.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.order_btn.setFont(font)
        self.order_btn.setStyleSheet("QPushButton {\n"
"background-color: rgba(30, 255, 97,140);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(86, 86, 86);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(30, 255, 97,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(30, 255, 97,150);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.order_btn.setIcon(icon2)
        self.order_btn.setIconSize(QtCore.QSize(30, 30))
        self.order_btn.setObjectName("order_btn")
        self.btnLayout.addWidget(self.order_btn)
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setMinimumSize(QtCore.QSize(181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(86, 86, 86);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(206, 206, 206);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon3)
        self.edit_btn.setIconSize(QtCore.QSize(30, 30))
        self.edit_btn.setObjectName("edit_btn")
        self.btnLayout.addWidget(self.edit_btn)
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setMinimumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.del_btn.setFont(font)
        self.del_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(86, 86, 86);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(206, 206, 206);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon4)
        self.del_btn.setIconSize(QtCore.QSize(30, 30))
        self.del_btn.setObjectName("del_btn")
        self.btnLayout.addWidget(self.del_btn)
        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setMinimumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.export_btn.setFont(font)
        self.export_btn.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(86, 86, 86);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(206, 206, 206);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon5)
        self.export_btn.setIconSize(QtCore.QSize(30, 30))
        self.export_btn.setObjectName("export_btn")
        self.btnLayout.addWidget(self.export_btn)
        self.btn_order_Layout.addLayout(self.btnLayout)
        self.verticalLayout.addLayout(self.btn_order_Layout)
        self.verticalLayout_12.addLayout(self.verticalLayout)
        self.panel_table_layout = QtWidgets.QHBoxLayout()
        self.panel_table_layout.setContentsMargins(-1, -1, 0, 0)
        self.panel_table_layout.setSpacing(10)
        self.panel_table_layout.setObjectName("panel_table_layout")
        self.filter_panel_lLayout = QtWidgets.QVBoxLayout()
        self.filter_panel_lLayout.setContentsMargins(10, -1, -1, -1)
        self.filter_panel_lLayout.setSpacing(0)
        self.filter_panel_lLayout.setObjectName("filter_panel_lLayout")
        self.filter_line_Layout = QtWidgets.QVBoxLayout()
        self.filter_line_Layout.setObjectName("filter_line_Layout")
        self.filter_Layout = QtWidgets.QHBoxLayout()
        self.filter_Layout.setContentsMargins(10, -1, -1, -1)
        self.filter_Layout.setObjectName("filter_Layout")
        self.filter_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.filter_label.setFont(font)
        self.filter_label.setScaledContents(True)
        self.filter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_label.setObjectName("filter_label")
        self.filter_Layout.addWidget(self.filter_label)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filter_Layout.addItem(spacerItem2)
        self.filter_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.filter_icon_label.setMaximumSize(QtCore.QSize(25, 25))
        self.filter_icon_label.setText("")
        self.filter_icon_label.setPixmap(QtGui.QPixmap(":/icons/icons/filter.svg"))
        self.filter_icon_label.setScaledContents(True)
        self.filter_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_icon_label.setObjectName("filter_icon_label")
        self.filter_Layout.addWidget(self.filter_icon_label)
        self.filter_line_Layout.addLayout(self.filter_Layout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.filter_line_Layout.addWidget(self.line)
        self.filter_panel_lLayout.addLayout(self.filter_line_Layout)
        self.client_Layout = QtWidgets.QVBoxLayout()
        self.client_Layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.client_Layout.setContentsMargins(-1, 0, -1, 0)
        self.client_Layout.setSpacing(0)
        self.client_Layout.setObjectName("client_Layout")
        self.client_label = QtWidgets.QLabel(self.centralwidget)
        self.client_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.client_label.setFont(font)
        self.client_label.setStyleSheet("")
        self.client_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.client_label.setIndent(-1)
        self.client_label.setObjectName("client_label")
        self.client_Layout.addWidget(self.client_label)
        self.client_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.client_lineEdit.setMinimumSize(QtCore.QSize(271, 31))
        self.client_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.client_lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rgb(180, 180, 180)")
        self.client_lineEdit.setInputMask("")
        self.client_lineEdit.setText("")
        self.client_lineEdit.setFrame(True)
        self.client_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.client_lineEdit.setPlaceholderText("")
        self.client_lineEdit.setObjectName("client_lineEdit")
        self.client_Layout.addWidget(self.client_lineEdit)
        self.filter_panel_lLayout.addLayout(self.client_Layout)
        self.device_Layout = QtWidgets.QVBoxLayout()
        self.device_Layout.setContentsMargins(-1, 0, -1, -1)
        self.device_Layout.setSpacing(0)
        self.device_Layout.setObjectName("device_Layout")
        self.device_label = QtWidgets.QLabel(self.centralwidget)
        self.device_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.device_label.setFont(font)
        self.device_label.setStyleSheet("")
        self.device_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.device_label.setObjectName("device_label")
        self.device_Layout.addWidget(self.device_label)
        self.device_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.device_lineEdit.setMinimumSize(QtCore.QSize(271, 31))
        self.device_lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200)")
        self.device_lineEdit.setInputMask("")
        self.device_lineEdit.setText("")
        self.device_lineEdit.setFrame(True)
        self.device_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.device_lineEdit.setPlaceholderText("")
        self.device_lineEdit.setObjectName("device_lineEdit")
        self.device_Layout.addWidget(self.device_lineEdit)
        self.filter_panel_lLayout.addLayout(self.device_Layout)
        self.service_Layout = QtWidgets.QVBoxLayout()
        self.service_Layout.setContentsMargins(-1, 0, -1, -1)
        self.service_Layout.setSpacing(0)
        self.service_Layout.setObjectName("service_Layout")
        self.service_label = QtWidgets.QLabel(self.centralwidget)
        self.service_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.service_label.setFont(font)
        self.service_label.setStyleSheet("")
        self.service_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.service_label.setObjectName("service_label")
        self.service_Layout.addWidget(self.service_label)
        self.service_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.service_lineEdit.setMinimumSize(QtCore.QSize(271, 31))
        self.service_lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200)")
        self.service_lineEdit.setInputMask("")
        self.service_lineEdit.setText("")
        self.service_lineEdit.setFrame(True)
        self.service_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.service_lineEdit.setPlaceholderText("")
        self.service_lineEdit.setObjectName("service_lineEdit")
        self.service_Layout.addWidget(self.service_lineEdit)
        self.filter_panel_lLayout.addLayout(self.service_Layout)
        self.price_Layout = QtWidgets.QVBoxLayout()
        self.price_Layout.setContentsMargins(-1, 0, -1, -1)
        self.price_Layout.setSpacing(0)
        self.price_Layout.setObjectName("price_Layout")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("")
        self.price_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.price_label.setObjectName("price_label")
        self.price_Layout.addWidget(self.price_label)
        self.price_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.price_lineEdit.setValidator(QtGui.QIntValidator())
        self.price_lineEdit.setMinimumSize(QtCore.QSize(271, 31))
        self.price_lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200)")
        self.price_lineEdit.setInputMask("")
        self.price_lineEdit.setText("")
        self.price_lineEdit.setFrame(True)
        self.price_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.price_lineEdit.setPlaceholderText("")
        self.price_lineEdit.setObjectName("price_lineEdit")
        self.price_Layout.addWidget(self.price_lineEdit)
        self.filter_panel_lLayout.addLayout(self.price_Layout)
        self.status_lLayout = QtWidgets.QVBoxLayout()
        self.status_lLayout.setContentsMargins(-1, 0, -1, -1)
        self.status_lLayout.setSpacing(0)
        self.status_lLayout.setObjectName("status_lLayout")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("")
        self.status_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.status_label.setObjectName("status_label")
        self.status_lLayout.addWidget(self.status_label)
        self.status_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.status_comboBox.setMinimumSize(QtCore.QSize(0, 31))
        self.status_comboBox.setStyleSheet("QComboBox {\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox::drop-down {\n"
"border: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/icons/icons/down-arrow.png);\n"
"width: 15px;\n"
"height: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QComboBox QListView {\n"
"border: 1px solid rgb(197, 197, 197);\n"
"outline: 0px;\n"
"}")
        self.status_comboBox.setEditable(False)
        self.status_comboBox.setCurrentText("")
        self.status_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.status_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.status_comboBox.setIconSize(QtCore.QSize(20, 20))
        self.status_comboBox.setDuplicatesEnabled(False)
        self.status_comboBox.setFrame(True)
        self.status_comboBox.setModelColumn(0)
        self.status_comboBox.setObjectName("status_comboBox")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_lLayout.addWidget(self.status_comboBox)
        self.filter_panel_lLayout.addLayout(self.status_lLayout)
        self.phonenumber_Layout = QtWidgets.QVBoxLayout()
        self.phonenumber_Layout.setContentsMargins(-1, 0, -1, -1)
        self.phonenumber_Layout.setSpacing(0)
        self.phonenumber_Layout.setObjectName("phonenumber_Layout")
        self.phonenumber_label = QtWidgets.QLabel(self.centralwidget)
        self.phonenumber_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.phonenumber_label.setFont(font)
        self.phonenumber_label.setStyleSheet("")
        self.phonenumber_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.phonenumber_label.setObjectName("phonenumber_label")
        self.phonenumber_Layout.addWidget(self.phonenumber_label)
        self.phonenumber_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phonenumber_lineEdit.setValidator(QtGui.QIntValidator())
        self.phonenumber_lineEdit.setMinimumSize(QtCore.QSize(271, 31))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.phonenumber_lineEdit.setFont(font)
        self.phonenumber_lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200)")
        self.phonenumber_lineEdit.setInputMask("")
        self.phonenumber_lineEdit.setText("")
        self.phonenumber_lineEdit.setFrame(True)
        self.phonenumber_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.phonenumber_lineEdit.setPlaceholderText("")
        self.phonenumber_lineEdit.setClearButtonEnabled(False)
        self.phonenumber_lineEdit.setObjectName("phonenumber_lineEdit")
        self.phonenumber_Layout.addWidget(self.phonenumber_lineEdit)
        self.filter_panel_lLayout.addLayout(self.phonenumber_Layout)
        self.master_Layout = QtWidgets.QVBoxLayout()
        self.master_Layout.setContentsMargins(-1, 0, -1, -1)
        self.master_Layout.setSpacing(0)
        self.master_Layout.setObjectName("master_Layout")
        self.master_label = QtWidgets.QLabel(self.centralwidget)
        self.master_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.master_label.setFont(font)
        self.master_label.setStyleSheet("")
        self.master_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.master_label.setObjectName("master_label")
        self.master_Layout.addWidget(self.master_label)
        self.master_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.master_comboBox.setMinimumSize(QtCore.QSize(0, 31))
        self.master_comboBox.setStyleSheet("QComboBox {\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(200, 200, 200);\n"
"}\n"
"QComboBox::drop-down {\n"
"border: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/icons/icons/down-arrow.png);\n"
"width: 15px;\n"
"height: 15px;\n"
"margin-right: 15px;\n"
"}\n"
"QComboBox QListView {\n"
"border: 1px solid rgb(197, 197, 197);\n"
"outline: 0px;\n"
"}")
        self.master_comboBox.setEditable(False)
        self.master_comboBox.setCurrentText("")
        self.master_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.master_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.master_comboBox.setIconSize(QtCore.QSize(20, 20))
        self.master_comboBox.setDuplicatesEnabled(False)
        self.master_comboBox.setFrame(True)
        self.master_comboBox.setModelColumn(0)
        self.master_comboBox.setObjectName("master_comboBox")
        self.master_comboBox.addItem("")
        self.master_comboBox.addItem("")
        self.master_Layout.addWidget(self.master_comboBox)
        self.filter_panel_lLayout.addLayout(self.master_Layout)
        self.button_Layout = QtWidgets.QHBoxLayout()
        self.button_Layout.setContentsMargins(10, 0, 10, -1)
        self.button_Layout.setSpacing(8)
        self.button_Layout.setObjectName("button_Layout")
        self.search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.search_Button.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.search_Button.setFont(font)
        self.search_Button.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"border: 2px solid rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(206, 206, 206);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        self.search_Button.setObjectName("search_Button")
        self.button_Layout.addWidget(self.search_Button)
        self.clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_Button.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Inter Medium")
        self.clear_Button.setFont(font)
        self.clear_Button.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 4px;\n"
"border: 2px solid rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(206, 206, 206);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        self.clear_Button.setObjectName("clear_Button")
        self.button_Layout.addWidget(self.clear_Button)
        self.filter_panel_lLayout.addLayout(self.button_Layout)
        self.panel_table_layout.addLayout(self.filter_panel_lLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableView.setStyleSheet("QTableView {\n"
"border: 1px solid rgb(200,200,200);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"height: 45px;\n"
"border-style:solid;\n"
"background-color: rgb(231, 231, 231);\n"
"border: 1px solid rgb(200,200,200);\n"
"font-size: 10pt;\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 1px solid rgb(223, 223, 223);\n"
"border-top: 1px solid rgb(223, 223, 223);\n"
"}\n"
"QTableView::item:selected {\n"
"background-color: rgba(255, 242, 142, 140);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView::down-arrow {;\n"
"width: 18px;\n"
"height:18px;\n"
"subcontrol-position: right;\n"
"image: url(:/icons/icons/down-arrow.png)\n"
"}\n"
"QHeaderView::up-arrow {;\n"
"width: 18px;\n"
"height:18px;\n"
"subcontrol-position: bottom right;\n"
"image: url(:/icons/icons/up-arrow.png);\n"
"}")
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView.setShowGrid(False)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setMinimumSectionSize(49)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setDefaultSectionSize(60)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setSortIndicatorShown(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.panel_table_layout.addWidget(self.tableView)
        self.panel_table_layout.setStretch(1, 6)
        self.verticalLayout_12.addLayout(self.panel_table_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.status_comboBox.setCurrentIndex(-1)
        self.master_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GrodnoLaptop"))
        self.Title_Label.setText(_translate("MainWindow", "GRODNOLAPTOP"))
        self.help_btn.setText(_translate("MainWindow", "  Справка"))
        self.order_label.setText(_translate("MainWindow", "Заказы"))
        self.order_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Добавить заказ</p></body></html>"))
        self.order_btn.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.order_btn.setText(_translate("MainWindow", "Заказ"))
        self.edit_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Редактировать заказ</p></body></html>"))
        self.edit_btn.setText(_translate("MainWindow", "Редактировать"))
        self.del_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Удалить заказ</p></body></html>"))
        self.del_btn.setText(_translate("MainWindow", "Удалить"))
        self.export_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Экспорт в формат .xls</p></body></html>"))
        self.export_btn.setText(_translate("MainWindow", "Экспорт"))
        self.filter_label.setText(_translate("MainWindow", "Фильтры"))
        self.client_label.setText(_translate("MainWindow", "Клиент"))
        self.client_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>ФИО клиента</p></body></html>"))
        self.device_label.setText(_translate("MainWindow", "Устройство"))
        self.device_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Тип и название устройства</p></body></html>"))
        self.service_label.setText(_translate("MainWindow", "Услуга"))
        self.service_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Предоставленные услуги</p></body></html>"))
        self.price_label.setText(_translate("MainWindow", "Стоимость"))
        self.price_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Стоимость работ</p></body></html>"))
        self.status_label.setText(_translate("MainWindow", "Статус"))
        self.status_comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Статус заказа</p></body></html>"))
        self.status_comboBox.setItemText(0, _translate("MainWindow", "Активен"))
        self.status_comboBox.setItemText(1, _translate("MainWindow", "Выполнен"))
        self.phonenumber_label.setText(_translate("MainWindow", "Номер телефона"))
        self.phonenumber_lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Номер телефона клиента</p></body></html>"))
        self.master_label.setText(_translate("MainWindow", "Мастер"))
        self.master_comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Имя мастера</p></body></html>"))
        self.master_comboBox.setItemText(0, _translate("MainWindow", "Константин"))
        self.master_comboBox.setItemText(1, _translate("MainWindow", "Михаил"))
        self.search_Button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Начать поиск</p></body></html>"))
        self.search_Button.setText(_translate("MainWindow", "Поиск"))
        self.clear_Button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Очистить фильтры</p></body></html>"))
        self.clear_Button.setText(_translate("MainWindow", "Очистить"))
import icons_res