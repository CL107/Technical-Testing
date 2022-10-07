import tkinter as tk
from tkinter import Tk, ttk
import sv_ttk
#import TKinterModernThemes as TKMT

class mainmenu():

    def __init__(self, master):
        
        # Setting the theme 
        #super().__init__(str("Chat Room"), str("azure"), str("dark"))
        
        # This where the magic happens
        sv_ttk.set_theme("dark")
        
        #menu gui
        self.master = master
        self.master.geometry("500x500")
        self.master.config(bg="Black")
        self.master.resizable(0,0)

        #db connection
        # self.host = "5.133.180.245"
        # self.db = "cliddell_project"
        # self.user = "cliddell_Nova"
        # self.password = "Motorstorm107!"
        # self.db_connection = mysql.connect(host=self.host, database=self.db, user=self.user, password=self.password)
        # self.dbhandler = self.db_connection.cursor()
        # print("Connected to:", self.db_connection.get_server_info())

        #presets for program
        # self.preset1 = "10"
        # self.preset2 = "5"
        # self.preset3 = "0.04"
        # self.preset4 = "100"

        #ttk styles
        # self.s = ttk.Style()
        # self.s.configure("frame.TFrame", background="#404040")
        # self.s.configure("label.TLabel", foreground="White", background="#404040")
        # self.s.configure("button.TButton", foreground="Black")
        # self.s.configure("combobox.TCombobox", background="Black")
        # self.s.configure("entry.TEntry", background="Grey")

        # #ttk maps
        # #self.s.map("frame.TFrame", background="Black")
        # #self.s.map("label.TLabel", foreground="White", background="Black")
        # self.s.map("button.TButton", 
        #     background=[("active", "#404040")],
        #     foreground=[("active", "Blue")],
            # )
        # self.s.map("combobox.TCombobox", background="Black")
        # self.s.map("entry.TEntry", background="Grey")

    def home(self):
        self.frame = ttk.Frame(self.master, height=500, width=500)
        
        log_button = ttk.Button(self.frame, text="Login")
        log_button.place(x=220, y=20)

        reg_button = ttk.Button(self.frame, text="Register")
        reg_button.place(x=220, y=50)

        pass_button = ttk.Button(self.frame, text="Forgotten Password")
        pass_button.place(x=200, y=80)

        quit_button = ttk.Button(self.frame, text="Quit", command=self.master.destroy)
        quit_button.place(x=220, y=110)

        self.frame.place(x=0, y=0)   

if __name__ == "__main__":
    root = tk.Tk()
    R = mainmenu(root)
    R.home()
    root.mainloop()