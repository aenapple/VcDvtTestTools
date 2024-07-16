import time
import sys
import os
import binascii
import zlib

BINFILE_PAGE_SIZE       = 256

BINFILE_ADR_IDENT       = 512
BINFILE_SIZE_IDENT      = 256 

BINFILE_ADR_VERSION     = 0
BINFILE_SIZE_VERSION    = 16

BINFILE_ADR_CRC         = BINFILE_ADR_VERSION + BINFILE_SIZE_VERSION
BINFILE_SIZE_CRC        = 4

BINFILE_ADR_SIZE_FILE   = BINFILE_ADR_CRC + BINFILE_SIZE_CRC
BINFILE_SIZE_SIZE_FILE  = 4


BINFILE_ADR_SRL_NUM     = BINFILE_ADR_SIZE_FILE +  BINFILE_SIZE_SIZE_FILE
BINFILE_SIZE_SRL_NUM    = 16


BINFILE_ADR_KEY         = BINFILE_ADR_SRL_NUM +  BINFILE_SIZE_SRL_NUM
BINFILE_SIZE_KEY        = 16


BINFILE_BUFFER_SIZE     = 256

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

        poly = 0xEDB88320  # CRC32 polynomial

        returnCrc = inputCrc
        for i in range(numberBytes):
            returnCrc = crc32_byte(returnCrc, buffer[i], poly)
            # print(returnCrc)
            # input()
            
        return returnCrc ^ 0xFFFFFFFF  # Final XOR


if __name__ == '__main__':

    str_file_input = 'K2_main_v1.bin'
    # str_file_input = 'LL01-ABE-01_flash.bin'
    
    
    file_size = os.stat(str_file_input)
    # print("Size of file :", file_size.st_size, "bytes")
    
    
    # -----------------------  CALCULATE CRC  --------------------------------------   
    
    number_bytes = file_size.st_size                # Full file size in decimal 
    hex_number_bytes = hex(number_bytes)            # Full file size in hex 
    if number_bytes < (BINFILE_PAGE_SIZE * 10):
        print("File - small size!")
        sys.exit(1)

    file_input = open(str_file_input, 'rb')
        
    before_ident     = file_input.read(BINFILE_ADR_IDENT)
    
    string_version   = file_input.read(BINFILE_SIZE_VERSION).decode()
    ident_file       = file_input.read(BINFILE_PAGE_SIZE - BINFILE_SIZE_VERSION)
    
    after_ident      = file_input.read(number_bytes - (BINFILE_ADR_IDENT + BINFILE_PAGE_SIZE))
    
    file_input.close()
    # print(before_ident)
    # print(string_version)
    # print(ident_file)
    # print(after_ident)
    print(number_bytes)
    
    
    crc = 0xFFFFFFFF
    file_input = open(str_file_input, 'rb')
    
    tmp_number_bytes = number_bytes
    counterBlocks = int(number_bytes / BINFILE_BUFFER_SIZE)    
    for i in range(counterBlocks):
        buffer = file_input.read(BINFILE_BUFFER_SIZE)        
        if i != 2:
            crc = calculate_crc32(crc, buffer, BINFILE_BUFFER_SIZE)
            print(hex(crc))
        
        tmp_number_bytes -= BINFILE_BUFFER_SIZE
    
    print(crc)
    buffer = file_input.read(tmp_number_bytes)        
    crc = calculate_crc32(crc, buffer, tmp_number_bytes)
    file_input.close()
    
    print(crc)
    hex_crc = hex(crc)
    
    print("CRC\t\t", crc)
    print("CRC Hex:\t", hex_crc)


    file_size = os.stat(str_file_input)                     
    str_file_output = string_version[:-5] + '_flash' + '.bin'
    
    file_output = open(str_file_output, 'wb')
    
    serial_number  = "LL01-00000000001" 
    encryption_key = "SAMPLEKEY1234567" # ?????
    
    
    # --------------------------  BIN START  --------------------------------------   
    file_output.write( before_ident)
    
    # ------------------------- START IDENT FILE  ---------------------------------------
    file_output.write( string_version.encode())
    file_output.write((crc          & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_CRC, byteorder="little"))
    file_output.write((number_bytes & 0xFFFFFFFF).to_bytes(BINFILE_SIZE_SIZE_FILE, byteorder="little"))
    file_output.write( serial_number.encode())
    # file_output.write((encryption_key     & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF).to_bytes(BINFILE_SIZE_KEY, byteorder="little"))
    file_output.write(encryption_key.encode())
    
    #  Fill in remaining bytes in Ident File
    for k in range(BINFILE_SIZE_IDENT - (BINFILE_ADR_KEY + BINFILE_SIZE_KEY)):
        file_output.write(bytes([255]))

    # ------------------------- END IDENT FILE  ---------------------------------------
    
    file_output.write(after_ident)
    
    number_bytes = os.stat(str_file_output).st_size
    
    print("Bin File Size: ", number_bytes)
    print("Hex File Size: ", hex(number_bytes))
    
    add_number_bytes = number_bytes % 8
    if add_number_bytes > 0:
        add_number_bytes = 8 - add_number_bytes
        for i in range(add_number_bytes):
            file_output.write(bytes([255]))

    file_output.close()
    
    
    
    
    


