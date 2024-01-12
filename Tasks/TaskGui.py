import sys
import time
import threading

import roboto as Roboto
import self
from PyQt5 import QtWidgets, QtCore
from PyQt5 import Qt
from ScreensClasses.ManualScreen import ManualScreen
from ScreensClasses.AutomaticScreen import AutomaticScreen
# from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5.QtCore import QMutex
from PyQt5.QtGui import QFont
import platform

#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # enable highdpi scaling
#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    # use highdpi icons


TASK_GUI_RESULT_OK = 0
TASK_GUI_RESULT_ERROR = 1
TASK_GUI_EXIT_FROM_APPLICATION = 2


class TaskGui(threading.Thread):
    def __init__(self):cd
        self.exitFlag = True
        threading.Thread.__init__(self)
        self.queueLock = threading.Lock()
        self.widget = QtWidgets.QStackedWidget()
        self.mutex = QMutex()
        self.result = TASK_GUI_RESULT_OK

        #self.widget.setWindowFlags(Qt.FramelessWindowHint)

        #self.SettingsScreen = SettingsScreen(self.widget)

       # gpio_control = GpioControl(self.SettingsScreen)
       # charger_control = GhargerControl(self.SettingsScreen)
       # service_cmd = ServiceCmd(self.SettingsScreen)
       # self.GpioState = GpioState(self.SettingsScreen)
       # self.ChargerState = ChargerState(self.SettingsScreen)
       # self.ServiceData = ServiceData(self.SettingsScreen)

        #self.ManualScreen = ManualScreen(self.widget, gpio_control, charger_control, service_cmd)
        #self.AutomaticScreen = AutomaticScreen(self.widget, charger_control, service_cmd)


        self.ManualScreen = ManualScreen(self)
        self.AutomaticScreen = AutomaticScreen(self)


        #self.widget.addWidget(self.SettingsScreen)
        self.widget.addWidget(self.AutomaticScreen)
        self.widget.addWidget(self.ManualScreen)



        self.widget.adjustSize()

        if platform.system() == 'Windows':
            self.widget.setFixedHeight(720)
            self.widget.setFixedWidth(1280)
            self.widget.show()
        else:
            self.widget.showFullScreen()
            font = QFont('Roboto')
            self.widget.setFont(font)


    def stop(self):
        self.mutex.lock()
        self.exitFlag = False
        self.mutex.unlock()

    def GetExitFlag(self):
        self.mutex.lock()
        flag = self.exitFlag
        self.mutex.unlock()
        return flag

    def CloseAllConnection(self):
        self.ChargerState.terminate()
        if self.ChargerState.wait(1000):
            self.GpioState.terminate()
        elif self.GpioState.wait(1000):
            self.ServiceData.terminate()
        elif self.ServiceData.wait(1000):
            return TASK_GUI_RESULT_OK
        else:
            return TASK_GUI_RESULT_ERROR

    def WaitingHardwareServer(self):
        while True:
            exit_flag = self.GetExitFlag()
            if exit_flag is False:
                return TASK_GUI_EXIT_FROM_APPLICATION

            if self.SettingsScreen.GetFlagPresentHardwareSensor() is False:
                time.sleep(0.2)
                test_button_clicked = self.SettingsScreen.GetTestButtonClicked()
                if test_button_clicked is True:
                    self.SettingsScreen.TestPresentHwServer()
                    if self.SettingsScreen.GetFlagPresentHardwareSensor() is True:
                        self.SettingsScreen.SetHwServerPresent()
                    else:
                        self.SettingsScreen.SetHwServerNotPresent()
                        time.sleep(1.0)
                        continue
                else:
                    continue
            else:
                return TASK_GUI_RESULT_OK

    def run(self):
        while True:

            if self.WaitingHardwareServer() == TASK_GUI_EXIT_FROM_APPLICATION:
                break

            self.ChargerState.start()
            self.GpioState.start()
            self.ServiceData.start()

            while self.GetExitFlag():
                """if not workQueue.empty():
                    data = q.get()
                    queueLock.release()"""
                # print("444")
                # self.queueLock.release()
                time.sleep(0.1)

                if self.SettingsScreen.GetFlagPresentHardwareSensor() is False:
                    # self.result = self.CloseAllConnection()
                    break

                self.ManualScreen.updateState(self.GpioState.GetState())
                data, event_changed_state = self.ChargerState.GetChargerState()
                self.ManualScreen.updateSettings(data)
                self.AutomaticScreen.updateSettings(data, event_changed_state)

                data = self.ServiceData.GetSringData()
                self.ManualScreen.setGetSringData(data)
                self.AutomaticScreen.setGetSringData(data)

            if self.result == TASK_GUI_RESULT_OK:
                continue
            else:
                break

        self.queueLock.acquire()
        print("Stop TaskGui")
        self.queueLock.release()

