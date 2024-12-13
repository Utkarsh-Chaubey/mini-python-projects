from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("My Python Program")
window.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("My Secondary Window")
    top.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
    my_img = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Jujutsu.png"))
    my_label = Label(top, image=my_img).pack()
    button2 = Button(top, text="Close Window", command=top.destroy).pack()

button1 = Button(window,text="Open Secondary Window",command=open).pack()

window.mainloop()