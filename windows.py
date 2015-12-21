from Tkinter import Tk, Text, BOTH
from ttk import Frame, Button, Label, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Windows")
        self.pack(fill = BOTH, expand = True)

        self.columnconfigure(1, weight = 1)
        self.columnconfigure(3, pad = 7)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(5, pad = 5)

        

def main():
    root = Tk()
    app = Example(root)
    root.geometry("300x200+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()
