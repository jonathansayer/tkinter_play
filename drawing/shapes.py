from Tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Shapes")
        self.pack(fill = BOTH, expand = 1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline = "gray", fill = "gray", width = 2)
        canvas.create_oval(110, 10, 210, 80, outline = "gray", fill = "gray", width = 2)

        canvas.pack(fill = BOTH, expand = 1)

def main():
    root = Tk()
    app = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()
