from tkinter import *

root = Tk()

# Creating Label Widget
myLabel1 = Label(root,text="This is row=0, column=0")
myLabel2 = Label(root, text="This is row=1, column=0")
myLabel3 = Label(root, text="This is row=0, column=1")
myLabel4 = Label(root, text="This is row=1, column=1")

# Grid does NOT Arrange with Refference to Screen
myLabel5 = Label(root, text="This is row=1, column=5")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=0, column=1)
myLabel4.grid(row=1, column=1)

# Grid Occupies the remaining space
myLabel5.grid(row=1, column=5)

root.mainloop()