from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Absalute Positioning")
        self.pack(fill=BOTH, expand = 1)

        Style().configure("TFrame", background = "#333")

        gotpic = Image.open("GOTpicture.jpg")
        gotpicobj = ImageTk.PhotoImage(gotpic)
        label1 = Label(self, image = gotpicobj)
        label1.image = gotpicobj
        label1.place(x = 20, y = 20)

        canyonpic = Image.open("canyon.jpg")
        canyonpicobj = ImageTk.PhotoImage(canyonpic)
        label2 = Label(self, image = canyonpicobj)
        label2.image = canyonpicobj
        label2.place(x = 40, y = 160)

        scipic = Image.open("science.jpeg")
        scipicobj = ImageTk.PhotoImage(scipic)
        label3 = Label(self, image = scipicobj)
        label3.image = scipicobj
        label3.place(x = 170, y = 50)

def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
