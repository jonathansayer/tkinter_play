from Tkinter import Tk,Frame, RIGHT, BOTH, RAISED
from ttk import Button, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief = RAISED, borderwidth = 1 )
        frame.pack(fill = BOTH, expand = True)

        self.pack(fill = BOTH, expand = True)

        closeButton = Button(self, text = "Close", command = self.quit)
        closeButton.pack(side = RIGHT, padx = 5, pady = 5)
        okButton = Button(self, text = "OK", command = self.printHello)
        okButton.pack(side = RIGHT)

    def printHello(self):
        print "Hello World"


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()
