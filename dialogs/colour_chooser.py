from Tkinter import Tk, Frame, Button, BOTH, SUNKEN
import tkColorChooser

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Colour Chooser")
        self.pack(fill = BOTH, expand = 1)

        self.btn = Button(self, text = "Choose Color", command = self.onChoose)
        self.btn.place( x = 30, y = 30 )

        self.frame = Frame(self, border = 1, relief = SUNKEN, width = 100, height = 100)
        self.frame.place(x = 160, y= 30)

    def onChoose(self):
        (rgb, hx) = tkColorChooser.askcolor()
        self.frame.config(bg = hx)


def main():
    root = Tk()
    app = Example(root)
    root.geometry("300x150+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()
