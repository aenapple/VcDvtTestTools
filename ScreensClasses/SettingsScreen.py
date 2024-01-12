import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from Screens_py.VcDvtTestTools_screen_settings import Ui_Settings
#import Mqtt.Control
from ScreensClasses.ScreenIndex import *
from images import *
#from Mqtt.Control import *
#import paho.mqtt.publish as publish
from PyQt5.QtCore import QMutex
from IniFile import IniFile
import sys

COM_PORT = 'COM1'

HARDWARE_SERVER_IP = 0
HARDWARE_SERVER_PORT = 1
HARDWARE_SERVER_CLIENT = 2
HARDWARE_SERVER_NAME = 3
HARDWARE_SERVER_PASSWORD = 4

HARDWARE_SERVER_TOPIC_GPIO_CONTROL = 'CONTROL'
HARDWARE_SERVER_TOPIC_GPIO_STATE = 'SWITCHES'
HARDWARE_SERVER_TOPIC_CHARGER_CONTROL = 'CHARGER'
HARDWARE_SERVER_TOPIC_CHARGER_STATE = 'STATE'
HARDWARE_SERVER_TOPIC_SERVICE_DATA = 'SERVICE_DATA'
HARDWARE_SERVER_TOPIC_SERVICE_CMD = 'SERVICE_CMD'


TS_CMD_SET_INTERFACE_V5 = 'SET_INTERFACE_V5'
TS_CMD_SET_INTERFACE_V6 = 'SET_INTERFACE_V6'
TS_CMD_SET_INTERFACE_V7 = 'SET_INTERFACE_V7'
TS_CMD_SET_NO_INTERFACE = 'SET_NO_INTERFACE'

TS_CMD_GET_VERSION_APP = 'GET_VERSION_APP'
TS_CMD_GET_SERIAL_NUMBER = 'GET_SERIAL_NUMBER'


class SettingsScreen(PyQt5.QtWidgets.QMainWindow, Ui_Settings):
    def __init__(self, w, parent=None):
        super(SettingsScreen, self).__init__(parent)
        self.setupUi(self)
        self.widget = w



        #self.label_green.setPixmap(QtGui.QPixmap('connect.png'))
        #pixmap = QPixmap("connect_red.png")
        #self.label_red.setPixmap(pixmap)
        #self.label_red.setPixmap(QtGui.QPixmap("images/connect_red.png"))
        #self.show()

        pixmap = QPixmap("connect.png")
        self.label_green.setPixmap(pixmap)
        pixmap = QPixmap('connect_red.png')
        self.label_red.setPixmap(pixmap)

        self.btn_CleanSettings.clicked.connect(self.CleanSettings)
        self.btn_ManualSettings.clicked.connect(self.setManualScreen)
        self.btn_AutomaticSettings.clicked.connect(self.setAutomatedScreen)
        self.lineEdit_ComPort.setText('')
        self.btn_ConnectSettings.clicked.connect(self.connect_sett)
        self.btn_DisconnectSettings.clicked.connect(self.disconnect_sett)
        self.btn_GetStateSettings.clicked.connect(self.getstate_sett)


    def CleanSettings(self):
        self.lineEdit_ComPort.setText(' ')
        self.lineEdit_GetState.setText(' ')

    def setManualScreen(self):
        # self.progressBar_start.setValue(0)
        self.widget.setCurrentIndex(MANUAL_SCREEN_INDEX)

    def setAutomatedScreen(self):
        self.widget.setCurrentIndex(AUTOMATIC_SCREEN_INDEX)

    def connect_sett(self):
        self.label_Connect.setVisible(1)
        self.label_Connect.setEnabled(1)

    def disconnect_sett(self):
        self.label_green.setVisible(0)
        self.label_red.setEnabled(1)

    def getstate_sett(self):
        self.lineEdit_GetState.setText('State')
















        """self.hardwareServer = ['localhost', '50000', 'client ID', 'name', 'password']
        self.flagPresentHwServer = False
        self.testButtonClicked = False
        self.mutexFlagPresentHwServer = QMutex()
        self.mutexPublish = QMutex()
        self.mutexTestButtonClicked = QMutex()
        self.mutexHardwareSever = QMutex(

        self.Init()
        self.btn_ManualMode.clicked.connect(self.SetManualScreen)
        self.btn_AutomaticMode.clicked.connect(self.SetAutomatedScreen)
        self.btn_Connect.clicked.connect(self.connectClicked)
        self.checkBox_v5.clicked.connect(self.v5Clicked)
        self.checkBox_v6.clicked.connect(self.v6Clicked)
        self.checkBox_v7.clicked.connect(self.v7Clicked)
        self.checkBox_noInterface.clicked.connect(self.noInterfacelicked)
        self.btn_Exit.clicked.connect(self.exitClicked)

         self.lineEdit_HardwareServerIP.setText(self.hardwareServer[HARDWARE_SERVER_IP])
        self.lineEdit_Port.setText(self.hardwareServer[HARDWARE_SERVER_PORT])
        self.lineEdit_ClientID.setText(self.hardwareServer[HARDWARE_SERVER_CLIENT])
        self.lineEdit_name.setText(self.hardwareServer[HARDWARE_SERVER_NAME])
        self.lineEdit_password.setText(self.hardwareServer[HARDWARE_SERVER_PASSWORD]) 


    def exitClicked(self):
        self.widget.close()


    def Init(self):
        self.label.setEnabled(0)
        self.label_Messages.setText(" ")
        self.checkBox_v5.setChecked(0)
        self.checkBox_v6.setChecked(0)
        self.checkBox_v7.setChecked(0)
        self.checkBox_noInterface.setChecked(0)

        f = IniFile()
        state = f.get_hardwareServerIP()
        del f
        self.lineEdit_HardwareServerIP.setText(state)

        f = IniFile()
        state = f.get_port()
        del f
        self.lineEdit_Port.setText(state)

        f = IniFile()
        state = f.get_clientID()
        del f
        self.lineEdit_ClientID.setText(state)

        f = IniFile()
        state = f.get_name()
        del f
        self.lineEdit_name.setText(state)

        f = IniFile()
        state = f.get_password()
        del f
        self.lineEdit_password.setText(state)

        f = IniFile()
        state = f.get_protocol()
        del f
        if state == 'V5':
            self.checkBox_v5.setChecked(1)
            self.v5Clicked()
        elif state == 'V6':
            self.checkBox_v6.setChecked(1)
            self.v6Clicked()
        elif state == 'V7':
            self.checkBox_v7.setChecked(1)
            self.v7Clicked()
        else:
            self.checkBox_noInterface.setChecked(1)
            self.noInterfacelicked()


    def SetManualScreen(self):
        self.widget.setCurrentIndex(MANUAL_SCREEN_INDEX)

    def SetAutomatedScreen(self):
        self.widget.setCurrentIndex(AUTOMATIC_SCREEN_INDEX)

    def connectClicked(self):
        self.mutexTestButtonClicked.lock()
        self.testButtonClicked = True
        self.mutexTestButtonClicked.unlock()

    def TestPresentHwServer(self):
        self.mutexHardwareSever.lock()

        port = self.lineEdit_Port.text()
        host_name = self.lineEdit_HardwareServerIP.text()
        client_id = self.lineEdit_ClientID.text()
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()


        self.mutexHardwareSever.unlock()

        self.mutexPublish.lock()

        try:
            publish.single(HARDWARE_SERVER_TOPIC_CHARGER_CONTROL,
                           Mqtt.Control.TS_CMD_GET_STATE,
                           hostname=host_name,
                           port=int(port),
                           client_id=client_id + 'test'
                           )
            self.SetFlagPresentHardwareSensor(True)
            self.SetHardwareServer(HARDWARE_SERVER_IP, host_name)
            self.SetHardwareServer(HARDWARE_SERVER_PORT, port)
            self.SetHardwareServer(HARDWARE_SERVER_CLIENT, client_id)

            self.save_port_settings(port)
            self.save_hardwareServerIP_settings(host_name)
            self.save_clientID_settings(client_id)
            self.save_name_settings(name)
            self.save_password_settings(password)

        except:
            self.SetFlagPresentHardwareSensor(False)

        self.mutexPublish.unlock()


    def Publish(self, topic, data, client_id):
        flag = self.GetFlagPresentHardwareSensor()
        if flag is False:
            return

        hardware_server = self.GetHardwareServer()
        self.mutexPublish.lock()

        try:
            publish.single(topic,
                           data,
                           hostname=hardware_server[HARDWARE_SERVER_IP],
                           port=int(hardware_server[HARDWARE_SERVER_PORT]),
                           client_id=hardware_server[HARDWARE_SERVER_CLIENT] + client_id
                           )
            self.SetFlagPresentHardwareSensor(True)
        except:
            self.SetFlagPresentHardwareSensor(False)

        self.mutexPublish.unlock()


    def SetHwServerPresent(self):
        self.label_red.setVisible(0)
        self.label.setVisible(1)
        self.label.setEnabled(1)
        self.label_Messages.setText("Hardware Server is present!")

    def SetHwServerNotPresent(self):
        self.label_Messages.setText("Hardware Server is not present!")
        self.label.setVisible(0)
        self.label_red.setVisible(1)
        self.label_red.setEnabled(1)

    def GetHardwareServer(self):
        self.mutexHardwareSever.lock()
        hardware_server = self.hardwareServer
        self.mutexHardwareSever.unlock()
        return hardware_server

    def SetHardwareServer(self, index, value):
        self.mutexHardwareSever.lock()
        self.hardwareServer[index] = value
        self.mutexHardwareSever.unlock()


    def GetFlagPresentHardwareSensor(self):
        self.mutexFlagPresentHwServer.lock()
        flag = self.flagPresentHwServer
        self.mutexFlagPresentHwServer.unlock()
        return flag

    def SetFlagPresentHardwareSensor(self, flag):
        self.mutexFlagPresentHwServer.lock()
        self.flagPresentHwServer = flag
        if flag:
            self.SetHwServerPresent()
        else:
            self.SetHwServerNotPresent()
        self.mutexFlagPresentHwServer.unlock()

    def GetTestButtonClicked(self):
        self.mutexTestButtonClicked.lock()
        test_button_clicked = self.testButtonClicked
        self.testButtonClicked = False
        self.mutexTestButtonClicked.unlock()
        return test_button_clicked

    def save_hardwareServerIP_settings(self, host_name):
        f = IniFile()
        f.set_hardwareServerIP(str(host_name))
        del f

    def save_port_settings(self, port):
        f = IniFile()
        f.set_port(str(port))
        del f

    def save_clientID_settings(self, clientID):
        f = IniFile()
        f.set_clientID(str(clientID))
        del f

    def save_name_settings(self, name):
        f = IniFile()
        f.set_name(str(name))
        del f

    def save_password_settings(self, password):
        f = IniFile()
        f.set_password(str(password))
        del f

    def save_protocol_settings(self, protocol):
        f = IniFile()
        f.set_protocol(str(protocol))
        del f


    def v5Clicked(self):
        self.checkBox_v6.setChecked(0)
        self.checkBox_v7.setChecked(0)
        self.checkBox_noInterface.setChecked(0)
        protocol = "V5"
        self.save_protocol_settings(protocol)
        self.Publish(HARDWARE_SERVER_TOPIC_CHARGER_CONTROL, TS_CMD_SET_INTERFACE_V5, "_charger")


    def v6Clicked(self):
        self.checkBox_v5.setChecked(0)
        self.checkBox_v7.setChecked(0)
        self.checkBox_noInterface.setChecked(0)
        protocol = "V6"
        self.save_protocol_settings(protocol)
        self.Publish(HARDWARE_SERVER_TOPIC_CHARGER_CONTROL, TS_CMD_SET_INTERFACE_V6, "_charger")


    def v7Clicked(self):
        self.checkBox_v6.setChecked(0)
        self.checkBox_v5.setChecked(0)
        self.checkBox_noInterface.setChecked(0)
        protocol = "V7"
        self.save_protocol_settings(protocol)
        self.Publish(HARDWARE_SERVER_TOPIC_CHARGER_CONTROL, TS_CMD_SET_INTERFACE_V7, "_charger")


    def noInterfacelicked(self):
        self.checkBox_v6.setChecked(0)
        self.checkBox_v7.setChecked(0)
        self.checkBox_v5.setChecked(0)
        protocol = "No Interface"
        self.save_protocol_settings(protocol)
        self.Publish(HARDWARE_SERVER_TOPIC_CHARGER_CONTROL, TS_CMD_SET_NO_INTERFACE, "_charger")"""









