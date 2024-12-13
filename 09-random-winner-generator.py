from tkinter import *
from random import randint

root = Tk()
root.title('Random Winner generator')
root.geometry("400x400")

def pick():
    # Contestants = 16                  # Useful with real players
    contestants = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8', 'Player9',
                   'Player10', 'Player11', 'Player12', 'Player13', 'Player14','Player12', 'Player10']

    # Convert List to Set
    contestants_set = set(contestants)
    # Convert Back To List = 14
    unique_contestants = list(contestants_set)

    # Create List size variable
    our_num = len(unique_contestants) - 1
    # Create random Number between 0 and 14
    rando = randint(0, our_num)

    winnerLabel = Label(root, text=unique_contestants[rando], font=("Helvetica", 18))
    winnerLabel.pack(pady=50)

topLabel = Label(root,text="Winner", font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = Button(root, text="PICK OUR WINNER!!", font=("Helvetica", 24), command=pick)
winButton.pack(pady=20)



root.mainloop()