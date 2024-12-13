from tkinter import *

root = Tk()
root.title('Classes with Tkinter')
root.geometry("400x400")

class Elder:

    def __init__(self, master):
        myframe = Frame(master)
        myframe.pack()

        self.myButton = Button(master, text="Click me!", command=self.clicked)
        self.myButton.pack(pady=20)

    def clicked(self):
        print("Good Job")


e = Elder(root)

root.mainloop()