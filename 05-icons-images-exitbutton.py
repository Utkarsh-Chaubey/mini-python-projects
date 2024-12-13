from tkinter import *
from PIL import ImageTk,Image

front = Tk()
front.title("My Python Program")
front.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

myImg = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Jujutsu.png"))
myLabel = Label(image=myImg)
myLabel.pack()

exit_Button = Button(front, text="Exit", command=front.quit)
exit_Button.pack()

front.mainloop()