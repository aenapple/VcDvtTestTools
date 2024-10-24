import sys
import time
import threading

import roboto as Roboto
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from ScreensClasses.ManualScreen import ManualScreen
from ScreensClasses.AutomaticScreen import AutomaticScreen
from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5.QtCore import QMutex
from Interfaces import InterfaceVIP
import platform

# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # enable highdpi scaling
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)    # use highdpi icons


TASK_GUI_RESULT_OK = 0
TASK_GUI_RESULT_ERROR = 1
TASK_GUI_EXIT_FROM_APPLICATION = 2


class TaskGui(threading.Thread):
    def __init__(self, interface_vip):
        self.exitFlag = True
        threading.Thread.__init__(self)
        self.queueLock = threading.Lock()
        self.widget = QtWidgets.QStackedWidget()
        self.mutex = QMutex()
        self.result = TASK_GUI_RESULT_OK
        self.InterfaceVIP = interface_vip

        self.SettingsScreen = SettingsScreen(self.widget, interface_vip)
        self.ManualScreen = ManualScreen(self.widget, interface_vip)
        self.AutomaticScreen = AutomaticScreen(self.widget, interface_vip)

        self.widget.addWidget(self.SettingsScreen)
        self.widget.addWidget(self.AutomaticScreen)
        self.widget.addWidget(self.ManualScreen)

        self.widget.adjustSize()

        self.widget.setFixedHeight(720)
        self.widget.setFixedWidth(1280)
        self.widget.setWindowIcon(QtGui.QIcon('Vc_icon4.png'))
        self.widget.setWindowTitle("VCycene DVT Test Tool")

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

