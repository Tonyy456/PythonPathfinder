from tkinter import *
'''
canvas_size = (500,500)
my_canvas = MyGrid(root, size=canvas_size, bg='gray')
my_canvas.pack(pady=20)
root.update()
my_canvas.drawSquares((50,50), (0,0), "white" , 20, outline_width=1)
'''
class MyGrid(Canvas):
    def __init__(self, parent=None, size=(500,500), **kw):
        super(MyGrid, self).__init__(parent, width=size[0], height=size[1], **kw)
        self.width = size[0]
        self.height = size[1]

    def drawRectangle(self, x1, y1, size, color, outl, w):
        self.create_rectangle(x1,y1,x1+size[0], y1+size[1], fill=color, outline=outl, width=w)

    def drawSquares(self, dim, offset, fill="blue", pad=0, outline="black", outline_width=1):
        #declare size of a tile and size of a square inside that tile
        tile_size = ((self.width - 2*pad) / dim[0], (self.height - 2*pad) / dim[1])
        square_size =(tile_size[0]-2*offset[0],tile_size[1]-2*offset[1])
        
        #loop through all squares and draw them
        for x in range(0, dim[0]):
            for y in range(0, dim[1]):
                x1 = tile_size[0] * x + offset[0]
                y1 = tile_size[1] * y + offset[1]
                self.drawRectangle(x1 + pad, y1 + pad, square_size, fill, outline, outline_width)
