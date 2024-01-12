from PyQt5 import QtWidgets

from ScreensClasses.ScreenIndex import AUTOMATIC_SCREEN_INDEX
from Screens_py.VcDvtTestTools_screen_manual_mode import Ui_Manual
from ScreensClasses.SettingsScreen import *
from PyQt5.QtGui import QIcon




class ManualScreen(QtWidgets.QMainWindow, Ui_Manual):
    def __init__(self, w, parent=None):
        super(ManualScreen, self).__init__(parent)
        self.setupUi(self)

        self.widget = w
        #self.widget.setWindowTitle("VcDvtTestTools | Manual Mode")
        self.btn_AutomaticManual.clicked.connect(self.AutomaticManual)
        self.btn_SettingsManual.clicked.connect(self.AutomaticManual)
        self.btn_CleanManual.clicked.connect(self.CleanManual)

        self.btn_MainMotor_Start.clicked.connect(self.MainMotor_Start)
        self.btn_MainMotor_Stop.clicked.connect(self.MainMotor_Stop)
        self.btn_TestMainMotor.clicked.connect(self.TestMainMotor)

        self.btn_TestDamMechanism.clicked.connect(self.TestDamMechanism)

        self.btn_ChamberMotorLeft_Start.clicked.connect(self.ChamberMotorLeft_Start)
        self.btn_ChamberMotorLeft_Stop.clicked.connect(self.ChamberMotorLeft_Stop)
        self.btn_TestChamberMotorLeft.clicked.connect(self.TestChamberMotorLeft)

        self.btn_ChamberMotorRight_Start.clicked.connect(self.ChamberMotorRight_Start)
        self.btn_ChamberMotorRight_Stop.clicked.connect(self.ChamberMotorRight_Stop)
        self.btn_TestChamberMotorRight.clicked.connect(self.TestChamberMotorRight)

        self.pushButton_on_PTCHeaterLeft.clicked.connect(self.On_PTCHeaterLeft)
        self.pushButton_off_PTCHeaterLeft.clicked.connect(self.Off_PTCHeaterLeft)
        self.btn_TestPTCHeaterLeft.clicked.connect(self.TestPTCHeaterLeft)

        self.pushButton_on_PTCHeaterRight.clicked.connect(self.On_PTCHeaterRight)
        self.pushButton_off_PTCHeaterRight.clicked.connect(self.Off_PTCHeaterRight)
        self.btn_TestPTCHeaterRight.clicked.connect(self.TestPTCHeaterRight)

        self.pushButton_on_PadHeaterLeft.clicked.connect(self.On_PadHeaterLeft)
        self.pushButton_off_PadHeaterLeft.clicked.connect(self.Off_PadHeaterLeft)
        self.btn_TestPadHeaterLeft.clicked.connect(self.TestPadHeaterLeft)

        self.pushButton_on_PadHeaterRight.clicked.connect(self.On_PadHeaterRight)
        self.pushButton_off_PadHeaterRight.clicked.connect(self.Off_PadHeaterRight)
        self.btn_TestPadHeaterRight.clicked.connect(self.TestPadHeaterRight)

        self.btn_LampBack_ON.clicked.connect(self.LampBack_ON)
        self.btn_LampBack_Off.clicked.connect(self.LampBack_Off)
        self.btn_TestLampBack.clicked.connect(self.TestLampBack)

        self.btn_LampFront_ON.clicked.connect(self.LampFront_ON)
        self.btn_LampFront_Off.clicked.connect(self.LampFront_Off)
        self.btn_TestLampFront.clicked.connect(self.TestLampFront)

        self.btn_GetState.clicked.connect(self.GetState)

    def AutomaticManual(self):
        self.widget.setCurrentIndex(AUTOMATIC_SCREEN_INDEX)

    def SettingsManual(self):
        self.widget.setCurrentIndex(SETTINGS_SCREEN_INDEX)

    def CleanManual(self):
        self.checkBox_TestMainMotor_Passed.setChecked(0)
        self.checkBox_TestMainMotor_NotPassed.setChecked(0)
        self.checkBox_TestDamMechanism_Passed.setChecked(0)
        self.checkBox_TestDamMechanism_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_Passed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorRight_Passed.setChecked(0)
        self.checkBox_TestChamberMotorRight_NotPassed.setChecked(0)
        self.checkBox_TestPTCHeaterLeft_Passed.setChecked(0)
        self.checkBox_TestPTCHeaterLeft_NotPassed.setChecked(0)
        self.checkBox_TestPTCHeaterRight_Passed.setChecked(0)
        self.checkBox_TestPTCHeaterRight_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_Passed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterRight_Passed.setChecked(0)
        self.checkBox_TestPadHeaterRight_NotPassed.setChecked(0)
        self.checkBox_TestLampBack_Passed.setChecked(0)
        self.checkBox_TestLampBack_NotPassed.setChecked(0)
        self.checkBox_TestLampFront_Passed.setChecked(0)
        self.checkBox_TestLampFront_NotPassed.setChecked(0)
        self.checkBox_PresentChamberLeft.setChecked(0)
        self.checkBox_PresentChamberRight.setChecked(0)
        self.checkBox_PresentTank.setChecked(0)
        self.checkBox_OpenLid.setChecked(0)
        self.checkBox_RemovedTop.setChecked(0)
        self.checkBox_UnlockTopLeft.setChecked(0)
        self.checkBox_UnlockTopRight.setChecked(0)

    def MainMotor_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def MainMotor_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestMainMotor(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestDamMechanism(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestChamberMotorLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorRight_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorRight_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestChamberMotorRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def On_PTCHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PTCHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPTCHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def On_PTCHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PTCHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPTCHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def On_PadHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PadHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPadHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def On_PadHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PadHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPadHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampBack_ON(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampBack_Off(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestLampBack(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampFront_ON(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampFront_Off(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestLampFront(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def GetState(self):
        self.checkBox_UnlockTopRight.setChecked(0)





















