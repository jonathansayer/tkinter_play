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
        warning = Button(self, text = "Warning", command = self.onWarn)
        warning.grid(row = 1, column = 0)

    def onError(self):
        mbox.showerror("Error", "Could not open file")

    def onWarn(self):
        mbox.showwarning("Warning", "Deprecated function call")


def main():
    root = Tk()
    app = Example(root)
    root.geometry("300x150+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()
