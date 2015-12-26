from ttk import Frame, Button
from Tkinter import Tk, BOTH
import tkMessageBox as mbox


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Message Box")
        self.pack()

        error = Button(self, text = "Error", command = self.onError)
        error.grid(padx = 5, pady = 5)


def main():
    root = Tk()
    app = Example()
    root.geometry("300x150+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()
