from tkinter import *

screen = Tk()
screen.title("Classes with Tkinter")
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

amz_btn=PhotoImage(file='C:/Users/utkar/Desktop/python TKinter/Images and Icons/amazon-logo.png')

amz_btn2=PhotoImage(file='C:/Users/utkar/Desktop/python TKinter/Images and Icons/amazon-logo.png')

def things():
    my_label.config(text="You Clicked The Button")

img_label=Label(image=amz_btn)
#img_label.pack(pady=20)

img_label2=Label(image=amz_btn2)

myBtn=Button(screen,image=amz_btn, command=things, borderwidth=0)
myBtn.pack(pady=20)

myBtn=Button(screen,image=amz_btn2, command=things)
myBtn.pack(pady=20)

my_label=Label(screen,text="")
my_label.pack(pady=20)


screen.mainloop()