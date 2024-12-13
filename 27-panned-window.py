from tkinter import *

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("400x400")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

# Panels
panel_1 = PanedWindow(bd=4,relief=RAISED,bg="red")
panel_1.pack(fill=BOTH,expand=1)

left_label = Label(panel_1,text="Left Panel")
panel_1.add(left_label)

# Create Second Panel
panel_2 = PanedWindow(panel_1,orient=VERTICAL,bd=4,relief=RAISED,bg="blue")
panel_1.add(panel_2)

top_label = Label(panel_2,text="Top Panel")
panel_2.add(top_label)

bottom_label = Label(panel_2,text="Bottom Panel")
panel_2.add(bottom_label)


screen,mainloop()