from tkinter import *

root = Tk()
root.title('Resizing Entry Box')
root.geometry("400x400")

def myclick():
    hello = "Hello " + box.get()
    myLabel = Label(root, text=hello)
    box.delete(0,END)
    myLabel.pack(pady=10)

box = Entry(root,width=50, font=('Arial', 16))          # Change The Text size and Label size will change itself
box.pack(padx=10, pady=10)

myButton = Button(root,text="Enter your Name", command=myclick)
myButton.pack(pady=10)

root.mainloop()