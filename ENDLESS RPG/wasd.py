from tkinter import *
from functools import partial

def validateLogin(username):
	print("username entered :", username.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Enter A Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

validateLogin = partial(validateLogin, username)

#login button
loginButton = Button(tkWindow, text="Play", command=validateLogin).grid(row=4, column=0)  
tkWindow.mainloop()

                                                                                                      