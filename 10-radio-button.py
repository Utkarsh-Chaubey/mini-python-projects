from tkinter import *

window = Tk()
window.title("My Python Program")
window.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
window.geometry("400x400")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(window,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(window,text=value)
    myLabel.pack()

#myLabel = Label(window,text=pizza.get())
#myLabel.pack()

myButton = Button(window,text="Click Me", command=lambda: clicked(pizza.get()))
myButton.pack()

window.mainloop()