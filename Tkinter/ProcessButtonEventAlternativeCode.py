from lib2to3.pgen2.token import PLUS
from tkinter import *
from turtle import circle

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", fg = "yellow", command = self.processCancel)

        btOK.pack()
        btCancel.pack()

        window.mainloop()
    def processOK(self):
        print("OK button is clicked")
    
    def processCancel(self):
        print("Cancel button is clicked")

ProcessButtonEvent()