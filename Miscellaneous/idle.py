from tkinter import Tk, Button, Frame, Entry, END

class ABC(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.geometry("300x25")
        self.pack()
        self.make_widgets()

    def kill(self):
        self.parent.destroy()
        quit()

    def make_widgets(self):
        self.winfo_toplevel().title("Disable Lights")
        log_button = Button(self.master, text="End Idle Loop", command=self.kill)
        log_button.pack()

root = Tk()
abc = ABC(root)
root.mainloop()