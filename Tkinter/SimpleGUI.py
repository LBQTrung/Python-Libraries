from tkinter import *

#Create a window
window = Tk() 
# Create a label
label = Label(window, text = "Welcome to Python")
# Create a button
button = Button(window, text = "Click me")
# Place the label in the window
label.pack()
# Place the button in the window
button.pack()
# Create an event loop
window.mainloop() 