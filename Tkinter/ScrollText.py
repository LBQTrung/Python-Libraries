import py_compile
from tkinter import *

class ScrollText:
    def __init__(self):
        window = Tk()
        window.title("Scroll Text")

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        text = Text(frame1, width = 40, height = 10, wrap = WORD,
            yscrollcommand = scrollbar.set)
        text.pack()
        scrollbar.config(command = text.yview)

        window.mainloop()
        
ScrollText()