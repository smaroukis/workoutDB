"""
A program that stores the following workout information:
Type, Intensity, Duration, Description

User can:
View all
Search by Type, Intensity, Duration
Add entry
Update entry
Delete
Close
"""

from tkinter import *

window=Tk()

l1=Label(window, text="Type")
l1.grid(row=0, column=0)

l2=Label(window, text="Intensity")
l2.grid(row=1, column=0)

l3=Label(window, text="Duration")
l3.grid(row=2, column=0)

type_text=StringVar()
e1=Entry(window, textvariable=type_text)
e1.grid(row=0, column=1)

intensity_text=StringVar()
e2=Entry(window, textvariable=intensity_text)
e2.grid(row=1, column=1)

duration_text=StringVar()
e3=Entry(window, textvariable=duration_text)
e3.grid(row=2, column=1)

list1=Listbox(window, height=6, width=25)
list1.grid(row=0, column=2, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=0, column=4, rowspan=6) 

list1.configure(yscrollcommand=sb1.set) # connecting the list and scroll bar
sb1.configure(command=list1.yview)

b1=Button(window, text="Search", width=12)
b1.grid(row=3, column=0)

b2=Button(window, text="Add", width=12)
b2.grid(row=4, column=0)

b3=Button(window, text="Update", width=12)
b3.grid(row=5, column=0)

b4=Button(window, text="View All", width=12)
b4.grid(row=3, column=1)

b5=Button(window, text="Delete", width=12)
b5.grid(row=4, column=1)

b6=Button(window, text="Close", width=12)
b6.grid(row=5, column=1)


window.mainloop()
