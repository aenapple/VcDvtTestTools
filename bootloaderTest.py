
from Interfaces.InterfaceVIP import InterfaceVIP
from array import array
import struct
import time
import sys
import os
import binascii
import zlib

BINFILE_PAGE_SIZE         = 256

BINFILE_ADR_IDENT         = 768
BINFILE_SIZE_IDENT        = 256 

BINFILE_ADR_VERSION       = 0
BINFILE_SIZE_VERSION      = 16

BINFILE_ADR_CRC           = BINFILE_ADR_VERSION + BINFILE_SIZE_VERSION
BINFILE_SIZE_CRC          = 4

BINFILE_ADR_SIZE_FILE     = BINFILE_ADR_CRC + BINFILE_SIZE_CRC
BINFILE_SIZE_SIZE_FILE    = 4


BINFILE_ADR_SRL_NUM       = BINFILE_ADR_SIZE_FILE +  BINFILE_SIZE_SIZE_FILE
BINFILE_SIZE_SRL_NUM      = 16


BINFILE_ADR_KEY           = BINFILE_ADR_SRL_NUM +  BINFILE_SIZE_SRL_NUM
BINFILE_SIZE_KEY          = 16


BINFILE_BUFFER_SIZE       = 256
BINFILE_CRC32_POLYNOMIAL  = 0xEDB88320

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
        
    before_ident     = file_input.read(BINFILE_ADR_IDENT)
    
    string_version   = file_input.read(BINFILE_SIZE_VERSION).decode()
    ident_file       = file_input.read(BINFILE_PAGE_SIZE - BINFILE_SIZE_VERSION)
    
    after_ident      = file_input.read(number_bytes - (BINFILE_ADR_IDENT + BINFILE_PAGE_SIZE))
    
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
    str_file_output = string_version[:-5] + '_flash_' + str_file_input.split('_')[-1][:-4] + '.bin'
    
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
    file_output.write(xs)
    
    number_bytes = os.stat(str_file_output).st_size
    
    print("Bin File Size: ", number_bytes)
    print("Hex File Size: ", hex(number_bytes))
    
    # add_number_bytes = number_bytes % 16
    # if add_number_bytes > 0:
    #     add_number_bytes = 16 - add_number_bytes
    #     for i in range(add_number_bytes):
    #         file_output.write(bytes([255]))

    file_output.close()
    
    return str_file_output
    
def BootLoaderTest(file_name):
    bootInterfaceVIP = InterfaceVIP()
    
    COMPORT = 'COM12'   
    result = bootInterfaceVIP.open(COMPORT, 115200)
    if result != 0:
        SystemExit(1)
        
    TYPE_MEMORY = 0x01
  
    # data = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    key  = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    
    # file_name = "BootFileCRC\\RND_SRC_Bootloader_v2_Red_flash.bin"
    # file_name = "LL01-BBE-01_flash.bin"
    
    with open(file_name, mode='rb') as file: # b is important -> binary
        binFileContent = file.read()

        lenFile = len(binFileContent)
        for data in range(0, lenFile, 8):
          # break 
          
          dataWriteToFLASH = binFileContent[data: data + 8] 
    
          packetToFlash = []
          readHex = []
          for i in range(len(dataWriteToFLASH)):
            
            packetToFlash.append(int(dataWriteToFLASH[i]))
            readHex.append(hex(dataWriteToFLASH[i]))
          
          result, read_data =  bootInterfaceVIP.cmd_write_packet(TYPE_MEMORY, data, packetToFlash)
          # if not (data >= 1023):
          if result:
            print(data)
            input()
          if not (data >= 50255):
            continue
          
          # print(data)
          # input()
          
          
    result, read_data =  bootInterfaceVIP.cmd_jump_to_application()
      
    
if __name__ == '__main__':
  str_file_input = 'BootFileCRC\\RND_SRC_Bootloader_v2_Blue.bin'
  # str_file_input = 'BootFileCRC\\RND_SRC_Bootloader_v2_Blank.bin'
  
  str_file_output = GenerateCRCFile(str_file_input)
  input()
  print(str_file_output)
  BootLoaderTest(str_file_output)