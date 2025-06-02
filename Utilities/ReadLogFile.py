
# from Interfaces import InterfaceVIP
import sys
import time
from Interfaces.InterfaceVIP import *
import os
import array as buf_array

if __name__ == '__main__':
    interfaceVIP = InterfaceVIP()

    result = interfaceVIP.open("COM23", 115200)
    if result != 0:
        sys.exit(1)

    result, read_data = interfaceVIP.read_state()
    # print(read_data)
    # print(result)
    if result != 0:
        interfaceVIP.close()
        sys.exit(2)

    str_file_output = 'Files/LogFile.txt'
    if os.path.exists(str_file_output):
        os.remove(str_file_output)
    file_output = open(str_file_output, 'w')

    for index_record in range(IFC_VIP_LOG_SIZE):
        # time.sleep(0.1)

        result, read_data = interfaceVIP.cmd_read_log(index_record)
        if result != 0:
            file_output.close()
            interfaceVIP.close()
            sys.exit(3)
        # print(read_data)
        # print(result)
        log_record = interfaceVIP.get_log_record()

        file_output.write(log_record)

    file_output.close()