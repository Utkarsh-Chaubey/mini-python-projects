from tkinter import *

root = Tk()
root.title('Remave Label')
root.geometry("400x400")

def mydelete():
    #myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = NORMAL
    #print(myButton.winfo_exists())
def myclick():
    global myLabel
    hello = "Hello " + box.get()
    myLabel = Label(root, text=hello)
    box.delete(0,END)
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED

box = Entry(root,width=50, font=('Arial', 16))          # Change The Text size and Label size will change itself
box.pack(padx=10, pady=10)

myButton = Button(root,text="Enter your Name", command=myclick)
myButton.pack(pady=10)

deleteButton = Button(root, text="Clear text", command=mydelete)
deleteButton.pack(pady=10)
root.mainloop()