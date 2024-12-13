# FOR UNICODE CHARACTERS SEARCH THERE CODES ON GOOGLE

from tkinter import *

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

my_label1 = Label(screen,text="40" + u"\u00b0",font=("Engravers MT",32)).pack(pady=10)

my_label2 = Label(screen,text="40" + u"\u00a9",font=("Cooper",32)).pack(pady=10)

#my_label3 = Label(screen,text="40" + u"\u00c0",font=("Engravers MT",32)).pack(pady=10)

#my_label4 = Label(screen,text="40" + u"\u00a4",font=("Engravers MT",32)).pack(pady=10)

#my_label5 = Label(screen,text="40" + u"\u00d5",font=("Engravers MT",32)).pack(pady=10)

my_button = Button(screen,text=u'\u00bb',font=("Curlz MT",32)).pack()

screen.mainloop()