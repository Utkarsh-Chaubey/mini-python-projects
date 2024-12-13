from tkinter import *

root = Tk()
root.title('Classes with Tkinter')
root.geometry("400x400")
root.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

def clicked(event):
    #myLabel = Label(root, text="You Clicked this Button: " + event.char)       # determines the key but no special charecter
    myLabel = Label(root, text="You Clicked this Button: " + event.keysym)      # determines all keys
    #myLabel = Label(root,text="You Clicked a Button" + str(event.x) + " " + str(event.y))       # Determine the position of mouse
    myLabel.pack()

myButton = Button(root, text="Click me!")
#myButton.bind("<Button-3>", clicked)        # For Right click
#myButton.bind("<Button-3>", clicked)        # For Left click
#myButton.bind("<Enter>", clicked)           # Activates when entered in button zone
#myButton.bind("<Leave>", clicked)           # Activates when leave button zone
#myButton.bind("<FocusIn>", clicked)         # Activates When tab is pressed
#myButton.bind("<Return>", clicked)          # Activates When tab and enter is pressed
myButton.bind("<Key>", clicked)              # # Activates When tab and any key is pressed
myButton.pack(pady=20)

root.mainloop()