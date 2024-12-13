from tkinter import *
from PIL import ImageTk,Image

screen = Tk()
screen.title("My Python Program")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

myImg1 = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Jujutsu.png"))
myImg2 = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Hunter.png"))
myImg3 = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Demon.png"))
myImg4 = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//Mashle.png"))
myImg5 = ImageTk.PhotoImage(Image.open("C://Users//utkar//Desktop//python TKinter//Images and Icons//One piece.png"))

image_list = [myImg1,myImg2,myImg3,myImg4,myImg5]

myLabel = Label(image=myImg1)
myLabel.grid(row=0,column=0,columnspan=3)

status = Label(screen,text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
def forword(image_no):
    global myLabel
    global button_back
    global button_forward

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_no - 1])
    button_forward = Button(screen,text=">>", command=lambda :forword(image_no + 1))
    button_back = Button(screen,text="<<", command=lambda :backword(image_no - 1))

    if image_no == 5:
        button_forward = Button(screen,text=">>",state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(screen, text="Image " + str(image_no) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def backword(image_no):
    global myLabel
    global button_back
    global button_forward

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_no - 1])
    button_forward = Button(screen, text=">>", command=lambda: forword(image_no + 1))
    button_back = Button(screen, text="<<", command=lambda: backword(image_no - 1))

    if image_no == 1:
        button_back = Button(screen, text="<<", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(screen, text="Image " + str(image_no) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(screen, text="<<",command=backword, state=DISABLED)
button_exit = Button(screen, text="Exit", command=screen.quit)
button_forward = Button(screen, text=">>", command=lambda :forword(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)


screen.mainloop()