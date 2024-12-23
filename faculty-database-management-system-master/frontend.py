from tkinter import *
from ttkbootstrap import Style
from ttkbootstrap.widgets import Combobox

import backend

def get_selected_row(event):
    global selected_tuple
    if lb1.curselection() != ():
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        clear_entries()
        e1.insert(END, selected_tuple[1])
        dept.set(selected_tuple[2])
        exp.set(f"{selected_tuple[3]} years")
        e4.insert(END, selected_tuple[4])

def view_command():
    lb1.delete(0, END)
    for row in backend.view():
        lb1.insert(END, row)

def search_command():
    lb1.delete(0, END)
    for row in backend.search(fn.get(), dept.get(), exp.get().split()[0], gpa.get()):
        lb1.insert(END, row)
    clear_entries()

def add_command():
    backend.insert(fn.get(), dept.get(), exp.get().split()[0], gpa.get())
    clear_entries()
    view_command()

def update_command():
    backend.update(selected_tuple[0], fn.get(), dept.get(), exp.get().split()[0], gpa.get())
    clear_entries()
    view_command()

def delete_command():
    if lb1.curselection():
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        backend.delete(selected_tuple[0])
        clear_entries()
        view_command()

def delete_data_command():
    backend.delete_data()
    view_command()

def clear_entries():
    e1.delete(0, END)
    dept.set(departments[0])
    exp.set(experience[0])
    e4.delete(0, END)

def clear_command():
    lb1.delete(0, END)
    clear_entries()

# Modern UI Window
style = Style("darkly")  # Use a sleek, modern dark theme
wind = style.master
wind.grid_columnconfigure(3, weight=1)  # Make column 3 (button column) stretchable

wind.title("Faculty Database Management System")
wind.geometry("800x600")  # Set window size

# Variables
fn = StringVar()
gpa = StringVar()
dept = StringVar()
exp = StringVar()

# Dropdown Menu Options
departments = ["CSE", "ISE", "ECE", "CIVIL", "MECH", "AIML"]
experience = [f"{i} years" for i in range(1, 31)]

dept.set(departments[0])
exp.set(experience[0])

# Title
Label(wind, text="Faculty Database Management", font=("Helvetica", 20, "bold"), bg="#1F1F1F", fg="#BB86FC").grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")
wind.grid_columnconfigure(3, weight=1)  # Make column 3 (button column) stretchable

# Labels
Label(wind, text="Name", font=("Helvetica", 12), bg="#1F1F1F", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
Label(wind, text="Faculty Dept", font=("Helvetica", 12), bg="#1F1F1F", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
Label(wind, text="Experience (in years)", font=("Helvetica", 12), bg="#1F1F1F", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)
Label(wind, text="Salary", font=("Helvetica", 12), bg="#1F1F1F", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky=W)

# Entries and Dropdown Menus
e1 = Entry(wind, textvariable=fn, font=("Helvetica", 12))
e4 = Entry(wind, textvariable=gpa, font=("Helvetica", 12))
department_menu = Combobox(wind, textvariable=dept, values=departments, state="readonly", font=("Helvetica", 12))
experience_menu = Combobox(wind, textvariable=exp, values=experience, state="readonly", font=("Helvetica", 12))
# Positioning Inputs
e1.grid(row=1, column=1, padx=10, pady=10, sticky=W)
department_menu.grid(row=2, column=1, padx=10, pady=10, sticky=W)
experience_menu.grid(row=3, column=1, padx=10, pady=10, sticky=W)
e4.grid(row=4, column=1, padx=10, pady=10, sticky=W)

# Buttons with ttkbootstrap styles
style_button = "primary-outline"  # Rounded button style
from ttkbootstrap.widgets import Button

# Correct Button creation with ttkbootstrap
Button(wind, text="View All", bootstyle=style_button, command=view_command).grid(row=1, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Search", bootstyle=style_button, command=search_command).grid(row=2, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Add New", bootstyle=style_button, command=add_command).grid(row=3, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Update", bootstyle=style_button, command=update_command).grid(row=4, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Delete", bootstyle="danger-outline", command=delete_command).grid(row=5, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Clear", bootstyle=style_button, command=clear_command).grid(row=6, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Delete All Faculty", bootstyle="danger", command=delete_data_command).grid(row=7, column=3, padx=10, pady=10, sticky="ew")
Button(wind, text="Exit", bootstyle="secondary-outline", command=wind.destroy).grid(row=8, column=3, padx=10, pady=10, sticky="ew")

# Listbox and Scrollbar
lb1 = Listbox(wind, height=15, width=50, font=("Helvetica", 10))
lb1.grid(row=5, column=0, rowspan=4, columnspan=2, padx=10, pady=10)
lb1.bind('<<ListboxSelect>>', get_selected_row)

sc = Scrollbar(wind, command=lb1.yview)
sc.grid(row=5, column=2, rowspan=4, sticky=N+S)
lb1.configure(yscrollcommand=sc.set)

wind.mainloop()
