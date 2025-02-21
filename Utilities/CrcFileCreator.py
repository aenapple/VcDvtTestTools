import sys
import os

BINFILE_PAGE_SIZE = 256

BINFILE_ADR_IDENT = 768
BINFILE_SIZE_IDENT = 256

BINFILE_ADR_VERSION = 0
BINFILE_SIZE_VERSION = 16

BINFILE_ADR_CRC = BINFILE_ADR_VERSION + BINFILE_SIZE_VERSION
BINFILE_SIZE_CRC = 4

BINFILE_ADR_SIZE_FILE = BINFILE_ADR_CRC + BINFILE_SIZE_CRC
BINFILE_SIZE_SIZE_FILE = 4

BINFILE_ADR_RESERVED = BINFILE_ADR_SIZE_FILE + BINFILE_SIZE_SIZE_FILE
BINFILE_SIZE_RESERVED = 16

BINFILE_ADR_KEY = BINFILE_ADR_RESERVED + BINFILE_SIZE_RESERVED
BINFILE_SIZE_KEY = 16

BINFILE_BUFFER_SIZE = 256
BINFILE_CRC32_POLYNOMIAL = 0xEDB88320


def crc32_byte(input_crc: int, data: int, poly: int) -> int:
        return_crc = input_crc
        cur_byte = data
        for _ in range(8):
            if (return_crc & 0x00000001) ^ (cur_byte & 0x01):
                return_crc = (return_crc >> 1) ^ poly
            else:
                return_crc >>= 1
            cur_byte >>= 1
            
        # print(hex(return_crc), return_crc)
        # input()
        return return_crc


def calculate_crc32(inputCrc, buffer, numberBytes) -> int:
        returnCrc = inputCrc
        for i in range(numberBytes):
            returnCrc = crc32_byte(returnCrc, buffer[i], BINFILE_CRC32_POLYNOMIAL)
            # print(returnCrc)
            # input()
            
        return returnCrc ^ 0xFFFFFFFF  # Final XOR


def GenerateCRCFile(str_file_input):
    # -----------------------  CALCULATE CRC  --------------------------------------
    file_size = os.stat(str_file_input)
    number_bytes = file_size.st_size                # Full file size in decimal 
    if number_bytes < (BINFILE_PAGE_SIZE * 10):
        print("File - small size!")
        sys.exit(1)

    file_input = open(str_file_input, 'rb')
        
    before_ident = file_input.read(BINFILE_ADR_IDENT)
    
    string_version = file_input.read(BINFILE_SIZE_VERSION).decode()
    ident_file = file_input.read(BINFILE_PAGE_SIZE - BINFILE_SIZE_VERSION)
    
    after_ident = file_input.read(number_bytes - (BINFILE_ADR_IDENT + BINFILE_PAGE_SIZE))
    
    file_input.close()
    # print(before_ident)
    print(string_version)
    # print(ident_file)
    # print(after_ident)
    # print(number_bytes)

    crc = 0xFFFFFFFF
    file_input = open(str_file_input, 'rb')
    
    tmp_number_bytes = number_bytes
    counterBlocks = int(number_bytes / BINFILE_BUFFER_SIZE)    
    for i in range(counterBlocks):
        buffer = file_input.read(BINFILE_BUFFER_SIZE)        
        if i != 3:
            crc = calculate_crc32(crc, buffer, BINFILE_BUFFER_SIZE)
        # print(hex(crc))
        # print(buffer)
        # input()

        tmp_number_bytes -= BINFILE_BUFFER_SIZE
        # print(tmp_number_bytes)

    buffer = file_input.read(tmp_number_bytes)   
    add_number_bytes = number_bytes % 16
    xs = b''
    if add_number_bytes > 0:
        add_number_bytes = 16 - add_number_bytes
        for i in range(add_number_bytes):
            xs += bytes([255])
    
    buffer += xs
    tmp_number_bytes += add_number_bytes
    print(hex(crc))
    crc = calculate_crc32(crc, buffer, tmp_number_bytes)    
    file_input.close()
    
    print("CRC\t\t",        crc)
    print("CRC Hex:\t", hex(crc))

    number_bytes += add_number_bytes  

    print(string_version)             
    str_file_output = 'Files/' + string_version + '.bin'
    
    file_output = open(str_file_output, 'wb')
    reserved = "0000000000000000"
    encryption_key = "0000000000000000"

    # --------------------------  BIN START  --------------------------------------   
    file_output.write(before_ident)
    
    # ------------------------- START IDENT FILE  ---------------------------------------
    file_output.write(string_version.encode())
    file_output.write((crc & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_CRC, byteorder="little"))
    file_output.write((number_bytes & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_SIZE_FILE, byteorder="little"))
    file_output.write(reserved.encode())
    file_output.write(encryption_key.encode())

    file_ident = open('ident.bin', 'wb')
    file_ident.write(string_version.encode())
    file_ident.write((crc & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_CRC, byteorder="little"))
    file_ident.write((number_bytes & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_SIZE_FILE, byteorder="little"))
    file_ident.close()
    
    #  Fill in remaining bytes in Ident File
    for k in range(BINFILE_SIZE_IDENT - (BINFILE_ADR_KEY + BINFILE_SIZE_KEY)):
        file_output.write(bytes([255]))

    # ------------------------- END IDENT FILE  ---------------------------------------

    file_output.write(after_ident)
    file_output.write(xs)
    
    number_bytes = os.stat(str_file_output).st_size
    
    print("Bin File Size: ", number_bytes)
    print("Hex File Size: ", hex(number_bytes))
    
    file_output.close()
    
    return str_file_output


if __name__ == '__main__':
    __doc__ = """
    ....
    """

    args = sys.argv[1:]
    # str_file_input = args[0]
    str_file_input = 'Files/s_qspi.bin'

    str_file_output = GenerateCRCFile(str_file_input)
    print(str_file_output)
