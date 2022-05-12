# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:12:21 2022

@author: oby_pc
"""

from tkinter import *

root =Tk() #first thing

e=Entry(root,width=50,bg="blue",fg="red",borderwidth=5)
e.pack()
e.insert(0,"Enter your name")


def myClick():
    number=int(e.get())**2
    # hello="Hello "+e.get()
    myLabel=Label(root,text="hello "+str(number))
    myLabel.pack()
    print(number)

myButton=Button(root, text="Enter your name", padx=50,pady=30,command=myClick,fg="blue", bg="cyan")
myButton.pack()






root.mainloop()






















