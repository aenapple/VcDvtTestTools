import sys
import time
import threading

import roboto as Roboto
import self
from PyQt5 import QtWidgets, QtCore
from PyQt5 import Qt
from PyQt5 import QtGui
from ScreensClasses.ManualScreen import ManualScreen
from ScreensClasses.AutomaticScreen import AutomaticScreen
from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5.QtCore import QMutex
from PyQt5.QtGui import QFont
import platform

# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # enable highdpi scaling
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    # use highdpi icons


TASK_GUI_RESULT_OK = 0
TASK_GUI_RESULT_ERROR = 1
TASK_GUI_EXIT_FROM_APPLICATION = 2


class TaskGui(threading.Thread):
    def __init__(self):
        self.exitFlag = True
        threading.Thread.__init__(self)
        self.queueLock = threading.Lock()
        self.widget = QtWidgets.QStackedWidget()
        self.mutex = QMutex()
        self.result = TASK_GUI_RESULT_OK

        self.SettingsScreen = SettingsScreen(self.widget)
        self.ManualScreen = ManualScreen(self.widget)
        self.AutomaticScreen = AutomaticScreen(self.widget)

        self.widget.addWidget(self.SettingsScreen)
        self.widget.addWidget(self.AutomaticScreen)
        self.widget.addWidget(self.ManualScreen)

        self.widget.adjustSize()

        self.widget.setFixedHeight(720)
        self.widget.setFixedWidth(1280)
        self.widget.setWindowIcon(QtGui.QIcon('Vc_icon4.png'))
        self.widget.setWindowTitle("VcDVT TEST TOOL")

        self.widget.show()

    def stop(self):
        self.mutex.lock()
        self.exitFlag = False
        self.mutex.unlock()

    def GetExitFlag(self):
        self.mutex.lock()
        flag = self.exitFlag
        self.mutex.unlock()
        return flag

    """ def CloseAllConnection(self):
        self.ChargerState.terminate()
        if self.ChargerState.wait(1000):
            self.GpioState.terminate()
        elif self.GpioState.wait(1000):
            self.ServiceData.terminate()
        elif self.ServiceData.wait(1000):
            return TASK_GUI_RESULT_OK
        else:
            return TASK_GUI_RESULT_ERROR """

    """ def WaitingHardwareServer(self):
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
                return TASK_GUI_RESULT_OK """

    def run(self):
        while True:

            """ if self.WaitingHardwareServer() == TASK_GUI_EXIT_FROM_APPLICATION:
                break

            self.ChargerState.start()
            self.GpioState.start()
            self.ServiceData.start() """

            while self.GetExitFlag():
                """if not workQueue.empty():
                    data = q.get()
                    queueLock.release()"""
                # print("444")
                # self.queueLock.release()
                time.sleep(0.1)

                """ if self.SettingsScreen.GetFlagPresentHardwareSensor() is False:
                    # self.result = self.CloseAllConnection()
                    break

                self.ManualScreen.updateState(self.GpioState.GetState())
                data, event_changed_state = self.ChargerState.GetChargerState()
                self.ManualScreen.updateSettings(data)
                self.AutomaticScreen.updateSettings(data, event_changed_state)

                data = self.ServiceData.GetSringData()
                self.ManualScreen.setGetSringData(data)
                self.AutomaticScreen.setGetSringData(data) """

            break

        self.queueLock.acquire()
        print("Stop TaskGui")
        self.queueLock.release()

