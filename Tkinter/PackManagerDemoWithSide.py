from operator import le
from tkinter import *

class PackManagerDemoWithSide:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Pack Manager Demo 2") # Set title

        Label(window, text = "Blue", bg = "blue").pack(side = LEFT)
        Label(window, text = "Red", bg = "red").pack(
            side = LEFT, fill = BOTH, expand = 1)
        Label(window, text = "Green", bg = "green").pack(
            side = LEFT, fill = BOTH)

        window.mainloop() # Create an event loop

PackManagerDemoWithSide()