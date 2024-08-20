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
        self.btn_MainMotor_Test.clicked.connect(self.MainMotor_Test)

        self.btn_AcMainPower_Test.clicked.connect(self.AcMainPower_Test)

        self.btn_ChamberMotorLeft_Start.clicked.connect(self.ChamberMotorLeft_Start)
        self.btn_ChamberMotorLeft_Stop.clicked.connect(self.ChamberMotorLeft_Stop)
        self.btn_ChamberMotorLeft_Test.clicked.connect(self.ChamberMotorLeft_Test)

        self.btn_ChamberMotorRight_Start.clicked.connect(self.ChamberMotorRight_Start)
        self.btn_ChamberMotorRight_Stop.clicked.connect(self.ChamberMotorRight_Stop)
        self.btn_ChamberMotorRight_Test.clicked.connect(self.ChamberMotorRight_Test)

        self.btn_PtcHeaterIntake_On.clicked.connect(self.PtcHeaterIntake_On)
        self.btn_PtcHeaterIntake_Off.clicked.connect(self.PtcHeaterIntake_Off)
        self.btn_PtcHeaterIntake_Test.clicked.connect(self.PtcHeaterIntake_Test)

        self.btn_PtcHeaterInternal_On.clicked.connect(self.PtcHeaterInternal_On)
        self.btn_PtcHeaterInternal_Off.clicked.connect(self.PtcHeaterInternal_Off)
        self.btn_PtcHeaterInternal_Test.clicked.connect(self.PtcHeaterInternal_Test)

        self.btn_PadHeaterLeft_On.clicked.connect(self.PadHeaterLeft_On)
        self.btn_PadHeaterLeft_Off.clicked.connect(self.PadHeaterLeft_Off)
        self.btn_PadHeaterLeft_Test.clicked.connect(self.PadHeaterLeft_Test)

        self.btn_PadHeaterRight_On.clicked.connect(self.PadHeaterRight_On)
        self.btn_PadHeaterRight_Off.clicked.connect(self.PadHeaterRight_Off)
        self.btn_PadHeaterRight_Test.clicked.connect(self.PadHeaterRight_Test)

        self.btn_Lamp_On.clicked.connect(self.Lamp_On)
        self.btn_Lamp_Off.clicked.connect(self.Lamp_Off)
        self.btn_Lamp_Test.clicked.connect(self.Lamp_Test)

        self.btn_IntakeFan_On.clicked.connect(self.IntakeFan_On)
        self.btn_IntakeFan_Off.clicked.connect(self.IntakeFan_Off)
        self.btn_IntakeFan_Test.clicked.connect(self.IntakeFan_Test)

        self.btn_GetState.clicked.connect(self.GetState)


    def AutomaticManual(self):
        self.widget.setCurrentIndex(AUTOMATIC_SCREEN_INDEX)

    def SettingsManual(self):
        self.widget.setCurrentIndex(SETTINGS_SCREEN_INDEX)

    def CleanManual(self):
        self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestAcMainPower_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestAcMainPower_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestChamberMotorRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPtcHeaterIntake_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPtcHeaterIntake_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPtcHeaterInternal_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPtcHeaterInternal_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLamp_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestLamp_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberLeft_Yes.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberLeft_No.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberRight_Yes.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_PresentChamberRight_No.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_BackLidOpen_Yes.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_BackLidOpen_No.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_FrontLidOpen_Yes.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_FrontLidOpen_No.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TopLocked_Yes.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TopLocked_No.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestIntakeFan_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestIntakeFan_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBlower_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBlower_NotPassed.setStyleSheet(TS_COLOR_INIT)

        self.checkBox_TestMainMotor_Passed.setChecked(0)
        self.checkBox_TestMainMotor_NotPassed.setChecked(0)
        self.checkBox_TestAcMainPower_Passed.setChecked(0)
        self.checkBox_TestAcMainPower_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_Passed.setChecked(0)
        self.checkBox_TestChamberMotorLeft_NotPassed.setChecked(0)
        self.checkBox_TestChamberMotorRight_Passed.setChecked(0)
        self.checkBox_TestChamberMotorRight_NotPassed.setChecked(0)
        self.checkBox_TestPtcHeaterIntake_Passed.setChecked(0)
        self.checkBox_TestPtcHeaterIntake_NotPassed.setChecked(0)
        self.checkBox_TestPtcHeaterIntake_Passed.setChecked(0)
        self.checkBox_TestPtcHeaterInternal_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_Passed.setChecked(0)
        self.checkBox_TestPadHeaterLeft_NotPassed.setChecked(0)
        self.checkBox_TestPadHeaterRight_Passed.setChecked(0)
        self.checkBox_TestPadHeaterRight_NotPassed.setChecked(0)
        self.checkBox_TestLamp_Passed.setChecked(0)
        self.checkBox_TestLamp_NotPassed.setChecked(0)
        self.checkBox_PresentChamberLeft_Yes.setChecked(0)
        self.checkBox_PresentChamberLeft_No.setChecked(0)
        self.checkBox_PresentChamberRight_Yes.setChecked(0)
        self.checkBox_PresentChamberRight_No.setChecked(0)
        self.checkBox_BackLidOpen_Yes.setChecked(0)
        self.checkBox_BackLidOpen_No.setChecked(0)
        self.checkBox_FrontLidOpen_Yes.setChecked(0)
        self.checkBox_FrontLidOpen_No.setChecked(0)
        self.checkBox_TopLocked_Yes.setChecked(0)
        self.checkBox_TopLocked_No.setChecked(0)
        self.checkBox_TestIntakeFan_Passed.setChecked(0)
        self.checkBox_TestIntakeFan_NotPassed.setChecked(0)
        self.checkBox_TestBlower_Passed.setChecked(0)
        self.checkBox_TestBlower_NotPassed.setChecked(0)

    def MainMotor_Start(self):
        pass

    def MainMotor_Stop(self):
        pass

    def MainMotor_Test(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MAIN_MOTOR)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestMainMotor_Passed.setChecked(1)
            self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_PASSED)
            # self.checkBox_TestMainMotor_NotPassed.setChecked(0)
            # self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_INIT)
        else:
            # self.checkBox_TestMainMotor_Passed.setChecked(0)
            # self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_INIT)
            self.checkBox_TestMainMotor_NotPassed.setChecked(1)
            self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def AcMainPower_Test(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_AC_POWER)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestAcMainPower_Passed.setChecked(1)
            self.checkBox_TestAcMainPower_Passed.setStyleSheet(TS_COLOR_PASSED)
            # self.checkBox_TestAcMainPower_NotPassed.setChecked(0)
            # self.checkBox_TestAcMainPower_NotPassed.setStyleSheet(TS_COLOR_INIT)
        else:
            # self.checkBox_TestAcMainPower_Passed.setChecked(0)
            # self.checkBox_TestAcMainPower_Passed.setStyleSheet(TS_COLOR_INIT)
            self.checkBox_TestAcMainPower_NotPassed.setChecked(1)
            self.checkBox_TestAcMainPower_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def ChamberMotorLeft_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Test(self):
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

    def ChamberMotorRight_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_CHAMBER_2)
        if result == 0:
            self.checkBox_TestChamberMotorRight_Passed.setChecked(1)
            self.checkBox_TestChamberMotorRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestChamberMotorRight_NotPassed.setChecked(1)
            self.checkBox_TestChamberMotorRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def PtcHeaterIntake_On(self):
        pass

    def PtcHeaterIntake_Off(self):
        pass

    def PtcHeaterIntake_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_INTAKE)
        if result == 0:
            self.checkBox_TestPtcHeaterIntake_Passed.setChecked(1)
            self.checkBox_TestPtcHeaterIntake_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPtcHeaterIntake_NotPassed.setChecked(1)
            self.checkBox_TestPtcHeaterIntake_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def PtcHeaterInternal_On(self):
        pass

    def PtcHeaterInternal_Off(self):
        pass

    def PtcHeaterInternal_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_INTERNAL)
        if result == 0:
            self.checkBox_TestPtcHeaterInternal_Passed.setChecked(1)
            self.checkBox_TestPtcHeaterInternal_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPtcHeaterInternal_NotPassed.setChecked(1)
            self.checkBox_TestPtcHeaterInternal_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def PadHeaterLeft_On(self):
        pass

    def PadHeaterLeft_Off(self):
        pass

    def PadHeaterLeft_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_1)
        if result == 0:
            self.checkBox_TestPadHeaterLeft_Passed.setChecked(1)
            self.checkBox_TestPadHeaterLeft_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPadHeaterLeft_NotPassed.setChecked(1)
            self.checkBox_TestPadHeaterLeft_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def PadHeaterRight_On(self):
        pass

    def PadHeaterRight_Off(self):
        pass

    def PadHeaterRight_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PAD_HEATER_2)
        if result == 0:
            self.checkBox_TestPadHeaterRight_Passed.setChecked(1)
            self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPadHeaterRight_NotPassed.setChecked(1)
            self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def Lamp_On(self):
        pass

    def Lamp_Off(self):
        pass

    def Lamp_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_OZONE)
        if result == 0:
            self.checkBox_TestLamp_Passed.setChecked(1)
            self.checkBox_TestLamp_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestLamp_NotPassed.setChecked(1)
            self.checkBox_TestLamp_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def GetState(self):
        result, read_data = self.InterfaceVIP.read_state()
        if result == 0:
            state_sensors = self.InterfaceVIP.get_sensor_state()

            if (state_sensors & IFC_VIP_STATE_SWITCHES_LOCK) > 0:
                self.checkBox_TopLocked_No.setChecked(1)
            else:
                self.checkBox_TopLocked_Yes.setChecked(1)

            if (state_sensors & IFC_VIP_STATE_SWITCH_FRONT_LID_OPEN) > 0:
                self.checkBox_FrontLidOpen_No.setChecked(1)
            else:
                self.checkBox_FrontLidOpen_Yes.setChecked(1)

            if (state_sensors & IFC_VIP_STATE_SWITCH_BACK_LID_OPEN) > 0:
                self.checkBox_BackLidOpen_No.setChecked(1)
            else:
                self.checkBox_BackLidOpen_Yes.setChecked(1)

            if (state_sensors & IFC_VIP_STATE_SWITCH_PRESENT_CH_LEFT) > 0:
                self.checkBox_PresentChamberLeft_No.setChecked(1)
            else:
                self.checkBox_PresentChamberLeft_Yes.setChecked(1)

            if (state_sensors & IFC_VIP_STATE_SWITCH_PRESENT_CH_RIGHT) > 0:
                self.checkBox_PresentChamberRight_No.setChecked(1)
            else:
                self.checkBox_PresentChamberRight_Yes.setChecked(1)



    def IntakeFan_On(self):
        pass

    def IntakeFan_Off(self):
        pass

    def IntakeFan_Test(self):
        test_result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_FAN_INTAKE)
        if test_result == IFC_VIP_TEST_RESULT_OK:
            self.checkBox_TestIntakeFan_Passed.setChecked(1)
            self.checkBox_TestIntakeFan_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestIntakeFan_NotPassed.setChecked(1)
            self.checkBox_TestIntakeFan_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)






















