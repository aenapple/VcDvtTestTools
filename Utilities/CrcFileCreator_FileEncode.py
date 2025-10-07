from CrcFileCreator import *
from FileEncoder import *
import sys


    
if __name__ == '__main__':
    __doc__ = """
    ....
    """

    args = sys.argv[1:]
    str_file_input = args[0]
    # str_file_input = 'Files/s_qspi.bin'

    str_file_output = GenerateCRCFile(str_file_input)

    secrets_key = secrets.token_bytes(16)
    print(secrets_key.hex())

    encryption = Encryption()

    encryption.file_encoder(str_file_output, secrets_key)


