from PyQt5 import QtWidgets

from ScreensClasses.ScreenIndex import AUTOMATIC_SCREEN_INDEX
from Screens_py.VcDvtTestTools_screen_manual_mode import Ui_Manual
from ScreensClasses.SettingsScreen import *
from Interfaces.InterfaceVIP import *

TS_COLOR_PASSED = 'background-color: #9df793'
TS_COLOR_NOTPASSED = 'background-color: #fe9393'
TS_COLOR_INIT = 'background-color: self.color'

class ManualScreen(QtWidgets.QMainWindow, Ui_Manual):
    def __init__(self, w, interface_vip, parent=None):
        super(ManualScreen, self).__init__(parent)
        self.setupUi(self)
        self.widget = w
        self.InterfaceVIP = interface_vip

        #self.widget.setWindowTitle("VcDvtTestTools | Manual Mode")
        self.btn_AutomaticManual.clicked.connect(self.AutomaticManual)
        self.btn_SettingsManual.clicked.connect(self.SettingsManual)
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

        self.btn_MainFan_ON.clicked.connect(self.MainFan_ON)
        self.btn_MainFanOff.clicked.connect(self.MainFan_Off)
        self.btn_TestMainFan.clicked.connect(self.TestMainFan)

        self.btn_GetState.clicked.connect(self.GetState)


    def AutomaticManual(self):
        self.widget.setCurrentIndex(AUTOMATIC_SCREEN_INDEX)

    def SettingsManual(self):
        self.widget.setCurrentIndex(SETTINGS_SCREEN_INDEX)

    def CleanManual(self):
        self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestDamMechanism_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestDamMechanism_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampBack_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampBack_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampFront_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampFront_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentTank.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_OpenLid.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_RemovedTop.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_UnlockTopLeft.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_UnlockTopRight.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestMainFan_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestMainFan_NotPassed.setStyleSheet(TS_COLOR_INIT)

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
        self.checkBox_TestMainFan_Passed.setChecked(0)
        self.checkBox_TestMainFan_NotPassed.setChecked(0)

    def MainMotor_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def MainMotor_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestMainMotor(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MAIN_MOTOR)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestMainMotor_Passed.setChecked(1)
            self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_PASSED)
            self.checkBox_TestMainMotor_NotPassed.setChecked(0)
            self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_INIT)
        else:
            self.checkBox_TestMainMotor_Passed.setChecked(0)
            self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_INIT)
            self.checkBox_TestMainMotor_NotPassed.setChecked(1)
            self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)


        """ result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_DAM_MOTOR)
        if result == 0:
            self.checkBox_TestMainMotor_Passed.setChecked(1)
            self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestMainMotor_NotPassed.setChecked(1)
            self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED) """


    def TestDamMechanism(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_DAM_MOTOR)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestDamMechanism_Passed.setChecked(1)
            self.checkBox_TestDamMechanism_Passed.setStyleSheet(TS_COLOR_PASSED)
            self.checkBox_TestDamMechanism_NotPassed.setChecked(0)
            self.checkBox_TestDamMechanism_NotPassed.setStyleSheet(TS_COLOR_INIT)
        else:
            self.checkBox_TestDamMechanism_Passed.setChecked(0)
            self.checkBox_TestDamMechanism_Passed.setStyleSheet(TS_COLOR_INIT)
            self.checkBox_TestDamMechanism_NotPassed.setChecked(1)
            self.checkBox_TestDamMechanism_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

        self.checkBox_TestDamMechanism_Passed.setChecked(0)
        self.checkBox_TestDamMechanism_NotPassed.setChecked(0)
        self.checkBox_TestDamMechanism_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestDamMechanism_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_DAM_MOTOR)
        if result == 0:
            self.checkBox_TestDamMechanism_Passed.setChecked(1)
            self.checkBox_TestDamMechanism_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestDamMechanism_NotPassed.setChecked(1)
            self.checkBox_TestDamMechanism_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def ChamberMotorLeft_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestChamberMotorLeft(self):
        self.checkBox_TestChamberMotorLeft_Passed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_CHAMBER_1)
        if result == 0:
            self.checkBox_TestChamberMotorLeft_Passed.setChecked(1)
            self.checkBox_TestChamberMotorLeft_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestChamberMotorLeft_NotPassed.setChecked(1)
            self.checkBox_TestChamberMotorLeft_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def ChamberMotorRight_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorRight_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestChamberMotorRight(self):
        self.checkBox_TestChamberMotorRight_Passed.setChecked(0)
        self.checkBox_TestChamberMotorRight_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorRight_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_CHAMBER_2)
        if result == 0:
            self.checkBox_TestChamberMotorRight_Passed.setChecked(1)
            self.checkBox_TestChamberMotorRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestChamberMotorRight_NotPassed.setChecked(1)
            self.checkBox_TestChamberMotorRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def On_PTCHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PTCHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPTCHeaterLeft(self):
        self.checkBox_TestPTCHeaterLeft_Passed.setChecked(0)
        self.checkBox_TestPTCHeaterLeft_NotPassed.setChecked(0)
        self.checkBox_TestPTCHeaterLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_1)
        if result == 0:
            self.checkBox_TestPTCHeaterLeft_Passed.setChecked(1)
            self.checkBox_TestPTCHeaterLeft_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPTCHeaterLeft_NotPassed.setChecked(1)
            self.checkBox_TestPTCHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def On_PTCHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PTCHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPTCHeaterRight(self):
        self.checkBox_TestPTCHeaterRight_Passed.setChecked(0)
        self.checkBox_TestPTCHeaterRight_NotPassed.setChecked(0)
        self.checkBox_TestPTCHeaterRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPTCHeaterRight_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_2)
        if result == 0:
            self.checkBox_TestPTCHeaterRight_Passed.setChecked(1)
            self.checkBox_TestPTCHeaterRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPTCHeaterRight_NotPassed.setChecked(1)
            self.checkBox_TestPTCHeaterRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def On_PadHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PadHeaterLeft(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPadHeaterLeft(self):
        self.checkBox_TestPadHeaterLeft_Passed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_1)
        if result == 0:
            self.checkBox_TestPadHeaterLeft_Passed.setChecked(1)
            self.checkBox_TestPadHeaterLeft_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPadHeaterLeft_NotPassed.setChecked(1)
            self.checkBox_TestPadHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def On_PadHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def Off_PadHeaterRight(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestPadHeaterRight(self):
        self.checkBox_TestPadHeaterRight_Passed.setChecked(0)
        self.checkBox_TestPadHeaterRight_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_2)
        if result == 0:
            self.checkBox_TestPadHeaterRight_Passed.setChecked(1)
            self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPadHeaterRight_NotPassed.setChecked(1)
            self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def LampBack_ON(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampBack_Off(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestLampBack(self):
        self.checkBox_TestLampBack_Passed.setChecked(0)
        self.checkBox_TestLampBack_NotPassed.setChecked(0)
        self.checkBox_TestLampBack_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampBack_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_1)
        if result == 0:
            self.checkBox_TestLampBack_Passed.setChecked(1)
            self.checkBox_TestLampBack_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestLampBack_NotPassed.setChecked(1)
            self.checkBox_TestLampBack_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def LampFront_ON(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def LampFront_Off(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestLampFront(self):
        self.checkBox_TestLampFront_Passed.setChecked(0)
        self.checkBox_TestLampFront_NotPassed.setChecked(0)
        self.checkBox_TestLampFront_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLampFront_NotPassed.setStyleSheet(TS_COLOR_INIT)

        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_2)
        if result == 0:
            self.checkBox_TestLampFront_Passed.setChecked(1)
            self.checkBox_TestLampFront_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestLampFront_NotPassed.setChecked(1)
            self.checkBox_TestLampFront_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def GetState(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def MainFan_ON(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def MainFan_Off(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def TestMainFan(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MAIN_FAN)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestMainFan_Passed.setChecked(1)
            self.checkBox_TestMainFan_Passed.setStyleSheet(TS_COLOR_PASSED)
            self.checkBox_TestMainFan_NotPassed.setChecked(0)
            self.checkBox_TestMainFan_NotPassed.setStyleSheet(TS_COLOR_INIT)
        else:
            self.checkBox_TestMainFan_Passed.setChecked(0)
            self.checkBox_TestMainFan_Passed.setStyleSheet(TS_COLOR_INIT)
            self.checkBox_TestMainFan_NotPassed.setChecked(1)
            self.checkBox_TestMainFan_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)






















