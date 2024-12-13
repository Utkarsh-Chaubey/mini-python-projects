from tkinter import *

screen = Tk()

entrybox = Entry(screen, width=50)
entrybox.pack()
entrybox.insert(0, "Enter Your Name")

def click():
    message = "Hello " + entrybox.get()
    mylabel = Label(screen, text=message)
    mylabel.pack()

myButton = Button(screen, text="Click Me", command=click)
myButton.pack()

screen.mainloop()