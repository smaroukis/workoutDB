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

#TODO restrict to only low, med, high intensities
#TODO restrict only to bike, swim, run
#TODO better user interface (scroll both ways, larger listbox)

from tkinter import *
import backend

def get_selected_row(event): # since we binded this to the <<ListboxSelect>> widget event
    # When user selects a row in the listbox, grab the id and put the data in the textboxes, use the bind method
    global selected_row # Need to perform action on in delete_command()
    index=list1.curselection()[0]
    selected_row = list1.get(index)# get's a tuple of values
    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])

def view_command():
    list1.delete(0, END) # deletes from 0 to END of listbox
    for row in backend.view():
        list1.insert(END, row) # insert(index, what) method  is specific to tkinter list objects

def search_command():
    list1.delete(0, END)
    for row in backend.search(type_text.get(), duration_text.get(),  intensity_text.get(), description_text.get()): # StringVar is not a direct string
        list1.insert(END, row)

def add_command():
    backend.insert(type_text.get(), duration_text.get(),  intensity_text.get(), description_text.get())
    list1.delete(0, END)
    list1.insert(END, [type_text.get(), duration_text.get(),  intensity_text.get(), description_text.get()] )
    view_command()

def delete_command():
    backend.delete(selected_row[0])
    view_command()
    # delete selected row, need to add data in text fields when selected in listbox

def update_command():
    backend.update(selected_row[0], type_text.get(), duration_text.get(),  intensity_text.get(), description_text.get())
    view_command()

backend.connect()

window=Tk()
window.wm_title("WorkoutDB")

l1=Label(window, text="Type")
l1.grid(row=0, column=0)

l2=Label(window, text="Intensity")
l2.grid(row=1, column=0)

l3=Label(window, text="Duration")
l3.grid(row=2, column=0)

l4=Label(window, text="Description")
l4.grid(row=3, column=0)

type_text=StringVar()
e1=Entry(window, textvariable=type_text)
e1.grid(row=0, column=1)

intensity_text=StringVar()
e2=Entry(window, textvariable=intensity_text)
e2.grid(row=1, column=1)

duration_text=StringVar()
e3=Entry(window, textvariable=duration_text)
e3.grid(row=2, column=1)

description_text=StringVar()
e4=Entry(window, textvariable=description_text)
e4.grid(row=3, column=1)

list1=Listbox(window, height=6, width=25)
list1.grid(row=0, column=2, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=0, column=4, rowspan=6)

list1.configure(yscrollcommand=sb1.set) # connecting the list and scroll bar
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row) # Binds the get_selected_row function to the <<ListboxSelect>> widget event

b1=Button(window, text="Search", width=12, command=search_command)
b1.grid(row=6, column=0)

b2=Button(window, text="Add", width=12, command=add_command)
b2.grid(row=4, column=0)

b3=Button(window, text="Update", width=12, command=update_command)
b3.grid(row=5, column=0)

b4=Button(window, text="View All", width=12, command=view_command)
b4.grid(row=6, column=1)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=4, column=1)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=5, column=1)


window.mainloop()
