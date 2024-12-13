from tkinter import *

screen = Tk()
screen.title("Classes with Tkinter")
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

def something():
    my_label.config(text="this is the new text!!",font=("Halvetica",8),bg="yellow")
    screen.config(bg="blue")
    my_button.config(text="you've been configged!",bg="green",state=DISABLED,pady=30)

global my_label
my_label = Label(screen,text="this is my label", font=("times new roman",18))
my_label.pack(pady=10)

global my_button
my_button = Button(screen,text="Click Me", command=something)
my_button.pack(pady=10)


screen.mainloop()