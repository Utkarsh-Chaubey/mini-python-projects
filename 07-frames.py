from tkinter import *

screen = Tk()
screen.title("My Python Program")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

# Purpose: To make different sections in Program

frame1 = LabelFrame(screen,padx=50,pady=50)
frame1.pack(padx=10,pady=10)

frame2 = LabelFrame(screen,padx=50,pady=50)
frame2.pack(padx=10,pady=10)

b1 = Button(frame1,text="Button 1")
b2 = Button(frame1,text="Button 2")

b3 = Button(frame2,text="Button 3")
b4 = Button(frame2,text="Button 4")

b1.grid(row=0,column=0)
b2.grid(row=1,column=1)

b3.grid(row=0,column=0)
b4.grid(row=0,column=1)

screen.mainloop()