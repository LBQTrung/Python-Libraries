from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        # Create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) # Display the menu bar

        # Create a pull-down menu, and add it to menu bar
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Operation", menu = operationMenu)
        operationMenu.add_command(label = "Add",
            command = self.add)
        operationMenu.add_command(label = "Subtract",
            command = self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label = "Multiply",
            command = self.multiply)
        operationMenu.add_command(label = "Divide",
            command = self.divide)
        
        # Create more pull-down menus
        exitmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Exit", menu = exitmenu)
        exitmenu.add_command(label = "Quit", command = window.quit)

        # Add a tool bar frame
        frame0 = Frame(window) # Create and add a frame to window
        frame0.grid(row = 1, column = 1, sticky = W)

        window.mainloop()
        # Add button


    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
MenuDemo()