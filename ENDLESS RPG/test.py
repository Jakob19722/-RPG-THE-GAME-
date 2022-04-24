from tkinter import *   
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs
def changeText():  
    btn['text'] = 'Welcome to StackHowTo!'
  
def changeColor():  
    btn['bg'] = 'Red'
gui = Tk()  
gui.geometry('200x100')  
btn = Button(gui, text = "Click here!", command = two_funcs(changeText, changeColor))
btn.pack()
gui.mainloop()