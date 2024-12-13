from tkinter import *

screen = Tk()
screen.title("Classes with Tkinter")
screen.geometry("700x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

entries=[]
def show_content():
    list_entry=""
    for i in entries:
        list_entry = list_entry + str(i.get()) + '\n'
        my_label.config(text=list_entry)

# Row loop
for x in range(5):
    # Column Loop
    for y in range(5):
        my_entry = Entry(screen)
        my_entry.grid(row=x,column=y,pady=20,padx=5)
        entries.append(my_entry)

my_button = Button(screen,text="Click me",command=show_content)
my_button.grid(row=6,column=0,pady=20)

my_label = Label(text="")
my_label.grid(row=7,column=0,pady=20)

screen.mainloop()