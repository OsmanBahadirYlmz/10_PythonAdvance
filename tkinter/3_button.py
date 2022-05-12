# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:12:21 2022

@author: oby_pc
"""

from tkinter import *

root =Tk() #first thing

e=Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()


def myClick():
    myLabel=Label(root,text="look!i clicked a button")
    myLabel.pack()

myButton=Button(root, text="Click me!", padx=50,pady=30,command=myClick,fg="blue", bg="cyan")
myButton.pack()






root.mainloop()






















