import time

from PyQt5 import QtGui, QtCore

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette

from Screens_py.VcDvtTestTools_screen_automatic_mode import Ui_Automatic
from ScreensClasses.ScreenIndex import *
#from ScreensClasses.ManualScreen import ManualScreen
#from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5.QtCore import QMutex

from ScreensClasses.SettingsScreen import *
from Interfaces.InterfaceVIP import *

TS_COLOR_PASSED = 'background-color: #9df793'
TS_COLOR_NOTPASSED = 'background-color: #fe9393'
TS_COLOR_INIT = 'background-color: self.color'



class AutomaticScreen(QtWidgets.QMainWindow, Ui_Automatic):
    def __init__(self, w, interface_vip, parent=None):
        super(AutomaticScreen, self).__init__(parent)
        self.setupUi(self)
        self.widget = w
        self.InterfaceVIP = interface_vip
        self.progressBarSteps = 0
        self.progressBar_start.close()

        #self.widget.setWindowTitle("VcDvtTestTools | Automatic Mode")

        self.btn_ManualAutomatic.clicked.connect(self.setManualScreen)
        self.btn_SettingsAutomatic.clicked.connect(self.setSettingsScreen)
        self.btn_AutomaticStart.clicked.connect(self.btnStartClicked)
        self.btn_AutomaticStop.clicked.connect(self.btnStopClicked)
        self.btn_CleanAutomatic.clicked.connect(self.btn_CleanClicked)


    def setManualScreen(self):
        # self.progressBar_start.setValue(0)
        self.btn_CleanClicked()
        self.widget.setCurrentIndex(MANUAL_SCREEN_INDEX)


    def setSettingsScreen(self):
        # self.progressBar_start.setValue(0)
        self.btn_CleanClicked()
        self.widget.setCurrentIndex(SETTINGS_SCREEN_INDEX)

    def progressBar(self):
        if self.progressBarSteps < 108:
            self.progressBarSteps += 8
            self.progressBar_start.setValue(self.progressBarSteps)
        else:
            self.progressBarSteps = 0
            self.progressBar_start.reset()

    def btnStartClicked(self):
        self.btn_CleanClicked()

        self.progressBar_start.setVisible(1)
        self.progressBarSteps = 0
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MAIN_MOTOR)
        if result == 0:
            self.checkBox_MainMotor.setChecked(1)
            self.checkBox_MainMotor.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_MainMotor.setChecked(0)
            self.checkBox_MainMotor.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_CHAMBER_1)
        if result == 0:
            self.checkBox_ChamberMotorLeft.setChecked(1)
            self.checkBox_ChamberMotorLeft.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_ChamberMotorLeft.setChecked(0)
            self.checkBox_ChamberMotorLeft.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_CHAMBER_2)
        if result == 0:
            self.checkBox_ChamberMotorRight.setChecked(1)
            self.checkBox_ChamberMotorRight.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_ChamberMotorRight.setChecked(0)
            self.checkBox_ChamberMotorRight.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_2)
        if result == 0:
            self.checkBox_LampFront.setChecked(1)
            self.checkBox_LampFront.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_LampFront.setChecked(0)
            self.checkBox_LampFront.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_1)
        if result == 0:
            self.checkBox_LampBack.setChecked(1)
            self.checkBox_LampBack.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_LampBack.setChecked(0)
            self.checkBox_LampBack.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_DAM_MOTOR)
        if result == 0:
            self.checkBox_DamMechanism.setChecked(1)
            self.checkBox_DamMechanism.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_DamMechanism.setChecked(0)
            self.checkBox_DamMechanism.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_1)
        if result == 0:
            self.checkBox_PTCHeaterLeft.setChecked(1)
            self.checkBox_PTCHeaterLeft.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_PTCHeaterLeft.setChecked(0)
            self.checkBox_PTCHeaterLeft.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_2)
        if result == 0:
            self.checkBox_PTCHeaterRight.setChecked(1)
            self.checkBox_PTCHeaterRight.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_PTCHeaterRight.setChecked(0)
            self.checkBox_PTCHeaterRight.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MAIN_FAN)
        if result == 0:
            self.checkBox_MainFan.setChecked(1)
            self.checkBox_MainFan.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_MainFan.setChecked(0)
            self.checkBox_MainFan.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_1)
        if result == 0:
            self.checkBox_PadHeaterLeft.setChecked(1)
            self.checkBox_PadHeaterLeft.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_PadHeaterLeft.setChecked(0)
            self.checkBox_PadHeaterLeft.setStyleSheet(TS_COLOR_NOTPASSED)
        self.progressBar()
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_2)
        if result == 0:
            self.checkBox_PadHeaterRight.setChecked(1)
            self.checkBox_PadHeaterRight.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_PadHeaterRight.setChecked(0)
            self.checkBox_PadHeaterRight.setStyleSheet(TS_COLOR_NOTPASSED)

        self.progressBar_start.close()

    def btnStopClicked(self):
        self.progressBar_start.close()


    def btn_CleanClicked(self):
        self.checkBox_MainMotor.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_ChamberMotorLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_ChamberMotorRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_LampFront.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_LampBack.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_DamMechanism.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PTCHeaterLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PTCHeaterRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_MainFan.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PadHeaterLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PadHeaterRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchUnlockTopLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchUnlockTopRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchPresentChamberLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchPresentChamberRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchPresentTank.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchOpenLid.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_SwitchRemovedTop.setStyleSheet(TS_COLOR_INIT)

        self.checkBox_MainMotor.setChecked(0)
        self.checkBox_ChamberMotorLeft.setChecked(0)
        self.checkBox_ChamberMotorRight.setChecked(0)
        self.checkBox_LampFront.setChecked(0)
        self.checkBox_LampBack.setChecked(0)
        self.checkBox_DamMechanism.setChecked(0)
        self.checkBox_PTCHeaterLeft.setChecked(0)
        self.checkBox_PTCHeaterRight.setChecked(0)
        self.checkBox_MainFan.setChecked(0)
        self.checkBox_PadHeaterLeft.setChecked(0)
        self.checkBox_PadHeaterRight.setChecked(0)
        self.checkBox_SwitchUnlockTopLeft.setChecked(0)
        self.checkBox_SwitchUnlockTopRight.setChecked(0)
        self.checkBox_SwitchPresentChamberLeft.setChecked(0)
        self.checkBox_SwitchPresentChamberRight.setChecked(0)
        self.checkBox_SwitchPresentTank.setChecked(0)
        self.checkBox_SwitchOpenLid.setChecked(0)
        self.checkBox_SwitchRemovedTop.setChecked(0)






















