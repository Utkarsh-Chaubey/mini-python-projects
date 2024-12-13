from tkinter import *

screen = Tk()
screen.title("Simple Calculator")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

entry = Entry(screen,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    first_no = entry.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_no)
    entry.delete(0,END)

def button_equal():
    second_no = entry.get()
    entry.delete(0, END)

    if math == "Addition":
        entry.insert(0, f_num + int(second_no))

    if math == "Subtraction":
        entry.insert(0, f_num - int(second_no))

    if math == "Multiplication":
        entry.insert(0, f_num * int(second_no))

    if math == "Divition":
        entry.insert(0, f_num / int(second_no))


def button_subtract():
    first_no = entry.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_no)
    entry.delete(0, END)
def button_multiply():
    first_no = entry.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_no)
    entry.delete(0, END)
def button_divide():
    first_no = entry.get()
    global f_num
    global math
    math = "Divition"
    f_num = int(first_no)
    entry.delete(0, END)

button_1 = Button(screen, text="1", padx=40, pady=20, command=lambda :button_click(1))
button_2 = Button(screen, text="2", padx=40, pady=20, command=lambda :button_click(2))
button_3 = Button(screen, text="3", padx=40, pady=20, command=lambda :button_click(3))
button_4 = Button(screen, text="4", padx=40, pady=20, command=lambda :button_click(4))
button_5 = Button(screen, text="5", padx=40, pady=20, command=lambda :button_click(5))
button_6 = Button(screen, text="6", padx=40, pady=20, command=lambda :button_click(6))
button_7 = Button(screen, text="7", padx=40, pady=20, command=lambda :button_click(7))
button_8 = Button(screen, text="8", padx=40, pady=20, command=lambda :button_click(8))
button_9 = Button(screen, text="9", padx=40, pady=20, command=lambda :button_click(9))
button_0 = Button(screen, text="0", padx=40, pady=20, command=lambda :button_click(0))

button_add = Button(screen,text="+",padx=39,pady=20,command=button_add)
button_subtract = Button(screen,text="-",padx=41,pady=20,command=button_subtract)
button_multiply = Button(screen,text="*",padx=40,pady=20,command=button_multiply)
button_divide = Button(screen,text="/",padx=41,pady=20,command=button_divide)

button_equal = Button(screen, text="=", padx=91, pady=20,command=button_equal)
button_clear = Button(screen, text="Clear", padx=79, pady=20, command=button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

screen.mainloop()