from tkinter import *

screen = Tk()

def click():
    myLabel = Label(screen,text="Button is Clicked")
    myLabel.pack()

myButton = Button(screen,text="Click Me",command=click,bg="yellow",fg="red")
myButton.pack()

myButton2 = Button(screen,text="desabled button",state=DISABLED)
myButton2.pack()


screen.mainloop()