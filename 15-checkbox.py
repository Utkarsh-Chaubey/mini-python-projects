from tkinter import *
from PIL import ImageTk,Image

front = Tk()
front.title("My Python Program")
front.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
front.geometry("400x400")

def show():
    myLabel = Label(front,text=var.get()).pack()

var = StringVar()

checkbox = Checkbutton(front,text="Click hear to SuperSize Your Order", variable=var,onvalue="SuperSize", offvalue="RegularSize")
checkbox.deselect()
checkbox.pack()

myButton = Button(front,text="Show Selection",command=show)
myButton.pack()
front.mainloop()