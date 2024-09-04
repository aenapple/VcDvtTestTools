import sys
import os
import binascii
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

BINFILE_BUFFER_SIZE = 256
BINFILE_CRC32_POLYNOMIAL = 0xEDB88320

ENCRYPTION_ADDRESS_KEY = BINFILE_ADR_KEY

ENCRYPTION_GC2_ROUNDS = 2
ENCRYPTION_GC2_BLOCK_LEN = 8

""" ////// barrel shifters. //////
#define ENCRYPTION_GC2_BARREL_R(x)  (((x) >> 3) | ((x) << 5))
#define ENCRYPTION_GC2_BARREL_L(x)  (((x) << 3) | ((x) >> 5)) """

"""
// ----------------------------------------------------------------------------------
/ **
* The function - Encodes 8 bytes of data.
*
* Parameter:
* pInput input data (plain)
* pCBCInDataOut at input holds the previous encryption buffer
* at output holds the encrypted pInput
*
* @ return void.
* /
void TEncryption::GC2Encode(INT8U * pInput)
{
    INT8U i;
    INT8U j;

    for (i=0; i < ENCRYPTION_GC2_BLOCK_LEN; i++)
    {
        this->cbc[i] = pInput[i] ^ this->cbc[i];
        for (j=0; j < ENCRYPTION_GC2_ROUNDS; j++)
            this->cbc[i] = ENCRYPTION_GC2_BARREL_L(this->cbc[i]) + this->key[i];
    }

}
// --- end GC2Encode ----------------------------------------------------------------

// ----------------------------------------------------------------------------------
/ **
* The function - Decodes 8 bytes of data.
*
* Parameter:
* pInput input data(cipher)
* pOutput receives plain data
* pCBC pointer to the CBC context.
*
* @ return void.
* /
void TEncryption::GC2Decode(INT8U * pInput, INT8U * pOutput)
{
    INT8U i;
    INT8U j;

    for (i=0; i < ENCRYPTION_GC2_BLOCK_LEN; i++)
    {
        pOutput[i] = pInput[i];
        for (j=0; j < ENCRYPTION_GC2_ROUNDS; j++)
        {
            pOutput[i] -= this->key[i];
            pOutput[i] = ENCRYPTION_GC2_BARREL_R(pOutput[i]);
        }

        pOutput[i] = pOutput[i] ^ this->cbc[i];
        this->cbc[i] = pInput[i];

    }

}
// --- end GC2Decode ----------------------------------------------------------------
"""


def gc2_barrel_right(x):
    x1 = (x >> 3) & 0xFF
    x2 = (x << 5) & 0xFF
    return x1 | x2


def gc2_barrel_left(x):
    x1 = (x << 3) & 0xFF
    x2 = (x >> 5) & 0xFF
    return x1 | x2


def file_encoder(file_name, key):
    encryption_cbc = buf_array.array('B')
    encryption_key = buf_array.array('B')
    for i in range(8):
        encryption_cbc.append(key[i])
        encryption_key.append(key[i + 8])

    print("encryptionCbc:")
    print(binascii.hexlify(encryption_cbc))
    print("encryptionKey:")
    print(binascii.hexlify(encryption_key))

    file_input = open(file_name, 'rb')
    read_bytes = 0
    while True:
        read_file_data = file_input.read(8)


          

    
if __name__ == '__main__':
    secrets_key = secrets.token_bytes(16)
    print(secrets_key.hex())
    str_file_output = 'BootFileCRC\RND_SRC_Bootloader_v2_Blue.bin'
    file_encoder(str_file_output, secrets_key)
    exit(0)


    args = sys.argv[1:]
    str_file_output = args[0]
    # str_file_output = 'BootFileCRC\\RND_SRC_Bootloader_v2_Blue.bin'
    print(str_file_output)
    # FileEncoder(str_file_output)