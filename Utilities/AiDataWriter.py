from Interfaces.InterfaceVIP import *
from array import array
import time
import sys
import os
import binascii
from tqdm import tqdm
from colorama import Fore

BINFILE_PAGE_SIZE = 256

BINFILE_ADR_IDENT = 768
BINFILE_SIZE_IDENT = 256

BINFILE_ADR_VERSION = 0
BINFILE_SIZE_VERSION = 16

BINFILE_ADR_CRC = BINFILE_ADR_VERSION + BINFILE_SIZE_VERSION
BINFILE_SIZE_CRC = 4

BINFILE_ADR_SIZE_FILE = BINFILE_ADR_CRC + BINFILE_SIZE_CRC
BINFILE_SIZE_SIZE_FILE = 4

BINFILE_ADR_SRL_NUM = BINFILE_ADR_SIZE_FILE + BINFILE_SIZE_SIZE_FILE
BINFILE_SIZE_SRL_NUM = 16

BINFILE_ADR_KEY = BINFILE_ADR_SRL_NUM + BINFILE_SIZE_SRL_NUM
BINFILE_SIZE_KEY = 16


def write_application(file_output_name, open_com_port):
    interface_vip = InterfaceVIP()

    result = interface_vip.open(open_com_port, 115200)
    if result > 0:
        print("Open COM-Port - ERROR")
        return

    waiting_time = 10  # 10 seconds
    while True:
        result, read_data = interface_vip.read_state()
        if result > 0:
            print("Communication - ERROR")
            return

        print(interface_vip.get_state_string())
        if interface_vip.get_state() == IFC_VIP_STATE_IDLE:
            break
        else:
            time.sleep(1.0)

        if waiting_time > 0:
            waiting_time -= 1
            continue
        else:
            print("Device is not in IDLE state")
            return

    file_output = open(file_output_name, 'rb')
    address = 0
    file_size = os.stat(file_output_name).st_size  # must be multiple of 16
    progress = 0
    step_progress = file_size / 100
    pbar = tqdm(desc='Uploading', total=file_size, colour='green')
    while True:
        output_data = file_output.read(8)
        result, read_data = interface_vip.cmd_write_packet(IFC_VIP_MEMORY_AI_DATA, address, output_data)
        if result > 0:
            # continue
            pbar.close()
            print("\nCommunication - ERROR")
            return

        result, read_data = interface_vip.read_state()
        if result > 0:
            pbar.close()
            print("\nCommunication - ERROR")
            return

        if interface_vip.get_state() != IFC_VIP_STATE_IDLE:
            pbar.close()
            print("\nWrite Flash - ERROR")
            return

        if file_size > 0:
            file_size -= 8

            if file_size == 0:
                pbar.close()
                print("\nWrite Flash - Ok")
                break
                # file_output.close()
                # return

            if address > progress * step_progress:
                progress += 1
                pbar.update(int(step_progress))

            address += 8

    file_output.close()
    time.sleep(0.1)


if __name__ == '__main__':
    __doc__ = """
    ....
    """

    args = sys.argv[1:]
    # str_file_output = args[0]
    str_file_output = "Files/LL01-AIP-001.000_en.bin"
    # com_port = args[1]
    com_port = "COM16"

    write_application(str_file_output, com_port)

