from tkinter import *
import tkinter.font as font

def combine_funcs(*funcs):
    
    def combined_func(*args, **kwargs):
        
        for f in funcs:
            f(*args, **kwargs)
    
    return combined_func

def welcome():
    
    print('Welcome!')

def level_1():
    
    print('Lets go')

def tutorial():
    print('Lets go')
def secondwindow():

    root2=Tk()
    root2.geometry('500x100')
    root2.title('Level Selection')

    button=Button(root2,bg='black',fg='blue',text='Tutorial',height=10, width=35, command=combine_funcs(tutorial, root2.destroy))
    button.pack(side=LEFT)
    button=Button(root2,bg='black',fg='orange', text='Level 1', height=10, width=35, command=combine_funcs(level_1, root2.destroy))
    button.pack(side=RIGHT)
    root2.resizable(0,0)
    root2.mainloop()

def firstwindow():

    root=Tk()
    root.geometry('500x100')
    root.title('Main Menu')
    button=Button(root,bg='black', fg='green', text='Play',height=10, width=35, command=combine_funcs(welcome,root.destroy,secondwindow))
    button.pack(side=LEFT)
    button=Button(root,bg='black',fg='red',text='Quit', height=10, width=35, command=combine_funcs(quit))
    button.pack(side=RIGHT)
    
    root.resizable(0,0)
    root.mainloop()

firstwindow()