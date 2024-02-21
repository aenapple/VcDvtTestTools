# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Screens\VcDvtTestTools_settings_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1280, 720)
        self.grBox_SettingsMode = QtWidgets.QGroupBox(Settings)
        self.grBox_SettingsMode.setEnabled(True)
        self.grBox_SettingsMode.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.grBox_SettingsMode.setFont(font)
        self.grBox_SettingsMode.setAutoFillBackground(True)
        self.grBox_SettingsMode.setFlat(True)
        self.grBox_SettingsMode.setObjectName("grBox_SettingsMode")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.grBox_SettingsMode)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 600, 160, 95))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_CleanSettings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_CleanSettings.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_CleanSettings.setFont(font)
        self.btn_CleanSettings.setObjectName("btn_CleanSettings")
        self.verticalLayout.addWidget(self.btn_CleanSettings)
        self.btn_ManualSettings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ManualSettings.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btn_ManualSettings.setFont(font)
        self.btn_ManualSettings.setObjectName("btn_ManualSettings")
        self.verticalLayout.addWidget(self.btn_ManualSettings)
        self.btn_AutomaticSettings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_AutomaticSettings.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btn_AutomaticSettings.setFont(font)
        self.btn_AutomaticSettings.setObjectName("btn_AutomaticSettings")
        self.verticalLayout.addWidget(self.btn_AutomaticSettings)
        self.groupBox = QtWidgets.QGroupBox(self.grBox_SettingsMode)
        self.groupBox.setGeometry(QtCore.QRect(190, 190, 411, 83))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.grBox_ComPort = QtWidgets.QGroupBox(self.groupBox)
        self.grBox_ComPort.setGeometry(QtCore.QRect(10, 10, 111, 62))
        self.grBox_ComPort.setObjectName("grBox_ComPort")
        self.lineEdit_ComPort = QtWidgets.QLineEdit(self.grBox_ComPort)
        self.lineEdit_ComPort.setGeometry(QtCore.QRect(3, 30, 101, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ComPort.setFont(font)
        self.lineEdit_ComPort.setObjectName("lineEdit_ComPort")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 10, 271, 62))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_ConnectSettings = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_ConnectSettings.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_ConnectSettings.setFont(font)
        self.btn_ConnectSettings.setObjectName("btn_ConnectSettings")
        self.verticalLayout_2.addWidget(self.btn_ConnectSettings)
        self.btn_DisconnectSettings = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_DisconnectSettings.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_DisconnectSettings.setFont(font)
        self.btn_DisconnectSettings.setObjectName("btn_DisconnectSettings")
        self.verticalLayout_2.addWidget(self.btn_DisconnectSettings)
        self.groupBox_2 = QtWidgets.QGroupBox(self.grBox_SettingsMode)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 300, 411, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_GetStateSettings = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_GetStateSettings.setEnabled(True)
        self.btn_GetStateSettings.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.btn_GetStateSettings.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_GetStateSettings.setFont(font)
        self.btn_GetStateSettings.setObjectName("btn_GetStateSettings")
        self.lineEdit_GetState = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_GetState.setGeometry(QtCore.QRect(10, 63, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lineEdit_GetState.setFont(font)
        self.lineEdit_GetState.setFrame(True)
        self.lineEdit_GetState.setObjectName("lineEdit_GetState")
        self.connectLabel = QtWidgets.QLabel(self.grBox_SettingsMode)
        self.connectLabel.setEnabled(False)
        self.connectLabel.setGeometry(QtCore.QRect(610, 170, 101, 111))
        self.connectLabel.setText("")
        self.connectLabel.setPixmap(QtGui.QPixmap("..\\Screens\\../connect_red.png"))
        self.connectLabel.setObjectName("connectLabel")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.grBox_SettingsMode.setTitle(_translate("Settings", "    Settings"))
        self.btn_CleanSettings.setText(_translate("Settings", "Clean"))
        self.btn_ManualSettings.setText(_translate("Settings", "Manual mode"))
        self.btn_AutomaticSettings.setText(_translate("Settings", "Automatic"))
        self.grBox_ComPort.setTitle(_translate("Settings", "Com Port"))
        self.lineEdit_ComPort.setText(_translate("Settings", "COM1"))
        self.btn_ConnectSettings.setText(_translate("Settings", "Connect"))
        self.btn_DisconnectSettings.setText(_translate("Settings", "Disconnect"))
        self.btn_GetStateSettings.setText(_translate("Settings", "Get State"))
