from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Classes with Tkinter')
#root.geometry("400x400")


myImg = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Jujutsu.png"))
myLabel = Label(root,image=myImg)
myLabel.place(x=10,y=10,relwidth=1,relheight=1)
myLabel.pack()

myLabel2 = Label(root,text="Hello")
myLabel2.pack(pady=10)

root.mainloop()