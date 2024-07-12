
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
    
    # KEY_OFFSET = 512+256

    # data = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    key  = [0x0C, 0x22, 0x38, 0x4E, 0x5A, 0x0C, 0x22, 0x38]
    
    file_name = "K2_main_v1.bin"
    
    with open(file_name, mode='rb') as file: # b is important -> binary
        binFileContent = file.read()

        lenFile = len(binFileContent)
        for data in range(0, int(lenFile/ 8), 8):
          
          dataWriteToFLASH = binFileContent[data: data + 8] 
    
          packetToFlash = []
          readHex = []
          for i in range(len(dataWriteToFLASH)):
            
            packetToFlash.append(int(dataWriteToFLASH[i]))
            readHex.append(hex(dataWriteToFLASH[i]))
          
          
              
      
          result, read_data =  bootInterfaceVIP.cmd_write_packet(TYPE_MEMORY, data, packetToFlash)
          if not (data >= 768):
            continue
          print(readHex)
          print(packetToFlash)
          print(data, len(read_data), read_data)
          print('\n')
          input()
          

    exit()
    
    for i in range(0, 768, 8):
        # address = struct.pack('>LL', i+1 )         
        result, read_data =  bootInterfaceVIP.cmd_write_packet(TYPE_MEMORY, i+KEY_OFFSET, key)
        
        # string_data = hex(read_data[0])
        # for i in range(1, len(read_data)):
        #     string_data = string_data + ", " + hex(read_data[i])
        print(len(read_data), read_data)
    
    
    FLASH_OFFSET = 0x8019000
    # exit()
    
    # for i in range(int(768/8)):
    #     # address = struct.pack('>L', i)
    #     result, read_data =  bootInterfaceVIP.cmd_read_packet(type_memory, i + OFFSET)
    #     # print(result, read_data)
    #     string_data = hex(read_data[0])
    #     for i in range(1, len(read_data)):
    #         string_data = string_data + ", " + hex(read_data[i])
    #     print(len(read_data), string_data)
        
        