import os
import sys
import array as buf_array
import zipfile
import csv


def file_decoder(file_input_name):
    filename, file_extension = os.path.splitext(file_input_name)

    filename_zip = filename + ".zip"
    filename_csv = filename + ".csv"
    print(filename)
    print(file_extension)

    file_name_extract = os.path.basename(file_input_name).split('/')[-1]
    os.rename(file_input_name, filename_zip)

    with zipfile.ZipFile(filename_zip, mode="r") as archive:
        file_input = archive.read(file_name_extract, pwd=b"vctr")
    print(file_input)
    decoded_string = file_input.decode("utf-8")
    string_array = decoded_string.split(',')
    print(decoded_string)
    print(string_array)

    os.rename(filename_zip, file_input_name)

    date_time = string_array[0]
    operator = string_array[1]

    with open(filename_csv, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(23):
            part_number = string_array[2] + str(i).zfill(2)
            if string_array[3 + i] == '1':
                employee_writer.writerow([date_time, operator, part_number, "Passed"])
            else:
                employee_writer.writerow([date_time, operator, part_number, "Failure"])

    """ file_size = os.stat(file_input_name)
    file_input = open(file_input_name, 'rb')
    bytes_input = file_input.read(file_size)
    file_input.close() """
    # os.remove(self.nameReportFile)
    # os.rename(name_zip_file, self.nameReportFile)






if __name__ == '__main__':
    __doc__ = """
    ....
    """

    args = sys.argv[1:]
    # str_file_output = args[0]
    str_file_output = "../Reports/LL01-000000000.vctr"

    file_decoder(str_file_output)
