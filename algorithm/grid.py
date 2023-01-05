from tkinter import *
import numpy as np

'''
canvas_size = (500,500)
my_canvas = MyGrid(root, size=canvas_size, bg='gray')
my_canvas.pack(pady=20)
root.update()
my_canvas.drawSquares((50,50), (0,0), "white" , 20, outline_width=1)
'''

class MyGrid(Canvas):
    def __init__(self, parent, size, **kw):
        super(MyGrid, self).__init__(parent, width=size[0], height=size[1], **kw)
        self.width = size[0]
        self.height = size[1]
        self.gsize =size

    def drawRectangle(self, gridPoint, cornerPoint, size, color, outline_color, outline_width):
        rectObject = self.create_rectangle(x1,y1,x1+size[0], y1+size[1], fill=color, outline=outline_color, width=outline_width)
        self.objectToPosition[rectObject] = (gridX, gridY)

    def color(self, x, y):
        if (self.positionInGrid(x,y)): return
        item = self.find_closest(x, y)
        self._setCube(item, location[0], location[1], True)

    def _setCube(self, cube, isOn):
        x, y = self.objectToPosition[item[0]]
        self.occupancy[x,y] = isOn
        if(isOn):
            self.itemconfig(cube, fill='green')
        else:
            self.itemconfig(cube, fill='white')

    def _positionInGrid(self, x, y):
        if (x > self.maxPoint.x or 
        x < self.minPoint.x or
        y > self.maxPoint.y or 
        y < self.minPoint.y): return False
        return True

    def printOccupancy(self):
        print(self.occupancy)

    def initialize(self, dimensions, offset, pad):
        self.dim = dimensions
        self.occupancy = np.zeros(dimensions)
        self.maxPoint = {"x": self.gsize.x - pad, "y": self.gsize.y - pad}
        self.minPoint = {"x": pad, "y": pad}
        self.objectToPosition = {}

    def drawSquares(self, fill="white", outline="black", outline_width=1):
        #declare size of a tile and size of a square inside that tile
        tile_size = {"x": self.width - 2 * self.pad) / dim.x, "y": (self.height - 2 * pad) / dim.y}
        square_size ={"x": tile_size[0] - 2 *offset[0], "y": tile_size[1] - 2 *offset[1]}

        #loop through all squares and draw them
        for x in range(0, self.dim.x):
            for y in range(0, self.dim.y):
                x1 = tile_size.x * x + offset.x
                y1 = tile_size.y * y + offset.y
		screenPoint = (x1 + self.pad y1 + self.pad)
                gridPoint = (x,y)
                self.drawRectangle( gridPoint, screenPoint, square_size, fill, outline, outline_width)
