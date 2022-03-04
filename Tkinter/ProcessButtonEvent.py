from tkinter import *
from turtle import color

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

# Create a window
window = Tk()
btOK = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)
# Place the OK button in the window
btOK.pack()
# Place the Cancel button in the window
btCancel.pack()
# Create the event loop
window.mainloop()