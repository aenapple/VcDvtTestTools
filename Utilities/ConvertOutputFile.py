import sys
from intelhex import IntelHex

FLASH_START_ADDRESS = 0x8000000
FLASH_END_ADDRESS = 0x8080000  # 512K
QSPI_START_ADDRESS = 0x20050000
QSPI_END_ADDRESS = 0x200C0000  # 448K


if __name__ == '__main__':
    args = sys.argv[1:]
    str_file_input = args[0]
    # str_file_input = 'Debug_Ram\RND_SRC_MainCpu_v5.hex'

    ih = IntelHex()
    # ih.loadhex('Files/RND_SRC_MainCpu_v5.hex')
    ih.loadhex(str_file_input)

    #  print(ih.addresses())

    # i = ih.segments()
    # print(ih.segments())
    fileFlash = open('Files/s_flash.bin', 'wb')
    fileQspi = open('Files/s_qspi.bin', 'wb')
    flash_end_address = 0
    qspi_end_address = 0

    for x in ih.segments():
        # print(hex(x[0]))
        # print(hex(x[1]))
        if x[0] >= FLASH_START_ADDRESS and x[1] < FLASH_END_ADDRESS:
            if flash_end_address < x[1]:
                flash_end_address = x[1]
        if x[0] >= QSPI_START_ADDRESS and x[1] < QSPI_END_ADDRESS:
            if qspi_end_address < x[1]:
                qspi_end_address = x[1]

    for i in range(0, flash_end_address - FLASH_START_ADDRESS):
        k = ih[FLASH_START_ADDRESS + i]
        fileFlash.write(bytes([k]))
    fileFlash.close()

    # fileFlash = open('Files/s_flash.bin', 'rb')
    # read_data = fileFlash.read(1024)
    # fileQspi.write(read_data)
    for i in range(0, qspi_end_address - QSPI_START_ADDRESS):
        k = ih[QSPI_START_ADDRESS + i]
        fileQspi.write(bytes([k]))

    # fileFlash.close()
    fileQspi.close()

    # print(ih[0x8000000])
    # print(ih[0x8000100])
    print(hex(FLASH_START_ADDRESS))
    print(hex(flash_end_address))
    print(hex(QSPI_START_ADDRESS))
    print(hex(qspi_end_address))

