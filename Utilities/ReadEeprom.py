
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
        sys.exit(1)

    result, read_data = interfaceVIP.read_state()
    # print(read_data)
    # print(result)
    if result != 0:
        interfaceVIP.close()
        sys.exit(2)

    str_file_output = 'Eeprom.bin'
    if os.path.exists(str_file_output):
        os.remove(str_file_output)
    file_output = open(str_file_output, 'wb')

    address = 0
    while True:
        time.sleep(0.1)

        result, read_data = interfaceVIP.cmd_read_packet(IFC_VIP_TYPE_MEMORY_EEPROM, address)
        if result != 0:
            interfaceVIP.close()
            sys.exit(3)
        # print(read_data)
        # print(result)
        packet = buf_array.array('B', [read_data[2]])
        for i in range(1, 8):
            packet.append(read_data[2 + i])

        file_output.write(packet)

        address += 8
        if address >= (0x20000 - 8):
            file_output.close()
            interfaceVIP.close()
            sys.exit(0)
