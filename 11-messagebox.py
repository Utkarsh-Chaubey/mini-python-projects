from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()
window.title("My Python Program")
window.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
window.geometry("400x400")

def popup():
    #response = messagebox.askquestion("This is My Popup", "Hello World")
    #response = messagebox.askyesno("This is My Popup", "Hello World")
    #response = messagebox.askokcancel("This is My Popup", "Hello World")
    #response = messagebox.askretrycancel("This is My Popup", "Hello World")
    #response = messagebox.askyesnocancel("This is My Popup", "Hello World")
    #response = messagebox.showinfo("This is My Popup", "Hello World")
    #response = messagebox.showerror("This is My Popup", "Hello World")
    response = messagebox.showwarning("This is My Popup", "Hello World")
    label = Label(window,text=response).pack()

button = Button(window, text="PopUp", command=popup)
button.pack()

window.mainloop()