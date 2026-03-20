from tkinter import *
import database

def add_command():
    database.insert(name_text.get(), age_text.get(),
                    course_text.get(), email_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (name_text.get(), age_text.get(),
                         course_text.get(), email_text.get()))

def view_command():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)

    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])

    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])

    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])

    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def update_command():
    database.update(selected_tuple[0],
                    name_text.get(),
                    age_text.get(),
                    course_text.get(),
                    email_text.get())
    view_command()

window = Tk()
window.title("Student Management System")

# Labels
Label(window, text="Name").grid(row=0, column=0)
Label(window, text="Age").grid(row=0, column=2)
Label(window, text="Course").grid(row=1, column=0)
Label(window, text="Email").grid(row=1, column=2)

# Entries
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

age_text = StringVar()
e2 = Entry(window, textvariable=age_text)
e2.grid(row=0, column=3)

course_text = StringVar()
e3 = Entry(window, textvariable=course_text)
e3.grid(row=1, column=1)

email_text = StringVar()
e4 = Entry(window, textvariable=email_text)
e4.grid(row=1, column=3)

# Listbox
listbox = Listbox(window, height=10, width=50)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

listbox.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
Button(window, text="Add", width=12, command=add_command).grid(row=2, column=3)
Button(window, text="View All", width=12, command=view_command).grid(row=3, column=3)
Button(window, text="Update", width=12, command=update_command).grid(row=4, column=3)
Button(window, text="Delete", width=12, command=delete_command).grid(row=5, column=3)
Button(window, text="Close", width=12, command=window.destroy).grid(row=6, column=3)

window.mainloop()