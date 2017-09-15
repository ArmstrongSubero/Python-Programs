import serial  # import serial library
import numpy   # import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *   # import drawnow library

# create two empty arrays with data from data stream
tempF = []
pressure = []

# create object to read from serial port
arduinoData = serial.Serial('com3', 9600)

# tell matplot lib to plot live data (interactive mode)
plt.ion()

cnt = 0

# create a function that makes desired plot
def makeFig():
    plt.ylim(80, 100)                               # set y min and max values
    plt.title("Live Streaming Sensor Data")         # plot title
    plt.grid(True)                                  # show grid
    plt.ylabel("TempF")                             # plot y label
    plt.plot(tempF, 'ro-', label='Degrees F')       # show temperature
    plt.legend(loc='upper left')                    # show first plot legend at upper left
    
    # create a twin of plt
    plt2 = plt.twinx()                  
    # set y limit for twin
    plt.ylim(90000, 105000)
    plt2.plot(pressure, 'b^-', label = "Pressure (Pa)")  # plot as blue triangle with line
    plt2.legend(loc= 'upper right')  # show plt2 legend at upper right
    

# loop forever
while True:
    # hang until there is data on serial port
    while (arduinoData.inWaiting == 0):
        pass  # do nothing

    # once there is data from arduino read string
    arduinoString = arduinoData.readline()

    # create an array with two values of split arduino string
    dataArray = arduinoString.split(',')

    # convert temp data to float
    temp = float(dataArray[0])

    # convert pressure data to float
    p = float(dataArray[1])

    # add data to tempF array
    tempF.append(temp)

    # add data to pressure array
    pressure.append(p)

    # call drawnow to update live graph
    drawnow(makeFig)

    # delay required by drawnow
    plt.pause(0.000001)

    # increment count
    cnt = cnt + 1

    # keep only 40 points
    if (cnt > 40):
        # remove last element from array
        tempF.pop(0)

        # remove last element from array
        pressure.pop(0)





