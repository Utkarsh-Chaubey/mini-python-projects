from tkinter import *
from PIL import ImageTk,Image

screen = Tk()
screen.title("My Python Program")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
screen.geometry("400x400")

vertical = Scale(screen,from_=0, to=300)
vertical.pack()

def slider():
    my_label = Label(screen, text=horizontal.get()).pack()
    screen.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(screen,from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(screen,text=horizontal.get()).pack()

myButton = Button(screen,text="Resize", command=slider).pack()
screen.mainloop()