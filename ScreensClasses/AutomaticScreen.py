import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette

from Screens_py.VcDvtTestTools_screen_automatic_mode import Ui_Automatic
from ScreensClasses.ScreenIndex import *
#from ScreensClasses.ManualScreen import ManualScreen
#from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5.QtCore import QMutex



TS_COLOR_PASSED = 'background-color: #9df793'
TS_COLOR_NOTPASSED = 'background-color: #fe9393'
TS_COLOR_INIT = 'background-color: self.color'



class AutomaticScreen(QtWidgets.QMainWindow, Ui_Automatic):
    def __init__(self, w, parent=None):
        super(AutomaticScreen, self).__init__(parent)
        self.setupUi(self)
        self.widget = w
        #self.widget.setWindowTitle("VcDvtTestTools | Automatic Mode")

        self.btn_ManualAutomatic.clicked.connect(self.setManualScreen)
        self.btn_SettingsAutomatic.clicked.connect(self.setSettingsScreen)
        self.btn_AutomaticStart.clicked.connect(self.btnStartClicked)
        self.btn_AutomaticStop.clicked.connect(self.btnStopClicked)
        self.btn_CleanAutomatic.clicked.connect(self.btn_CleanClicked)


    def setManualScreen(self):
        #self.progressBar_start.setValue(0)
        self.btn_CleanClicked()
        self.widget.setCurrentIndex(MANUAL_SCREEN_INDEX)


    def setSettingsScreen(self):
        #self.progressBar_start.setValue(0)
        self.btn_CleanClicked()
        self.widget.setCurrentIndex(SETTINGS_SCREEN_INDEX)

    def btnStartClicked(self):
        self.checkBox_MainMotor.setStyleSheet(TS_COLOR_INIT)

    def btnStopClicked(self):
        self.checkBox_MainMotor.setStyleSheet(TS_COLOR_INIT)


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
        self.checkBox_SwitchUnlockTopRight.setChecked(0)
        self.checkBox_SwitchPresentChamberLeft.setChecked(0)
        self.checkBox_SwitchPresentChamberRight.setChecked(0)
        self.checkBox_SwitchPresentTank.setChecked(0)
        self.checkBox_SwitchOpenLid.setChecked(0)
        self.checkBox_SwitchRemovedTop.setChecked(0)





















