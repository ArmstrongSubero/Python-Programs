# import comm tools
from time import sleep
from msvcrt import kbhit
import pywinusb.hid as hid
from pywinusb import *
import sys

#import gui
from tkinter import *
from tkinter import messagebox

#global variable
count = 0

#-------------------------------------------------------------------------------
# Function reads data from list and Prints second element
#-------------------------------------------------------------------------------
def readData(data):
    # copy of global variable count to modify
    global count

    # read data and insert into textbox1
    str1 = str(data[1]) + '\n'
    t1.insert(END, str1)

    # increment count
    count = count + 1

    # if 10 reached, clear textbox and reset count
    if (count > 10):
        # clear textbox 1
        t1.delete("1.0", END)
        count = 0

    return None

#-------------------------------------------------------------------------------
# default function displays menu to user
#-------------------------------------------------------------------------------
def default():
    # find all devices
    all_hids = hid.find_all_hid_devices()

    # if devices found
    if all_hids:
        # show user menu
        txt1= "Choose a device to monitor input reports:\n"
        txt2= "0 => Exit\n"

        # write menu to textbox1
        t1.insert(END, txt1)
        t1.insert(END, txt2)

        # get data on all found devices
        for index, device in enumerate(all_hids):
            device_name = str("{0.vendor_name} {0.product_name}" \
                    "(vID=0x{1:04x}, pID=0x{2:04x})"\
                    "".format(device, device.vendor_id, device.product_id))
            # display found devices for user
            txt3 = ("{0} => {1}\n".format(index+1, device_name))

            # write all options to textbox
            t1.insert(END, txt3)

#-------------------------------------------------------------------------------
# function is event handler for button click and communicates with PC
#-------------------------------------------------------------------------------
def onClick():
    #disable button
    btn1.config(state=DISABLED)

    # clear textbox 1
    t1.delete("1.0", END)

    # find all devices
    all_hids = hid.find_all_hid_devices()

    # get user choice of device from textbox 2
    selected_device = int(t2.get(1.0, END))

    # store user selection in variable
    device = all_hids[selected_device-1]

    try:
        # open selected device
        device.open()

        # set datahandler to read data
        device.set_raw_data_handler(readData)

        # browse output reports
        report = device.find_output_reports()

        # while not key pressed and device is connected, keep doing
        while not kbhit() and device.is_plugged():
                #turn LED off
                buffer= [0xFF]*65
                buffer[0]=0x0  # report id
                buffer[1]=0x74 # off command (t)
                report[0].set_raw_data(buffer)
                report[0].send()

                # write value every second and update window
                sleep(1)
                window.update()

                # turn LED on
                buffer= [0xFF]*65
                buffer[0]=0x0     # report id
                buffer[1]=0x62    # on command(b)
                report[0].set_raw_data(buffer)
                report[0].send()

                # write value every second and update window
                sleep(1)
                window.update()

    except IndexError:
        err_txt = "Please check your device and try again"
        t1.insert(END, err_txt)

    finally:
        # close device
        device.close()


#-------------------------------------------------------------------------------
# function shows about box on GUI
#-------------------------------------------------------------------------------
def showAbout():
    messagebox.showinfo("About HID Communicator", "Created by Armstrong Subero")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Program Start
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# create an empty window
window = Tk()

# rename window
window.title("HID Communicator")

# make window non-resizeable
window.resizable(0,0)

# text window
t1 = Text(window, height=10, width=80)
t1.grid(row = 0, column=0)

# make textbox read only
t1.bind("<Key>", lambda e: "break")

# entry box
t2 = Text(window, height=2, width=8, padx=10)
t2.grid(row = 3, column=0)

# create buttons
buttonframe = Frame(window)
buttonframe.grid(row=5, column=0, columnspan=2)
btn1 = Button(buttonframe, text = "Enter", width=10, command=onClick)
btn1.grid(row=0, column=0)

# add menubar
menu= Menu(window)
window.config(menu=menu)

# add menu items
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=filemenu)
filemenu.add_command(label="About", command=showAbout)

# call default function
default()

#infinite loop
window.mainloop()
