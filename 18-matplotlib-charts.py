from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plot

page = Tk()
page.title("My Python Program")
page.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")
page.geometry("400x200")

def graph():
    house_price = np.random.normal(200000, 25000, 50000)
    plot.hist(house_price,50)
    #plot.pie(house_price)
    #plot.polar(house_price)
    plot.show()


myButton = Button(page,text="Graph It", command=graph)
myButton.pack()

page.mainloop()