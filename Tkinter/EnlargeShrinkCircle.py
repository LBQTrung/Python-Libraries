from tkinter import *

class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50

        window = Tk()
        window.title("Enlarge Shrink Circle")
        self.canvas = Canvas(window, width = 200,
            height = 200, bg = "white")
        self.canvas.pack()
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags = "oval"
        )

        # Bind canvas with mouse event
        self.canvas.bind("<Button-1>", self.increaseCircle)
        self.canvas.bind("<Button-2>", self.decreaseCircle)

        window.mainloop()
    
    def increaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius < 100:
            self.radius += 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags = "oval"
        )
    
    def decreaseCircle(self, event):
        self.canvas.delete("oval")
        if self.radius > 2:
            self.radius -= 2
        self.canvas.create_oval(
            100 - self.radius, 100 - self.radius,
            100 + self.radius, 100 + self.radius, tags = "oval"            
        )

EnlargeShrinkCircle()