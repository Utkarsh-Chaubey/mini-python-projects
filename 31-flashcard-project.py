import random
from tkinter import *
from PIL import ImageTk, Image
from random import randint

screen = Tk()
screen.title('Classes with Tkinter')
screen.geometry("500x560")
screen.iconbitmap("C:/Users/utkar/Desktop/python TKinter/Images and Icons/icon1.ico")

# Create Randomizing state function
def random_state():
    # Create list of state names
    global our_states
    our_states = ['andra pradesh','himachal pradesh','karnataka','kerala','punjab','madhya pradesh','rajesthan','tamil nadu','utter pradesh','west bengal']

    # Generate random number
    global random_no
    random_no = randint(0,len(our_states)-1)
    random_state = 'C://Users//utkar//Desktop//python TKinter//Images and Icons//states//' + our_states[random_no] + '.png'

    # Create state images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(random_state))
    show_state.config(image=state_img,bg="white")

# Create state_capital_answer function
def state_capital_answer():
    if capital_radio.get() == our_state_capital[answer]:
        response = "Correct! " + our_state_capital[answer].title() + " is the capital of " + answer.title()
    else:
        response = "Incorrect! " + our_state_capital[answer].title() + " is the capital of " + answer.title()

    answer_label_capital.config(text=response)

# Create state_answer function
def state_answer():
    answer = answer_input.get()
    # Determine if answer is right or wrong
    if answer.lower() == our_states[random_no]:
        response = "correct! >>>" + our_states[random_no].title()
    else:
        response = "incorrect! >>>" + our_states[random_no].title()
    answer_label.config(text=response)

    # Clear Entry box
    answer_input.delete(0, END)

    random_state()

# Create State Flashcard function
def states():
    hide_all_frames()
    states_frame.pack(expand=1,fill=BOTH)
    """
    # Create list of state names
    global our_states
    our_states = ['andra pradesh','himachal pradesh','karnataka','kerala','punjab','madhya pradesh','rajesthan','tamil nadu','utter pradesh','west bengal']

    # Generate random number
    global random_no
    random_no = randint(0,len(our_states)-1)
    random_state = 'C://Users//utkar//Desktop//python TKinter//Images and Icons//states//' + our_states[random_no] + '.png'

    # Create state images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(random_state))
    """
    global show_state
    show_state = Label(states_frame)
    show_state.pack(pady=15)
    random_state()

    # Create answer input box
    global answer_input
    answer_input = Entry(states_frame,font=("Cooper",18),bg="white",bd=2)
    answer_input.pack(pady=15)

    # Create Button to randomize state images
    state_btn = Button(states_frame,text="Pass", command=states)
    state_btn.pack(pady=10)

    # Create Button To answer the question
    answer_btn = Button(states_frame,text="Answer",command=state_answer)
    answer_btn.pack(pady=5)

    # Create Label to check your answer
    global answer_label
    answer_label = Label(states_frame,text="",font=("Cooper",18))
    answer_label.pack(pady=15)

# Create state capitals function
def state_capitals():
    hide_all_frames()
    state_capital_frame.pack(expand=1,fill=BOTH)

    global show_state
    show_state = Label(state_capital_frame)
    show_state.pack(pady=15)


    global our_states
    our_states = ['andra pradesh', 'himachal pradesh', 'karnataka', 'kerala', 'punjab', 'madhya pradesh', 'rajesthan',
                  'tamil nadu', 'utter pradesh', 'west bengal']

    global our_state_capital
    our_state_capital = {
        'andra pradesh': "amaravati",
        'himachal pradesh': "shimla",
        'karnataka': "bangalore",
        'kerala': "thiruvananthapuram",
        'punjab': "Chandigarh",
        'madhya pradesh': "Bhopal",
        'rajesthan': "Jaipur",
        'tamil nadu': "Chennai",
        'utter pradesh': "Lucknow",
        'west bengal': "Kolkata"
    }

    # Create empty answer list and counter
    answer_list = []
    count = 1

    # Generate 3 options
    while count < 4:
        random_no = randint(0, len(our_states) - 1)

        global answer
        # if first selection makes it our answer
        if count == 1:
            answer = our_states[random_no]
            global state_img
            state = 'C://Users//utkar//Desktop//python TKinter//Images and Icons//states//' + our_states[random_no] + '.png'
            state_img = ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_img)

        # Add our First selection to a new list
        answer_list.append(our_states[random_no])

        # Remove Answer from the old list
        our_states.remove(our_states[random_no])

        # Shuffle Original list
        random.shuffle(our_states)
        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(None)

    capital_radio_btn1 = Radiobutton(state_capital_frame,text=our_state_capital[answer_list[0]].title(),variable=capital_radio,value=our_state_capital[answer_list[0]]).pack()
    capital_radio_btn2 = Radiobutton(state_capital_frame,text=our_state_capital[answer_list[1]].title(),variable=capital_radio,value=our_state_capital[answer_list[1]]).pack()
    capital_radio_btn3 = Radiobutton(state_capital_frame,text=our_state_capital[answer_list[2]].title(),variable=capital_radio,value=our_state_capital[answer_list[2]]).pack()

    # Add a Pass button
    pass_button = Button(state_capital_frame,text="Pass",command=state_capitals)
    pass_button.pack(pady=15)

    # Create a button to answer
    capital_answer_btn = Button(state_capital_frame,text="Answer",command=state_capital_answer)
    capital_answer_btn.pack(pady=15)

    # Create an Answer label
    global answer_label_capital
    answer_label_capital = Label(state_capital_frame,text="",font=("Engravers MT",10))
    answer_label_capital.pack(pady=15)

# Hide All previous Frames
def hide_all_frames():
    for widget in states_frame.winfo_children():
        widget.destroy()

    for widget in state_capital_frame.winfo_children():
        widget.destroy()

    states_frame.pack_forget()
    state_capital_frame.pack_forget()

# Create Menu
my_menu = Menu(screen)
screen.config(menu=my_menu)

# Create Geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geogrphy", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=screen.quit)

# Create Frames
states_frame = Frame(screen,width=500,height=500,bg="white")
state_capital_frame = Frame(screen,width=500,height=500)

screen.mainloop()