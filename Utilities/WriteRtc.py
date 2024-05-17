# from Interfaces import InterfaceVIP
import sys
import time
from Interfaces.InterfaceVIP import *
import os
import array as buf_array

if __name__ == '__main__':
    interfaceVIP = InterfaceVIP()

    result = interfaceVIP.open("COM8", 115200)
    if result != 0:
        SystemExit(1)

    result, read_data = interfaceVIP.cmd_set_rtc()
    print(read_data)
    print(result)