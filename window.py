from tkinter import *
from algorithm.dropDownMenu import *

'''
to find out what you can do with a certain tkinter object...
	btn = ttk.Button(frm, ...)
	print(btn.configure().keys())

or you can compare what methods a certain object has
	print(set(btn.configure().keys()) - set(frm.configure().keys()))

or print every option!
	print(dir(btn))
	print(set(dir(btn)) - set(dir(frm)))
'''

def drawRectangle(canvas, x1, y1, w, h):
    canvas.create_rectangle(x1,y1,x1+w, y1+h, fill="blue")

root = Tk()
root.title('Python Pathfinder')
root.geometry("800x800")

canvas_size = (500,500)

my_canvas = Canvas(root, width=canvas_size[0], height=canvas_size[1], bg="white")
my_canvas.pack(pady=20)

square_size = (94,94)
offset = (3,3)
tile_size=(square_size[0]+2*offset[0],square_size[1]+2*offset[1])
numSquares = (canvas_size[0]/tile_size[0], canvas_size[1]/tile_size[1])
for i in range(0,int(numSquares[0])):
    for j in range(0,int(numSquares[1])):
        drawRectangle(
                 my_canvas,
                 tile_size[0] * i + offset[0],
                 tile_size[1] * j + offset[1],
                 square_size[0],square_size[1])

root.mainloop()

