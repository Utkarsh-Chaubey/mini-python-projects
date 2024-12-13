from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

box = Tk()
box.title("My Python Program")
box.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
#box.geometry("400x400")

def open():
    global my_img
    box.filename = filedialog.askopenfilename(initialdir="C://Users//utkar//Desktop//python TKinter//Images and Icons", title="Select a File", filetypes=(("png files", "*.png*"),("All Files", "*.*")))
    my_label = Label(box, text=box.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(box.filename))
    my_img_label = Label(image=my_img).pack()

my_button = Button(box,text="Open File", command=open).pack()

box.mainloop()