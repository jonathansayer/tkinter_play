from Tkinter import Tk, BOTH, Frame
from ttk import Button, Style


class Example(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent,background ="white")
        self.parent = parent
        self.centerWindow()
        self.createButtons()
        self.initUI()

    def initUI(self):
        self.parent.title("Quit Button")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)


    def createButtons(self):
        helloButton = Button(self, text = "Hello", command = self.printHello)
        helloButton.place(x = 100, y = 100)
        quitButton = Button(self, text="Quit", command = self.quit)
        quitButton.place(x = 50, y = 50)

    def printHello(self):
        print "Hello World"

    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w,h,x,y))



def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
