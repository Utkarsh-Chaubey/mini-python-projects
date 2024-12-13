from tkinter import *

root = Tk()
root.title('Resizing Entry Box')
root.geometry("400x400")

myLabel = Label(root)
'''
def mydelete():
    myLabel.grid_forget()
    #myLabel.destroy()
    myButton['state'] = NORMAL
    #print(myButton.winfo_exists())
'''

def myclick():
    global myLabel
    myLabel.destroy()

    hello = "Hello " + box.get()
    myLabel = Label(root, text=hello)

    box.delete(0,END)
    myLabel.grid(row=3, column=0, pady=10)
    #myButton['state'] = DISABLED

box = Entry(root,width=17, font=('Arial', 30))          # Change The Text size and Label size will change itself
box.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root,text="Enter your Name", command=myclick)
myButton.grid(row=1, column=0, pady=10)

#deleteButton = Button(root, text="Clear text", command=mydelete)
#deleteButton.grid(row=2, column=0, pady=10)
root.mainloop()