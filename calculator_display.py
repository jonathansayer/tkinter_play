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

        self.pack()

def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
