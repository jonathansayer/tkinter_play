from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from ttk import Frame, Label, Entry

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Review")
        self.pack(fill = BOTH, expand = True)

        frame1 = Frame(self)
        frame1.pack(fill = X)

        lbl1 = Label(frame1, text = "Title", width = 6)
        lbl1.pack(side = LEFT, padx = 5, pady = 5)

        frame2 = Frame(self)
        frame2.pack(fill = X)

        lbl2 = Label(frame2, text = "Author", width = 6)
        lbl2.pack(side = LEFT, padx = 5, pady = 5)

        frame3 = Frame(self)
        frame3.pack(fill = X, expand = True)




def main():
    root = Tk()
    root.geometry("300x300+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()
