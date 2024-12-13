from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Classes with Tkinter')
root.geometry("400x400")
root.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

# Database

# Establishing Connection
con = sqlite3.connect('address_book.db')

# Create Cursor
cursor = con.cursor()

# Create Table
'''
cursor.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                addresses text,
                city text,
                state text,
                pincode integer
                )""")
'''

def save():
    # Establishing Connection
    con = sqlite3.connect('address_book.db')

    # Create Cursor
    cursor = con.cursor()

    rec_id = delete_box.get()

    cursor.execute("""UPDATE addresses SET 
                    first_name= :first,
                    last_name= :last,
                    addresses= :address,
                    city= :city,
                    state= :state,
                    pincode= :pincode
                    WHERE oid= :oid""",
                   {
                       'first': f_name_editor.get(),
                       'last': l_name_editor.get(),
                       'address': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'pincode': pincode_editor.get(),
                       'oid': rec_id
                   })

    # Commit Changes
    con.commit()

    # Close Connection
    con.close()

    editor.destroy()

# Create Update Function
def update():
    global editor
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x400")
    editor.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

    # Establishing Connection
    con = sqlite3.connect('address_book.db')

    # Create Cursor
    cursor = con.cursor()

    rec_id = delete_box.get()

    # query the Database
    cursor.execute("SELECT *,oid FROM addresses WHERE oid = " + rec_id)
    record = cursor.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global pincode_editor

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    pincode_editor = Entry(editor, width=30)
    pincode_editor.grid(row=5, column=1)

    # Create Text box Label
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    pincode_label_editor = Label(editor, text="Pincode")
    pincode_label_editor.grid(row=5, column=0)

    for i in record:
        f_name_editor.insert(0, i[0])
        l_name_editor.insert(0, i[1])
        address_editor.insert(0, i[2])
        city_editor.insert(0, i[3])
        state_editor.insert(0, i[4])
        pincode_editor.insert(0, i[5])

        # Create Save Button
        save_btn = Button(editor, text="Save Record", command=save)
        save_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=143)

# Create Delete function
def delete():
    # Establishing Connection
    con = sqlite3.connect('address_book.db')

    # Create Cursor
    cursor = con.cursor()

    cursor.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0,END)

    # Commit Changes
    con.commit()

    # Close Connection
    con.close()

#Create Submit function
def submit():
    # Establishing Connection
    con = sqlite3.connect('address_book.db')

    # Create Cursor
    cursor = con.cursor()

    # Insert into Table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :pincode)",
                   {'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'pincode': pincode.get()
                    })

    # Commit Changes
    con.commit()

    # Close Connection
    con.close()

    # Clear the textbox
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pincode.delete(0, END)

def query():
    # Establishing Connection
    con = sqlite3.connect('address_book.db')

    # Create Cursor
    cursor = con.cursor()

    # query the Database
    cursor.execute("SELECT *,oid FROM addresses")
    record = cursor.fetchall()

    # Loop through result
    print_rec = ''
    for i in record:
        print_rec += str(i[6]) + "\t" + str(i[0]) + " " + str(i[1]) +"\n"

    query_label = Label(root,text=print_rec)
    query_label.grid(row=12, column=0,columnspan=2)

    # Commit Changes
    con.commit()

    # Close Connection
    con.close()

# Create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)
address = Entry(root,width=30)
address.grid(row=2,column=1)
city = Entry(root,width=30)
city.grid(row=3,column=1)
state = Entry(root,width=30)
state.grid(row=4,column=1)
pincode = Entry(root,width=30)
pincode.grid(row=5,column=1)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

# Create Text box Label
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
pincode_label = Label(root,text="Pincode")
pincode_label.grid(row=5,column=0)
delete_box_label = Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0,pady=5)

# Create submit button
submit_btn = Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

# Create Query Button
query_btn = Button(root,text="Show Records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

# Create Delete Button
delete_btn = Button(root,text="Delete Record", command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

# Create Update Button
update_btn = Button(root,text="Update Record", command=update)
update_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=143)



# Commit Changes
con.commit()

# Close Connection
con.close()
root.mainloop()