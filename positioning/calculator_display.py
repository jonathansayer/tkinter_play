from Tkinter import Tk, W, E
from ttk import Frame, Button, Style
from ttk import Entry

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")

        Style().configure("TButton", padding = (0,5,0,5), font = 'serif 10')

        self.columnconfigure(0, pad = 3)
        self.columnconfigure(1, pad = 3)
        self.columnconfigure(2, pad = 3)
        self.columnconfigure(3, pad = 3)

        self.rowconfigure(0, pad = 3)
        self.rowconfigure(1, pad = 3)
        self.rowconfigure(2, pad = 3)
        self.rowconfigure(3, pad = 3)
        self.rowconfigure(4, pad = 3)

        entry = Entry(self)
        entry.grid(row = 0, columnspan = 4, sticky = W + E)
        clear = Button(self, text = 'Cls')
        clear.grid(row = 1, column = 0)
        bck = Button(self, text = "Bck")
        bck.grid(row = 1, column = 1)
        lbl = Button(self)
        lbl.grid(row = 1, column = 2)
        close = Button(self, text = "Close")
        close.grid(row = 1, column = 3)

        sev = Button(self, text = "7")
        eig = Button(self, text = "8")
        nin = Button(self, text = "9")
        div = Button(self, text = "/")
        sev.grid(row = 2, column = 0)
        eig.grid(row = 2, column = 1)
        nin.grid(row = 2, column = 2)
        div.grid(row = 2, column = 3)

        four = Button(self, text = "4")
        five = Button(self, text = "5")
        six = Button(self, text = "6")
        mul = Button(self, text = "*")
        four.grid(row = 3, column = 0)
        five.grid(row = 3, column = 1)
        six.grid(row = 3, column = 2)
        mul.grid(row = 3, column = 3)

        one = Button(self, text = "1")
        two = Button(self, text = "2")
        thr = Button(self, text = "3")
        sub = Button(self, text = "-")
        one.grid(row = 4, column = 0)
        two.grid(row = 4, column = 1)
        thr.grid(row = 4, column = 2)
        sub.grid(row = 4, column = 3)

        zer = Button(self, text = "0")
        dec = Button(self, text = ".")
        equ = Button(self, text = "=")
        pls = Button(self, text = "+")
        zer.grid(row = 5, column = 0)
        dec.grid(row = 5, column = 1)
        equ.grid(row = 5, column = 2)
        pls.grid(row = 5, column = 3)

        self.pack()

def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
