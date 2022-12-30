import tkinter as tk
import tkinter.ttk as ttk
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
print(dir(tk))
class MyGrid():
    def __init__(self, master, w=250, h=200, xdim=5, ydim=4):
        canvas = tk.Canvas(master, width=w, height=h)
        rectS = (w/xdim, h/ydim)
        for i in range(0, xdim):
            for j in range(0, ydim):
                canvas.create_rectangle(rectS[0]*i, rectS[1]*j, rectS[0], rectS[1])
        self.canvas = canvas
    

root = tk.Tk()
root.geometry("800x800")
ddm = AlgorithmSelection(root)
ddm.grid(row=0, column=0, sticky='nw')
grid = MyGrid(root)
root.mainloop()

