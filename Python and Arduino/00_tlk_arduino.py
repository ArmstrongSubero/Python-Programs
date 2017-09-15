import serial    #import serial library

# create serial port object
arduinoSerialData = serial.Serial('com3', 9600)

# keep looping
while(1):
    # only read data if data is there
    if(arduinoSerialData.inWaiting()>0):
        # read data from serial port and put in var
        myData = arduinoSerialData.readline()
        # once data read print
        print myData
        

