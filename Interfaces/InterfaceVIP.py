import serial
import sys
import array as buf_array
import time
import struct
from datetime import datetime

INTERFACE_VIP_SIZE_PACKET = 16
INTERFACE_VIP_INDEX_COMMAND = 0  # command 1 byte
INTERFACE_VIP_INDEX_STATE = (INTERFACE_VIP_INDEX_COMMAND + 1)  # state - 1 byte
INTERFACE_VIP_INDEX_ERROR = (INTERFACE_VIP_INDEX_STATE + 1)  # error - 1 byte
INTERFACE_VIP_INDEX_SUB_STATE = (INTERFACE_VIP_INDEX_ERROR + 1)  # sub-state - 1 byte
INTERFACE_VIP_INDEX_MOTOR_STATES = (INTERFACE_VIP_INDEX_SUB_STATE + 1)  # motor states - 1 byte
INTERFACE_VIP_INDEX_SENSOR_STATES = (INTERFACE_VIP_INDEX_MOTOR_STATES + 1)  # sensor states - 2 bytes
INTERFACE_VIP_INDEX_AC_CURRENT = (INTERFACE_VIP_INDEX_SENSOR_STATES + 2)  # AC current - 2 bytes
INTERFACE_VIP_INDEX_LAMP_STATES = (INTERFACE_VIP_INDEX_AC_CURRENT + 2)  # lamp states - 1 byte
INTERFACE_VIP_INDEX_TANK_LEVEL = (INTERFACE_VIP_INDEX_LAMP_STATES + 1)  # tank level - 1 byte
INTERFACE_VIP_INDEX_LEFT_LEVEL = (INTERFACE_VIP_INDEX_TANK_LEVEL + 1)  # chamber left level - 1 byte
INTERFACE_VIP_INDEX_RIGHT_LEVEL = (INTERFACE_VIP_INDEX_LEFT_LEVEL + 1)  # chamber right level - 1 byte
INTERFACE_VIP_INDEX_HEATER_STATES = (INTERFACE_VIP_INDEX_RIGHT_LEVEL + 2)  # heater states - 1 byte

INTERFACE_VIP_INDEX_COMPONENT = (INTERFACE_VIP_INDEX_COMMAND + 1)
INTERFACE_VIP_INDEX_TEST_RESULT = (INTERFACE_VIP_INDEX_COMPONENT + 1)

IFC_VIP_COMMAND_GET_STATE = 0x00
IFC_VIP_COMMAND_GET_BME688_1 = 0x01
IFC_VIP_COMMAND_GET_BME688_2 = 0x02
IFC_VIP_COMMAND_SET_FAN_SPEED = 0x03
IFC_VIP_COMMAND_GET_FAN_SPEED = 0x04
IFC_VIP_COMMAND_GET_ADC_CHANNEL = 0x05
IFC_VIP_COMMAND_GET_AC_PARAMETERS = 0x06
IFC_VIP_COMMAND_GET_TEMPERATURE = 0x07
IFC_VIP_COMMAND_SET_HEATER_PARAMETERS = 0x08
IFC_VIP_COMMAND_SET_MOTOR_PARAMETERS = 0x09
IFC_VIP_COMMAND_GET_MOTOR_PARAMETERS = 0x0C
IFC_VIP_COMMAND_GET_GAS_SENSOR = 0x0B
IFC_VIP_COMMAND_GET_MOTOR_PARAMETERS = 0x0C
IFC_VIP_COMMAND_GET_LAMP_PARAMETERS = 0x0D
IFC_VIP_COMMAND_GET_HEATER_PARAMETERS = 0x0E
IFC_VIP_COMMAND_START_TEST = 0x0F
IFC_VIP_COMMAND_CONTINUE_PROCESS = 0x10
IFC_VIP_COMMAND_STOP_PROCESS = 0x11
IFC_VIP_COMMAND_START_PROCESS = 0x12
IFC_VIP_COMMAND_WRITE_BYTE = 0x13
IFC_VIP_COMMAND_READ_BYTE = 0x14
IFC_VIP_COMMAND_WRITE_PACKET = 0x15
IFC_VIP_COMMAND_READ_PACKET = 0x16
IFC_VIP_COMMAND_JUMP_APPLICATION = 0x17
IFC_VIP_COMMAND_RESET = 0x18
IFC_VIP_COMMAND_CONTROL_LAMP = 0x19
IFC_VIP_COMMAND_GET_STATE_LAMP = 0x1A
IFC_VIP_COMMAND_CONTROL_MOTOR = 0x1B
IFC_VIP_COMMAND_GET_STATE_MOTOR = 0x1C
IFC_VIP_COMMAND_CONTROL_HEATER = 0x1D
IFC_VIP_COMMAND_GET_STATE_HEATER = 0x1E
IFC_VIP_COMMAND_SET_POSITION = 0x1F
IFC_VIP_COMMAND_GET_LEVEL_SENSOR = 0x20
IFC_VIP_COMMAND_GET_RESULT_TEST = 0x21
IFC_VIP_COMMAND_GET_POSITION = 0x22
IFC_VIP_COMMAND_SET_RTC = 0x23
IFC_VIP_COMMAND_GET_RTC = 0x24
IFC_VIP_COMMAND_NACK = 0xFF

IFC_VIP_STATE_NO_STATE = 0x00
IFC_VIP_STATE_SELF_TEST = 0x01
IFC_VIP_STATE_IDLE = 0x02
IFC_VIP_STATE_PROCESS_CH1 = 0x03
IFC_VIP_STATE_PROCESS_CH2 = 0x04
IFC_VIP_STATE_INIT = 0x05
IFC_VIP_STATE_MESOPHILIC_PHASE = 0x06
IFC_VIP_STATE_THERMOPHILIC_PHASE = 0x07
IFC_VIP_STATE_COOLING_PHASE = 0x08
IFC_VIP_STATE_BUSY = 0x09
IFC_VIP_STATE_PHASE_0 = 0x0A
IFC_VIP_STATE_PHASE_1 = 0x0B
IFC_VIP_STATE_PHASE_2 = 0x0C
IFC_VIP_STATE_TOP_REMOVED = 0x0D
IFC_VIP_STATE_LID_OPEN = 0x0E
IFC_VIP_STATE_GRINDING = 0x0F
IFC_VIP_STATE_TANK_FULL = 0x10
IFC_VIP_STATE_ERROR = 0xFF

IFC_VIP_SUB_STATE_APPLICATION = 0x00
IFC_VIP_SUB_STATE_BOOTLOADER = 0x01

IFC_VIP_ERROR_MAIN_MOTOR = 0x00
IFC_VIP_ERROR_MOTOR_CHAMBER_1 = 0x01
IFC_VIP_ERROR_MOTOR_CHAMBER_2 = 0x02
IFC_VIP_ERROR_LAMP_1 = 0x03
IFC_VIP_ERROR_LAMP_2 = 0x04
IFC_VIP_ERROR_MAIN_FAN = 0x05
IFC_VIP_ERROR_PAD_HEATER_1 = 0x06
IFC_VIP_ERROR_PAD_HEATER_2 = 0x07
IFC_VIP_ERROR_I2C_1 = 0x08
IFC_VIP_ERROR_I2C_2 = 0x09
IFC_VIP_ERROR_UART = 0x0A
IFC_VIP_ERROR_APPLICATION = 0x0B
IFC_VIP_ERROR_APPLICATION_NONE = 0x0C
IFC_VIP_ERROR_INTERFACE_MASTER_VIP = 0x0D
IFC_VIP_ERROR_INTERFACE_SLAVE_VIP = 0x0E
IFC_VIP_ERROR_CRITICAL_GAS_LEVEL = 0x0F
IFC_VIP_ERROR_PTC_HEATER_1 = 0x10
IFC_VIP_ERROR_PTC_HEATER_2 = 0x11
IFC_VIP_ERROR_AC_MAIN_NOT_PRESENT = 0x12
IFC_VIP_ERROR_REMOVED_CHAMBER_1 = 0x13
IFC_VIP_ERROR_REMOVED_CHAMBER_2 = 0x14
IFC_VIP_ERROR_REMOVED_TANK = 0x15
IFC_VIP_ERROR_DAM_MOTOR = 0x16

IFC_VIP_COMPONENT_ALL = 0x00
IFC_VIP_COMPONENT_LAMP_1 = 0x01
IFC_VIP_COMPONENT_LAMP_2 = 0x02
IFC_VIP_COMPONENT_MOTOR_CHAMBER_1 = 0x03
IFC_VIP_COMPONENT_MOTOR_CHAMBER_2 = 0x04
IFC_VIP_COMPONENT_MAIN_MOTOR = 0x05
IFC_VIP_COMPONENT_PAD_HEATER_1 = 0x06
IFC_VIP_COMPONENT_PAD_HEATER_2 = 0x07
IFC_VIP_COMPONENT_PTC_HEATER_1 = 0x08
IFC_VIP_COMPONENT_PTC_HEATER_2 = 0x09
IFC_VIP_COMPONENT_MAIN_FAN = 0x0A
IFC_VIP_COMPONENT_DAM_MECHANISM = 0x0B

IFC_VIP_T_PAD_HEATER_LEFT = 0x01
IFC_VIP_T_PAD_HEATER_RIGHT = 0x02
IFC_VIP_T_PTC_HEATER_LEFT = 0x05
IFC_VIP_T_PTC_HEATER_RIGHT = 0x06
IFC_VIP_T_CPU_NETWORK = 0x03
IFC_VIP_T_CPU_MAIN = 0x04
IFC_VIP_T_CPU_TOP = 0x0B

IFC_VIP_TEST_RESULT_OK = 0x00
IFC_VIP_TEST_RESULT_PROCESS = 0x01
IFC_VIP_TEST_RESULT_ERROR = 0xFF

IFC_VIP_TYPE_MEMORY_FLASH_CPU1 = 0x00
IFC_VIP_TYPE_MEMORY_FLASH_CPU2 = 0x02
IFC_VIP_TYPE_MEMORY_EEPROM = 0x03


class InterfaceVIP:
    def __init__(self):
        self.ComPort = None
        self.command = IFC_VIP_COMMAND_GET_STATE
        self.state = IFC_VIP_STATE_NO_STATE
        self.error = IFC_VIP_ERROR_MAIN_MOTOR
        self.subState = IFC_VIP_SUB_STATE_BOOTLOADER
        self.motorStates = 0x00
        self.sensorStates = 0x0000
        self.acCurrent = 0
        self.lampStates = 0x00
        self.tankLevel = 0
        self.chamberLeftLevel = 0
        self.chamberRightLevel = 0
        self.heaterStates = 0

    def get_null_packet(self):
        return self.get_component_packet(0)
        """ packet = buf_array.array('B', b'\x00')
        for i in range(1, INTERFACE_VIP_SIZE_PACKET - 2):
            packet.append(0)
        return packet """

    def get_component_packet(self, component):
        packet = buf_array.array('B', [component])
        for i in range(1, INTERFACE_VIP_SIZE_PACKET - 2):
            packet.append(0)
        return packet

    def read_state(self):
        write_data = self.get_null_packet()
        read_result, read_data = self.read_module(IFC_VIP_COMMAND_GET_STATE, write_data)
        if read_result != 0:
            return read_result, read_data

        # Unpack the packet
        # < indicates little-endian
        # b = signed char (1 byte)
        # H = unsigned short (2 bytes)
        # I = unsigned int (4 bytes)
        # x = pad byte (skips the unused byte)
        self.state, self.error, self.subState, self.motorStates, self.sensorStates, self.acCurrent, \
        self.lampStates, self.tankLevel, self.chamberLeftLevel, self.chamberRightLevel, self.heaterStates = \
            struct.unpack('<xbbbbHHbbbbbxx', read_data)

        return 0, read_data

    def cmd_write_packet(self, type_memory, address, packet):
        write_data = buf_array.array('B', [type_memory])
        write_data.append(address & 0xFF)
        write_data.append((address >> 8) & 0xFF)
        write_data.append((address >> 16) & 0xFF)
        write_data.append((address >> 24) & 0xFF)
        for i in range(8):
            write_data.append(packet[i])

        read_result, read_data = self.read_module(IFC_VIP_COMMAND_WRITE_PACKET, write_data)
        if read_result != 0:
            return read_result, read_data

        return 0, read_data

    def cmd_read_packet(self, type_memory, address):
        write_data = buf_array.array('B', [type_memory])
        write_data.append(address & 0xFF)
        write_data.append((address >> 8) & 0xFF)
        write_data.append((address >> 16) & 0xFF)
        write_data.append((address >> 24) & 0xFF)

        read_result, read_data = self.read_module(IFC_VIP_COMMAND_READ_PACKET, write_data)
        if read_result != 0:
            return read_result, read_data

        return 0, read_data


    def cmd_set_rtc(self):
        date_now = datetime.now()
        temp_bcd = self.int_to_bcd(date_now.second)
        write_data = buf_array.array('B', [temp_bcd])
        temp_bcd = self.int_to_bcd(date_now.minute)
        write_data.append(temp_bcd)
        temp_bcd = self.int_to_bcd(date_now.hour)
        write_data.append(temp_bcd)
        temp_bcd = self.int_to_bcd(date_now.isoweekday())
        write_data.append(temp_bcd)
        temp_bcd = self.int_to_bcd(date_now.day)
        write_data.append(temp_bcd)
        temp_bcd = self.int_to_bcd(date_now.month)
        write_data.append(temp_bcd)
        temp_bcd = self.int_to_bcd(date_now.year - 2000)
        write_data.append(temp_bcd)
        for i in range(7, INTERFACE_VIP_SIZE_PACKET - 2):
            write_data.append(0)

        read_result, read_data = self.read_module(IFC_VIP_COMMAND_SET_RTC, write_data)
        if read_result != 0:
            return read_result, read_data

        return 0, read_data

    def cmd_get_rtc(self):
        write_data = self.get_null_packet()
        read_result, read_data = self.read_module(IFC_VIP_COMMAND_GET_RTC, write_data)
        if read_result != 0:
            return read_result, read_data

        return 0, read_data

    def cmd_test(self, component):
        write_data = buf_array.array('B', [component])
        for i in range(1, INTERFACE_VIP_SIZE_PACKET - 2):
            write_data.append(0)

        read_result, read_data = self.read_module(IFC_VIP_COMMAND_START_TEST, write_data)
        if read_result != 0:
            return read_result, read_data
        #  DEBUG
        #  return 0, read_data
        #  DEBUG

        timeout = 10.0  # 10 Sec
        while True:
            read_result, read_data = self.read_module(IFC_VIP_COMMAND_GET_RESULT_TEST, write_data)
            if read_result != 0:
                return read_result, read_data

            # print(read_data)

            if read_data[INTERFACE_VIP_INDEX_TEST_RESULT] != IFC_VIP_TEST_RESULT_PROCESS:
                break

            time.sleep(0.1)
            timeout -= 0.1
            if timeout == 0:
                return 2, read_data  # timeout

        # return - IFC_VIP_TEST_RESULT_OK or IFC_VIP_TEST_RESULT_ERROR
        return read_data[INTERFACE_VIP_INDEX_TEST_RESULT], read_data

    def get_temperature(self, num_sensor):
        pass

    def get_bme688(self, num_sensor, part):
        pass

    def get_state(self):
        return self.state

    def close(self):
        if self.ComPort is None:
            return
        self.ComPort.close()
        self.ComPort = None

    def open(self, com_port, baud_rate):
        try:
            self.ComPort = serial.Serial(com_port, baud_rate, timeout=0.5)
        except serial.SerialException:
            print("Serial Exception:")
            print(sys.exc_info())
            return 1

        return 0

    def read_module(self, command, write_data):
        if self.ComPort is None:
            print("COM Port is not open!")
            return 1, None

        self.send_data(command, write_data)  # send command and data to module
        # time.sleep(0.1)
        read_data = self.ComPort.read(INTERFACE_VIP_SIZE_PACKET)
        len_data = len(read_data)
        if len_data == 0:  #
            return 1, read_data  # 'No answer'

        self.command = read_data[INTERFACE_VIP_INDEX_COMMAND]

        # DEBUG
        # print(read_data)
        # return 0, read_data
        # DEBUG

        if self.command == IFC_VIP_COMMAND_NACK:
            return IFC_VIP_COMMAND_NACK, read_data

        return 0, read_data  # 'OK'

    def send_data(self, command, data):
        buffer = buf_array.array('B', [command])
        # buffer.append(current & 0xFF)
        # buffer.append(current >> 8)
        for i in range(INTERFACE_VIP_SIZE_PACKET - 2):
            buffer.append(data[i])
        buffer.append(self.calc_crc8(buffer, INTERFACE_VIP_SIZE_PACKET - 1))
        self.ComPort.write(buffer)  # send command to module

    def calc_crc8(self, buffer, num_bytes):
        crc = 0
        for i in range(num_bytes):
            crc += buffer[i]
        crc += 1
        return crc

    def bcd_to_int(self, n):
        return int(('%x' % n), base=10)

    def int_to_bcd(self, n):
        return int(str(n), base=16)


if __name__ == '__main__':
    interfaceVIP = InterfaceVIP()

    result = interfaceVIP.open("COM8", 115200)
    if result != 0:
        SystemExit(1)

    result, read_data = interfaceVIP.cmd_set_rtc()
    print(read_data)
    print(result)

    while True:
        # result, data = interfaceVIP.cmd_test(IFC_VIP_COMPONENT_LAMP_1)
        # print("Lamp1")
        # print(result)

        time.sleep(1.0)

        result, read_data = interfaceVIP.read_state()
        print(read_data)
        print(result)

        time.sleep(1.0)
