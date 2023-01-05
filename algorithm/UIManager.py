from tkinter import *
from algorithm.dropDownMenu import *
from algorithm.grid import *
from algorithm.UIManager import *

class Manager:
    def __init__(self, window):
        self.window = window
        self.gridInPixels = (500,500)

        self._create_grid()

    def _create_grid(self):
        self.my_canvas = MyGrid(self.window, size = self.gridInPixels, bg='gray')
        self.my_canvas.pack(pady=20)
        self.window.update()
        self.my_canvas.drawSquares((10,10), (0,0), "white" , 20, outline_width=1)
        self.window.bind('<B1-Motion>', self.motion)
       

    def motion(self, event):
        if (event.widget == self.my_canvas):
            print('#'*50)
            print(self.my_canvas.printOccupancy())
            print('#'*50)
 
            self.my_canvas.color(event.x, event.y)
