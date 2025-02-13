import struct
from matplotlib import pyplot as plt
from matplotlib import figure
from scipy.interpolate import make_interp_spline
import numpy as np


if __name__ == '__main__':
    __doc__ = """
    ....
    """

    f = open('.\Data\ChamberMotor_noStuck.txt', 'r')

    count = 0
    one = f.readline().replace(' ', '')
    two = f.readline().replace(' ', '')
    y = []

    for i in range(0, len(one), 4):
        hex_string = one[i:i + 4]
        byte_string = bytes.fromhex(hex_string)
        if len(byte_string) > 1:
            y.append(struct.unpack('<H', byte_string)[0])

    x = np.arange(0, len(y))
    plt.plot(x, y)
    plt.rcParams["figure.figsize"] = (60, 20)
    plt.show()

    """ zeroLevel = 0
    for i in range(0, len(y)):
        zeroLevel += y[i]
    zeroLevel /= len(y)

    y_out = []
    for i in range(0, len(y)):
        if zeroLevel > y[i]:
            y_out.append(zeroLevel - y[i])
        elif y[i] > zeroLevel:
            y_out.append(y[i] - zeroLevel)
        else:
            y_out.append(0)

    x = np.arange(0, len(y_out))
    plt.plot(x, y_out)
    plt.rcParams["figure.figsize"] = (60, 20)
    plt.show() """



    """ X_smooth = np.linspace(x.min(), x.max(), 2000)
    spline = make_interp_spline(x, y)
    Y_smooth = spline(X_smooth)

    plt.plot(X_smooth, Y_smooth)
    plt.rcParams["figure.figsize"] = (60, 20)
    plt.show()

    y = []
    for i in range(0, len(two), 4):
        hex_string = two[i:i + 4]
        byte_string = bytes.fromhex(hex_string)
        if len(byte_string) > 1:
            y.append(struct.unpack('<H', byte_string)[0])

    plt.plot(range(0, len(y)), y)
    plt.rcParams["figure.figsize"] = (60, 15)
    plt.show() """
