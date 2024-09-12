import sys
import os
import binascii
import time
import zlib
import secrets
import array as buf_array

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

ENCRYPTION_ADDRESS_KEY = BINFILE_ADR_IDENT + BINFILE_ADR_KEY

ENCRYPTION_GC2_ROUNDS = 2
ENCRYPTION_GC2_BLOCK_LEN = 8


class Encryption:
    def __init__(self):
        self.encryption_cbc = bytearray(8)
        self.encryption_key = bytearray(8)

    def gc2_barrel_right(self, x):
        x = x & 0xFF
        x1 = (x >> 3) & 0xFF
        x2 = (x << 5) & 0xFF
        return x1 | x2

    def gc2_barrel_left(self, x):
        x = x & 0xFF
        x1 = (x << 3) & 0xFF
        x2 = (x >> 5) & 0xFF
        return x1 | x2

    def gc2_init(self, key):
        str_cbc = bytearray('VCycene!', 'utf-8')
        for i in range(ENCRYPTION_GC2_BLOCK_LEN):
            self.encryption_key[i] = (key[i] ^ key[i + 8]) & 0xFF

        for i in range(ENCRYPTION_GC2_BLOCK_LEN):
            self.encryption_cbc[i] = 0
            for k in range(ENCRYPTION_GC2_BLOCK_LEN):
                self.encryption_cbc[i] = self.encryption_cbc[i] ^ str_cbc[k]
                self.encryption_cbc[i] = self.gc2_barrel_left(self.encryption_cbc[i])
                self.encryption_cbc[i] = (self.encryption_cbc[i] + self.encryption_key[i]) & 0xFF

    def gc2_encode(self, input_data):
        output_data = bytearray(8)
        for i in range(ENCRYPTION_GC2_BLOCK_LEN):
            self.encryption_cbc[i] = input_data[i] ^ self.encryption_cbc[i]
            for k in range(ENCRYPTION_GC2_ROUNDS):
                self.encryption_cbc[i] = (self.gc2_barrel_left(self.encryption_cbc[i]) + self.encryption_key[i]) & 0xFF

        for i in range(8):
            output_data[i] = self.encryption_cbc[i]

        return output_data

    def gc2_decode(self, input_data):
        output_data = bytearray(8)
        for i in range(ENCRYPTION_GC2_BLOCK_LEN):
            output_data[i] = input_data[i]
            for k in range(ENCRYPTION_GC2_ROUNDS):
                output_data[i] = (output_data[i] - self.encryption_key[i]) & 0xFF
                output_data[i] = self.gc2_barrel_right(output_data[i])

            output_data[i] = output_data[i] ^ self.encryption_cbc[i]
            self.encryption_cbc[i] = input_data[i]

        return output_data

    def debug_encoder(self):
        input_buffer = bytearray(8)
        default_key = [0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x04, 0x94, 0x04, 0x94, 0x04, 0x94, 0x04, 0x94]
        # default_cbc = [0x04, 0x94, 0x04, 0x94, 0x04, 0x94, 0x04, 0x94]

        for i in range(8):
            input_buffer[i] = i + 10

        self.gc2_init(bytearray(default_key))
        temp_encryption_cbc = self.gc2_encode(input_buffer)
        print(binascii.hexlify(temp_encryption_cbc))

        self.gc2_init(bytearray(default_key))
        output_data = self.gc2_decode(temp_encryption_cbc)
        print(binascii.hexlify(output_data))

    def file_encoder(self, file_input_name, key):
        self.gc2_init(key)

        print("encryptionCbc:")
        print(binascii.hexlify(self.encryption_cbc))
        print("encryptionKey:")
        print(binascii.hexlify(self.encryption_key))

        file_input = open(file_input_name, 'rb')
        file_output_name = file_input.name[:-4] + '_en' + '.bin'
        file_output = open(file_output_name, 'wb')

        file_size = os.stat(file_input_name).st_size  # must be multiple of 16
        read_bytes = 0
        write_key = bytearray(8)
        while True:
            read_file_data = file_input.read(8)

            if read_bytes == ENCRYPTION_ADDRESS_KEY:
                for i in range(8):
                    write_key[i] = key[i]
                file_output.write(bytearray(write_key))
            elif read_bytes == (ENCRYPTION_ADDRESS_KEY + 8):
                for i in range(8):
                    write_key[i] = key[i + 8]
                file_output.write(bytearray(write_key))
            else:
                self.gc2_encode(read_file_data)
                file_output.write(bytearray(self.encryption_cbc))

            read_bytes = read_bytes + 8
            file_size = file_size - 8
            if file_size == 0:
                break

        file_input.close()
        file_output.close()

        # DEBUG
        self.gc2_init(key)

        print("encryptionCbc:")
        print(binascii.hexlify(bytearray(self.encryption_cbc)))
        print("encryptionKey:")
        print(binascii.hexlify(bytearray(self.encryption_key)))

        file_input = open(file_output_name, 'rb')
        file_output = open('DecodedFile.bin', 'wb')

        file_size = os.stat(file_output_name).st_size
        read_bytes = 0
        while True:
            read_file_data = file_input.read(8)

            if read_bytes == ENCRYPTION_ADDRESS_KEY or read_bytes == (ENCRYPTION_ADDRESS_KEY + 8):
                file_output.write(bytearray(read_file_data))
            else:
                output_data = self.gc2_decode(read_file_data)
                file_output.write(bytearray(output_data))

            read_bytes = read_bytes + 8
            file_size = file_size - 8
            if file_size == 0:
                break

        file_input.close()
        file_output.close()
        # DEBUG

    def debug_file_encoder(self, file_name):
        file_input = open(file_name, 'rb')

        file_size = os.stat(file_name).st_size
        address = 0
        temp_buffer = bytearray(1024)
        while True:
            input_data = file_input.read(8)

            for i in range(8):
                temp_buffer[address + i] = input_data[i]

            if address == (1024 - 8):
                key = bytearray(16)
                for i in range(16):
                    key[i] = temp_buffer[BINFILE_ADR_IDENT + BINFILE_ADR_KEY + i]
                """ self.gc2_init(key)
                read_file_data = bytearray(8)
                for i in range(8):
                    read_file_data[i] = temp_buffer[i]
                output_data = self.gc2_decode(read_file_data)
                print(bytearray(output_data)) """
                break

            address += 8

        file_input.close()

        time.sleep(1)
        file_input = open(file_name, 'rb')
        input_data = file_input.read(8)
        self.gc2_init(key)
        output_data = self.gc2_decode(input_data)
        print(bytearray(output_data))

if __name__ == '__main__':
    __doc__ = """
    ....
    """

    args = sys.argv[1:]
    str_file_output = args[0]
    # str_file_output = 'LL01-AMB-001.00B.bin'
    # str_file_output = 'LL01-AMB-001.000_en.bin'

    secrets_key = secrets.token_bytes(16)
    print(secrets_key.hex())

    encryption = Encryption()

    encryption.file_encoder(str_file_output, secrets_key)
    # encryption.debug_encoder()
    # encryption.debug_file_encoder(str_file_output)
