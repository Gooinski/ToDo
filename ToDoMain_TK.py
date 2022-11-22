import tkinter
from tkinter import *

root = Tk()
root.title('Weekly To Do List')
root.geometry('300x400')
root.resizable(0, 0)
root.config(bg="CadetBlue1")

#Heading

Label(root, text='Weekly To Do List', bg='CadetBlue1', font=("Helvetica", 15), wraplength=300).place(x=35, y=0)

#Listbox scroll all tasks bar
tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)

scroller.place(x=260, y=50, height=232)

#Running loop
root.update()
root.mainloop()