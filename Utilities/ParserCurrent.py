import matplotlib.pyplot as plt


class LilaCurrent(object):
    def __init__(self):
        self.current = []
        self.seconds = []

    def get_current(self):
        return self.current

    def get_seconds(self):
        return self.seconds

    def transform_data(self):
        file_input = open('DebugOutput/output_current.txt', 'r')
        file_csv = open('DebugOutput/csv_current.txt', 'w')
        seconds = 0
        for line in file_input:
            str_record = line.replace(line[0:24], '')  # remove Date
            pos = str_record.find('\n')
            current = int(str_record[0:pos])
            self.current.append(current)
            str_record_csv = str_record.replace(str_record[pos], ',')
            file_csv.write(str_record_csv + '\n')

            seconds += 1
            self.seconds.append(seconds)

            """ str_record = line.replace(line[0:27], '')  # remove Date and Time
            for i in range(7):
                pos = str_record.find(',')
                if i == 3:
                    iac = int(str_record[0:pos])
                    self.iac.append(iac)
                if i == 4:
                    gfci = int(str_record[0:pos])
                    self.gfci.append(gfci)

                str_record = str_record.replace(str_record[0:pos + 1], '') """


        # t_array.append(t)
        # file_csv.write(str(t) + ',' + '\n')
        # print(str_record)

        file_csv.close()
        file_input.close()
        print(seconds)



if __name__ == '__main__':
    __doc__ = """
    ....
    """

    fig, ax = plt.subplots()

    lila_current = LilaCurrent()
    lila_current.transform_data()
    plt.ylim(0, 3000)
    ax.plot(lila_current.get_seconds(), lila_current.get_current(), label="Current, mA")

    ax.set(xlabel='time', ylabel='mA', title='Current consumption')
    ax.grid()
    plt.legend()
    plt.show()

    print("OK")