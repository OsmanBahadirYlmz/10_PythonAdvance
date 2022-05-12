# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:12:21 2022

@author: oby_pc
"""

from tkinter import *

root =Tk() #first thing


# creating a label
myLabel1= Label(root,text="hello world!")
myLabel2= Label(root,text="my name is oby")



# showing it on the screen can be done above
# like myLabel1= Label(root,text="hello world!").grid(row=0, column=0)
myLabel1.grid(row=0, column=0) 
myLabel2.grid(row=1, column=5)






root.mainloop()






















