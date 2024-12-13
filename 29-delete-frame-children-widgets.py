# The Program to make menu-bar and Add frames

from tkinter import *

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

my_menu = Menu(screen)
screen.config(menu=my_menu)


def my_command():
    my_label = Label(screen,text="You Clicked A dropdown Menu").pack()

# File New Function
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both",expand=1)
    my_label = Label(file_new_frame, text="You Clicked file >>> New Menu",bg="red").pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both",expand=1)
    my_label = Label(edit_cut_frame, text="You Clicked Edit >>> Cut Menu", bg="blue").pack()

def hide_all_frames():
    # Loop through all the Children(Labels,Buttons,Dropdown-box etc) in the Frame
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    edit_cut_frame.pack_forget()
    file_new_frame.pack_forget()

# Create a Menu Item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New...",command=file_new)
file_menu.add_separator()                                     # Adds a line to Separate options
file_menu.add_command(label="Exit",command=screen.quit)

# Create an Edit Menu Item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",command=edit_cut)
edit_menu.add_command(label="Copy",command=my_command)

# Create an Option Menu Item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find",command=my_command)
option_menu.add_command(label="Go To Line",command=my_command)

# Create some Frames
file_new_frame = Frame(screen,width=400,height=400,bg="red")
edit_cut_frame = Frame(screen,width=400,height=400,bg="blue")

screen.mainloop()