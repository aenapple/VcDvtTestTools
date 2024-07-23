
from Interfaces.InterfaceVIP import InterfaceVIP
from array import array
import struct


if __name__ == '__main__':

    COMPORT = 'COM12'    
    bootInterfaceVIP = InterfaceVIP()

    result = bootInterfaceVIP.open(COMPORT, 115200)
    if result != 0:
        SystemExit(1)
        
    TYPE_MEMORY = 0x01
  
    # data = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    key  = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    
    # file_name = "BootFileCRC\\RND_SRC_Bootloader_v2_Red_flash.bin"
    file_name = "BootFileCRC\\RND_SRC_Bootloader_v2_Blue_flash.bin"
    
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
          if not (data >= 30000):
            continue
          
          print(data)
          # print(input())
          
  
          
    

    result, read_data =  bootInterfaceVIP.cmd_jump_to_application()
      
    
  
    FLASH_OFFSET = 0x8019000

        