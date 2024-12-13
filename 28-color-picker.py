from tkinter import *
from tkinter import colorchooser

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(screen,text="You Choose Color!!!!!",bg=my_color).pack()

button = Button(screen,text="Pick A Color",command=color).pack()

screen,mainloop()