import time
import sys
import serial



if __name__ == '__main__':
    __doc__ = """
    ....
    """
    # print(buffer)
    # print(len(buffer))
    # sys.exit(0)

    try:
        com_port = serial.Serial('COM3', 115200, timeout=0.5)
    except serial.SerialException:
        print("Serial Exception:")
        print(sys.exc_info())
        sys.exit(1)

    file_output = open("DebugOutput/debug_output.txt", 'wb')
    while True:
        time.sleep(0.2)
        # read_data = com_port.read(256)
        read_data = com_port.readline()
        len_data = len(read_data)
        if len_data == 0:  #
            continue

        # string = read_data.decode()
        # pos = string.find("\r\n")
        # string.replace("\r\n", '')
        # string.replace(string[pos + 1], '', 2)
        # print(pos)
        # print(string)
        print(read_data)
        # file_output.writelines(string)
        file_output.write(read_data)
        # file_output.writelines(read_data)
