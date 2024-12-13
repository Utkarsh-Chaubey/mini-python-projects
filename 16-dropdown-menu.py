from tkinter import *
from PIL import ImageTk,Image

main = Tk()
main.title("My Python Program")
main.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
main.geometry("400x400")

def show():
    myLabel = Label(main,text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(main,clicked,*options)
drop.pack()

myButton = Button(main,text="Show Selection", command=show).pack()

main.mainloop()