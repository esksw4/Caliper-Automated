import tkinter
from itertools import cycle
 
class App(tkinter.Tk):
    def __init__(self, textList, master=None):
        tkinter.Tk.__init__(self, master)
        self.textiter = cycle(textList)
        self.txt = tkinter.StringVar()
        self.whatever = tkinter.Entry(self)
        self.whatever.pack()
        self.rootEntry = tkinter.Entry(self, textvariable=self.txt)
        self.rootEntry.pack()
        print("arg: ", self.whatever)
        print("arg1: ", self.rootEntry)
        self.whateverMethod(self.whatever, self.rootEntry)
        self.rootEntry.bind("<Return>", self.cycle_text)
        self.rootText = tkinter.Text(self)
        self.rootText.pack()
        self.rootText.bind("<Insert>", self.insert_all)
        self.newList = []
 
    def cycle_text(self, arg=None):
        t = self.textiter.next()
        self.txt.set(t)
        self.rootText.insert("end", t+"\n")
        self.newList.append(self.rootText.get("end - 2 chars linestart", "end - 1 chars"))
 
    def insert_all(self, arg):
        self.rootText.insert("end", "".join([s.strip() for s in self.newList]))

    def whateverMethod(self, arg, arg1):
        print("inside whateverMethod, arg: ", arg)
        print("inside whateverMethod, arg1: ", arg1)
 
textList = ["Line 1", "Line 2", "Line 3"]
root = App(textList)
root.mainloop()