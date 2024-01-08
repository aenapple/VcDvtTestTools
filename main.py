import sys
import time
import platform
import threading
from PyQt5.QtWidgets import QApplication
from Tasks.TaskGui import TaskGui
from Tasks.TaskEvseController import TaskEvseController
import paho.mqtt.client as mqtt
from random import randrange, uniform
from Mqtt.GpioState import GpioState
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys

# STANDBY,2000,24000,18,238,0,OFF


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

    taskGui = TaskGui()
    taskGui.start()

    # taskGpioState = GpioState()
    # taskGpioState = GpioState.start()

    app.exec_()


    # taskSystem.stop()
    # taskEvseController.stop()
    taskGui.stop()

    time.sleep(0.5)
    print("Stop Application")
