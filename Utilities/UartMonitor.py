import time
import sys
import serial
import os



if __name__ == '__main__':
    __doc__ = """
    ....
    """
    # print(buffer)
    # print(len(buffer))
    # sys.exit(0)

    com_port_number = input("Enter COM port number: COM")
    
    if not com_port_number.isdigit():
        raise ValueError("Invalid COM port number. Please enter a numeric value.")
    
    com_port_number = "COM" + com_port_number

    try:
        com_port = serial.Serial(com_port_number, 115200, timeout=0.5)
    except serial.SerialException:
        print("Serial Exception:")
        print(sys.exc_info())
        sys.exit(1)

    output_folder = "DebugOutput"
    # Add the current date to the output file name
    current_date = time.strftime("%Y-%m-%d")
    output_file = os.path.join(output_folder, f"debug_output_{current_date}_{com_port_number}.txt")
    # output_file = os.path.join(output_folder, "debug_output.txt")

    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the file in write-binary mode
    file_output = open(output_file, 'ab')  # Open in append-binary mode

    while True:
        time.sleep(0.1)
        read_data = com_port.readline()
        len_data = len(read_data)
        if len_data == 0:
            continue

        try:
            string = read_data.decode()
            string = string.replace("\r\n", '')
            print(string)
        except UnicodeDecodeError:
            pass

        file_output.write(read_data)
        file_output.flush()  # Ensure data is written to the file in real time
