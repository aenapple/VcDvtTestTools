import time
import platform
import threading

from PyQt5.QtWidgets import QApplication
from ScreensClasses.ScreenIndex import *
from PyQt5 import QtWidgets
import Tasks.TaskGui
from ScreensClasses.ManualScreen import ManualScreen
from ScreensClasses.AutomaticScreen import AutomaticScreen
from ScreensClasses.SettingsScreen import SettingsScreen
from PyQt5 import QtGui
import sys


class TaskSystem(threading.Thread):
    def __init__(self):
        self.exitFlag = True
        threading.Thread.__init__(self)
        self.queueLock = threading.Lock()

    def stop(self):
        self.exitFlag = False

    def run(self):
        while self.exitFlag:
            # self.queueLock.acquire()
            """if not workQueue.empty():
                data = q.get()
                queueLock.release()"""
            # print("444")
            # self.queueLock.release()

            time.sleep(0.1)

        self.queueLock.acquire()
        # print("Stop TaskSystem")
        self.queueLock.release()


if __name__ == '__main__':
    # print(platform.system())
    app = QApplication(sys.argv)
    app.setStyle('Windows')

    # taskSystem = TaskSystem()
    # taskSystem.start()

    # taskEvseController = TaskEvseController()
    # taskEvseController.start()

    taskGui = Tasks.TaskGui.TaskGui()
    taskGui.start()

    """ w1 = ManualScreen(self)
    w1.setWindowTitle("VcDvtTestTools")
    w1.show()
    w2 = AutomaticScreen(self)
    w2.setWindowTitle("VcDvtTestTools")
    w2.show()
    w3 = SettingsScreen(self)
    w3.setWindowTitle("VcDvtTestTools")
    w3.show() """

    app.exec_()

    taskGui.stop()
    time.sleep(0.5)
    print("Stop Application")
