from tkinter import Tk, Canvas, Frame, BOTH
class grid(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.tile("Lines")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(self)
        canvas.create_line(15,25,200,25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(fill=BOTH, expand=1)

