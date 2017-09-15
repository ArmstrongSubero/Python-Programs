import serial           # import serial library
from visual import *    # import vPython library

# create object to read serial port
arduinoSerialData = serial.Serial('com3', 9600)

#create cylinder object
measuringRod = cylinder(length = 4, color = color.yellow, radius = 0.1, pos = (-3,-2,0))

#create label object                                     #x  y  z
lengthLabel = label(text = 'Target distance is: ', pos = (0, 5, 0), height = 30, box = false)

# create box object
target = box(color = color.green, length = 0.2, width = 3, height = 3,  pos = (0, -0.5, 0)) 

# loop forever
while(1):
    # set rate to update for vPython
    rate(20)
    # if data on serial port
    if(arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline() # if data there read it

        # convert string from serial port to float
        distance = float(myData)

        print distance
        
        # set label to string + data read
        myLabel = "Target distance is " + myData

        # dynamically update lengthLabel text
        lengthLabel.text = myLabel

        # set measuring rod to distance
        measuringRod.length = distance

        # change box position
        target.pos = (-3+distance, -0.5, 0)
