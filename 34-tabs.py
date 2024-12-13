from tkinter import *
from tkinter import ttk

screen = Tk()
screen.title("Classes with Tkinter")
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

my_notebook=ttk.Notebook(screen)
my_notebook.pack()

def hide():
    my_notebook.hide(1)     #Here 1 is the index no. of 2nd Tab just like a list

def show():
    my_notebook.add(frame2, text="red Tab")

def select():
    my_notebook.select(1)

frame1=Frame(my_notebook,width=400,height=400,bg="green")       # Green Tab  index 0
frame2=Frame(my_notebook,width=400,height=400,bg="red")         # Red Tab index1

frame1.pack(fill="both",expand=1)
frame2.pack(fill="both",expand=1)

my_notebook.add(frame1,text="Green Tab")
my_notebook.add(frame2,text="Red Tab")

# Hide a Tab
my_Button1=Button(frame1,text="Hide tab 2",command=hide).pack(pady=15)

# Show the Tab
my_Button2=Button(frame1,text="Show tab 2",command=show).pack(pady=15)

# Navigate to a Tab
my_Button3=Button(frame1,text="Navigate to Tab2",command=select).pack(pady=15)

screen.mainloop()