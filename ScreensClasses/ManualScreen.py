import easygui
import time
from ScreensClasses.ScreenIndex import AUTOMATIC_SCREEN_INDEX
from Screens_py.VcDvtTestTools_screen_manual_mode import Ui_Manual
from ScreensClasses.SettingsScreen import *
from Interfaces.InterfaceVIP import *
import ctypes
import datetime
from Utilities.FileEncoder import Encryption
import secrets
import os
import binascii
import zipfile
import pyminizip

TS_COLOR_PASSED = 'background-color: #9df793'
TS_COLOR_NOTPASSED = 'background-color: #fe9393'
TS_COLOR_INIT = 'background-color: self.color'

RESULT_TEST_PASSED = "1"
RESULT_TEST_NOT_PASSED = "0"
RESULT_TEST_NOT_TESTED = "2"
RESULT_TEST_INCORRECT = "3"

PRE_ASSEMBLY_TEST = 1
POST_ASSEMBLY_TEST = 2

DEBUG_APP = 1
RELEASE_APP = 2


class ManualScreen(QtWidgets.QMainWindow, Ui_Manual):
    def __init__(self, w, interface_vip, parent=None):
        super(ManualScreen, self).__init__(parent)
        self.setupUi(self)
        self.widget = w
        self.InterfaceVIP = interface_vip
        self.nameReportFile = None
        self.assemblyTest = PRE_ASSEMBLY_TEST  # for Walter
        # self.assemblyTest = POST_ASSEMBLY_TEST  # for Howell
        self.versionApp = DEBUG_APP  # for debug
        # self.versionApp = RELEASE_APP  # for release

        # self.widget.setWindowTitle("VcDvtTestTools | Manual Mode")
        self.btn_AutomaticManual.clicked.connect(self.AutomaticManual)
        self.btn_SettingsManual.clicked.connect(self.SettingsManual)
        self.btn_CleanManual.clicked.connect(self.CleanManual)

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

        self.btn_Lamp_Test.clicked.connect(self.Lamp_Test)

        self.btn_IntakeFan_On.clicked.connect(self.IntakeFan_On)
        self.btn_IntakeFan_Off.clicked.connect(self.IntakeFan_Off)
        self.btn_IntakeFan_Test.clicked.connect(self.IntakeFan_Test)

        self.btn_Blower_On.clicked.connect(self.Blower_On)
        self.btn_Blower_Off.clicked.connect(self.Blower_Off)
        self.btn_Blower_Test.clicked.connect(self.Blower_Test)

        self.btn_GetState.clicked.connect(self.GetState)

        self.btn_Bme688_Exhaust_Test.clicked.connect(self.Bme688_Exhaust_Test)
        self.btn_Bme688_Intake_Test.clicked.connect(self.Bme688_Intake_Test)
        self.btn_Bme688_Left_Test.clicked.connect(self.Bme688_Left_Test)
        self.btn_Bme688_Right_Test.clicked.connect(self.Bme688_Right_Test)

        self.btn_WeightBack_Test.clicked.connect(self.WeightBack_Test)
        self.btn_WeightFront_Test.clicked.connect(self.WeightFront_Test)

        self.btn_CatalyticBoard_Test.clicked.connect(self.CatalyticBoard_Test)

        self.pButtonCreateReport.clicked.connect(self.CreateReport)


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
        self.checkBox_TestBme688_Exhaust_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Exhaust_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Intake_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Intake_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Left_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Left_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Right_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestBme688_Right_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestWeightLeft_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestWeightLeft_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestWeightRight_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestWeightRight_NotPassed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestCatalyticBoard_Passed.setStyleSheet(TS_COLOR_INIT)
        self.checkBox_TestCatalyticBoard_NotPassed.setStyleSheet(TS_COLOR_INIT)

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
        self.checkBox_TestBme688_Exhaust_Passed.setChecked(0)
        self.checkBox_TestBme688_Exhaust_NotPassed.setChecked(0)
        self.checkBox_TestBme688_Intake_Passed.setChecked(0)
        self.checkBox_TestBme688_Intake_NotPassed.setChecked(0)
        self.checkBox_TestBme688_Left_Passed.setChecked(0)
        self.checkBox_TestBme688_Left_NotPassed.setChecked(0)
        self.checkBox_TestBme688_Right_Passed.setChecked(0)
        self.checkBox_TestBme688_Right_NotPassed.setChecked(0)
        self.checkBox_TestWeightLeft_Passed.setChecked(0)
        self.checkBox_TestWeightLeft_NotPassed.setChecked(0)
        self.checkBox_TestWeightRight_Passed.setChecked(0)
        self.checkBox_TestWeightRight_NotPassed.setChecked(0)
        self.checkBox_TestCatalyticBoard_Passed.setChecked(0)
        self.checkBox_TestCatalyticBoard_NotPassed.setChecked(0)

    # TA/TB
    def MainMotor_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestMainMotor_Passed.setChecked(1)
            self.checkBox_TestMainMotor_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestMainMotor_NotPassed.setChecked(1)
            self.checkBox_TestMainMotor_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def AcMainPower_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_AC_POWER)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestAcMainPower_Passed.setChecked(1)
            self.checkBox_TestAcMainPower_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestAcMainPower_NotPassed.setChecked(1)
            self.checkBox_TestAcMainPower_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def ChamberMotorLeft_Start(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Stop(self):
        self.checkBox_UnlockTopRight.setChecked(0)

    def ChamberMotorLeft_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_2)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_MOTOR_3)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_PTC_HEATER_2)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestPadHeaterRight_Passed.setChecked(1)
            self.checkBox_TestPadHeaterRight_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestPadHeaterRight_NotPassed.setChecked(1)
            self.checkBox_TestPadHeaterRight_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def Lamp_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
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
                self.checkBox_FrontLidOpen_Yes.setChecked(1)
            else:
                self.checkBox_FrontLidOpen_No.setChecked(1)

            if (state_sensors & IFC_VIP_STATE_SWITCH_BACK_LID_OPEN) > 0:
                self.checkBox_BackLidOpen_Yes.setChecked(1)
            else:
                self.checkBox_BackLidOpen_No.setChecked(1)

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
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_FAN_2)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestIntakeFan_Passed.setChecked(1)
            self.checkBox_TestIntakeFan_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestIntakeFan_NotPassed.setChecked(1)
            self.checkBox_TestIntakeFan_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)


    def Blower_On(self):
        pass

    def Blower_Off(self):
        pass

    def Blower_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_FAN_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestBlower_Passed.setChecked(1)
            self.checkBox_TestBlower_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestBlower_NotPassed.setChecked(1)
            self.checkBox_TestBlower_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)


    def Bme688_Exhaust_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_BME688_4)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestBme688_Exhaust_Passed.setChecked(1)
            self.checkBox_TestBme688_Exhaust_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestBme688_Exhaust_NotPassed.setChecked(1)
            self.checkBox_TestBme688_Exhaust_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def Bme688_Intake_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_BME688_3)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestBme688_Intake_Passed.setChecked(1)
            self.checkBox_TestBme688_Intake_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestBme688_Intake_NotPassed.setChecked(1)
            self.checkBox_TestBme688_Intake_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def Bme688_Left_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_BME688_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestBme688_Left_Passed.setChecked(1)
            self.checkBox_TestBme688_Left_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestBme688_Left_NotPassed.setChecked(1)
            self.checkBox_TestBme688_Left_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def Bme688_Right_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_BME688_2)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestBme688_Right_Passed.setChecked(1)
            self.checkBox_TestBme688_Right_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestBme688_Right_NotPassed.setChecked(1)
            self.checkBox_TestBme688_Right_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)


    def WeightBack_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_WEIGHT_SENSOR_1)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestWeightBack_Passed.setChecked(1)
            self.checkBox_TestWeightBack_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestWeightBack_NotPassed.setChecked(1)
            self.checkBox_TestWeightBack_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def WeightFront_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_WEIGHT_SENSOR_2)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestWeightFront_Passed.setChecked(1)
            self.checkBox_TestWeightFront_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestWeightFront_NotPassed.setChecked(1)
            self.checkBox_TestWeightFront_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)


    def CatalyticBoard_Test(self):
        result, read_data = self.InterfaceVIP.cmd_test(IFC_VIP_COMPONENT_CATALYTIC_BOARD)
        # state - IFC_VIP_STATE_IDLE or IFC_VIP_TEST_RESULT_ERROR
        if result == 0 and self.InterfaceVIP.get_state() == IFC_VIP_STATE_IDLE:
            self.checkBox_TestCatalyticBoard_Passed.setChecked(1)
            self.checkBox_TestCatalyticBoard_Passed.setStyleSheet(TS_COLOR_PASSED)
        else:
            self.checkBox_TestCatalyticBoard_NotPassed.setChecked(1)
            self.checkBox_TestCatalyticBoard_NotPassed.setStyleSheet(TS_COLOR_NOTPASSED)

    def GetResultTest(self, name_test, check_box_passed, check_box_not_passed):
        if check_box_passed.isChecked():
            if check_box_not_passed.isChecked():
                ctypes.windll.user32.MessageBoxW(0, name_test + " is not correct!", "", 16)
                return RESULT_TEST_INCORRECT
            else:
                return RESULT_TEST_PASSED
        else:
            if check_box_not_passed.isChecked():
                return RESULT_TEST_NOT_PASSED
            else:
                ctypes.windll.user32.MessageBoxW(0, name_test + " is not tested!", "", 16)
                return RESULT_TEST_NOT_TESTED

    def CreateReport(self):
        # read and check serial number
        # DEBUG
        string_sn = "LL01-000000000"
        # DEBUG
        string_check = "LL01"
        string_sn_check = string_sn.split("-")
        if string_check != string_sn_check[0]:
            ctypes.windll.user32.MessageBoxW(0, "Incorrect Serial Number!", "Error!", 16)
            return

        datetime_object = datetime.datetime.now()
        string_result = datetime_object.strftime("%m/%d/%Y-%H:%M:%S,")

        if self.assemblyTest == PRE_ASSEMBLY_TEST:
            # for Walter
            string_result += "Walter,L3600-TA4,"
        else:
            # for Howell
            string_result += "Howell,L3600-TB4,"

        # Main Motor test result - TA400
        result_test = self.GetResultTest("Main Motor", self.checkBox_TestMainMotor_Passed,
                                         self.checkBox_TestMainMotor_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # AC Main Power test result - TA401
        result_test = self.GetResultTest("AC Main Power", self.checkBox_TestAcMainPower_Passed,
                                         self.checkBox_TestAcMainPower_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Chamber Motor Left test result - TA402
        result_test = self.GetResultTest("Chamber Motor Left", self.checkBox_TestChamberMotorLeft_Passed,
                                         self.checkBox_TestChamberMotorLeft_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Chamber Motor Right test result - TA403
        result_test = self.GetResultTest("Chamber Motor Right", self.checkBox_TestChamberMotorRight_Passed,
                                         self.checkBox_TestChamberMotorRight_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # PTC Heater Intake test result - TA404
        result_test = self.GetResultTest("PTC Heater Intake", self.checkBox_TestPtcHeaterIntake_Passed,
                                         self.checkBox_TestPtcHeaterIntake_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # PTC Heater Internal test result - TA405
        result_test = self.GetResultTest("PTC Heater Internal", self.checkBox_TestPtcHeaterInternal_Passed,
                                         self.checkBox_TestPtcHeaterInternal_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Pad Heater Left test result - TA406
        result_test = self.GetResultTest("Pad Heater Left", self.checkBox_TestPadHeaterLeft_Passed,
                                         self.checkBox_TestPadHeaterLeft_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Pad Heater Right test result - TA407
        result_test = self.GetResultTest("Pad Heater Right", self.checkBox_TestPadHeaterRight_Passed,
                                         self.checkBox_TestPadHeaterRight_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Lamp test result - TA408
        result_test = self.GetResultTest("Lamp", self.checkBox_TestLamp_Passed,
                                         self.checkBox_TestLamp_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # switch - Chamber Left Present result - TA409
        result_test = self.GetResultTest("Chamber Left Present", self.checkBox_PresentChamberLeft_Yes,
                                         self.checkBox_PresentChamberLeft_No)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # switch - Chamber Right Present result - TA410
        result_test = self.GetResultTest("Chamber Right Present", self.checkBox_PresentChamberRight_Yes,
                                         self.checkBox_PresentChamberRight_No)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # switch - Back Lid Open result - TA411
        result_test = self.GetResultTest("Back Lid Open", self.checkBox_BackLidOpen_Yes,
                                         self.checkBox_BackLidOpen_No)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # switch - Front Lid Open result - TA412
        result_test = self.GetResultTest("Front Lid Open", self.checkBox_FrontLidOpen_Yes,
                                         self.checkBox_FrontLidOpen_No)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # switch - Top Locked result - TA413
        result_test = self.GetResultTest("Top Locked", self.checkBox_TopLocked_Yes,
                                         self.checkBox_TopLocked_No)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Intake Fan test result - TA414
        result_test = self.GetResultTest("Intake Fan", self.checkBox_TestIntakeFan_Passed,
                                         self.checkBox_TestIntakeFan_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Blower test result - TA415
        result_test = self.GetResultTest("Blower", self.checkBox_TestBlower_Passed,
                                         self.checkBox_TestBlower_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # BME688 Exhaust test result - TA416
        result_test = self.GetResultTest("BME688 Exhaust", self.checkBox_TestBme688_Exhaust_Passed,
                                         self.checkBox_TestBme688_Exhaust_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # BME688 Intake test result - TA417
        result_test = self.GetResultTest("BME688 Intake", self.checkBox_TestBme688_Intake_Passed,
                                         self.checkBox_TestBme688_Intake_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # BME688 Chamber Left test result - TA418
        result_test = self.GetResultTest("BME688 Chamber Left", self.checkBox_TestBme688_Left_Passed,
                                         self.checkBox_TestBme688_Left_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # BME688 Chamber Right test result - TA419
        result_test = self.GetResultTest("BME688 Chamber Right", self.checkBox_TestBme688_Right_Passed,
                                         self.checkBox_TestBme688_Right_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Weight Sensor Chamber Left test result - TA420
        result_test = self.GetResultTest("Weight Sensor Chamber Left", self.checkBox_TestWeightLeft_Passed,
                                         self.checkBox_TestWeightLeft_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Weight Sensor Chamber Right test result - TA421
        result_test = self.GetResultTest("Weight Sensor Chamber Right", self.checkBox_TestWeightRight_Passed,
                                         self.checkBox_TestWeightRight_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test + ","

        # Catalytic Board test result - TA422
        result_test = self.GetResultTest("Catalytic Board", self.checkBox_TestCatalyticBoard_Passed,
                                         self.checkBox_TestCatalyticBoard_NotPassed)
        if result_test == RESULT_TEST_INCORRECT or result_test == RESULT_TEST_NOT_TESTED:
            return
        string_result = string_result + result_test

        if self.versionApp == DEBUG_APP:
            self.nameReportFile = ".\\Reports\\" + string_sn + ".vctr"  # DEBUG
        else:
            self.nameReportFile = "Reports\\" + string_sn + ".vctr"  # RELEASE
        file_output = open(self.nameReportFile, 'w')
        file_output.write(string_result)
        file_output.close()

        if self.versionApp == DEBUG_APP:
            name_zip_file = ".\\Reports\\" + string_sn + ".zip"  # DEBUG
        else:
            name_zip_file = "Reports\\" + string_sn + ".zip"  # RELEASE

        pyminizip.compress(self.nameReportFile, None, name_zip_file, "vctr", 5)
        os.remove(self.nameReportFile)
        os.rename(name_zip_file, self.nameReportFile)

        ctypes.windll.user32.MessageBoxW(0, "The report file has been successfully created!", "", 64)







