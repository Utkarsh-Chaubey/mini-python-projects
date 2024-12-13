# List box with scroll bar

from tkinter import *

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("400x600")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

# Create frame and scrollbar
my_frame = Frame(screen)
my_scrollbar = Scrollbar(my_frame,orient=VERTICAL)

# ListBox!
# SINGLE,MUTIPLE,EXTENDED,BROWSE
my_listbox = Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,selectmode=MULTIPLE)

# Configure Scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_frame.pack()

my_listbox.pack(pady=15)

# Add items in the listbox
my_listbox.insert(0, "Item 0")
my_listbox.insert(END, "Item 1")
my_listbox.insert(END, "Item 2")

# Add list of items
my_list = ["Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5","Item 3","Item 4","Item 5"]

for items in my_list:
    my_listbox.insert(END,items)

def delete():
    my_listbox.delete(ANCHOR)

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0,END)

def select_all():
    result = ''

    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + '\n'

    my_label.config(text= result)

def delete_multiple():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)
        my_label.config(text='')

my_button = Button(screen,text="Detete",command=delete)
my_button.pack(pady=10)

my_button2 = Button(screen,text="Select",command=select)
my_button2.pack(pady=10)

global my_label
my_label = Label(screen,text="")
my_label.pack(pady=5)

my_button3 = Button(screen,text="Delete All",command=delete_all)
my_button3.pack(pady=10)

my_button4 = Button(screen,text="Select All",command=select_all)
my_button4.pack(pady=10)

my_button5 = Button(screen,text="Delete Multiple",command=delete_multiple)
my_button5.pack(pady=10)

screen.mainloop()