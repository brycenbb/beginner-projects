from random import *
from tkinter.messagebox import YES
''' Rock paper scissors game taking input from player. Might come back and add GUI later'''

def playgame():
    ans = input('\nSo you would like to play RPS? Make your choice! ')

    if not ans in ('Rock','rock','Paper','paper','Scissors', "scissors"):
        return print("\n Cheater! You didn't choose one of the valid options, start over.")

    x = ["Rock", "Paper","Scissors"]
    index = randint(0,2)
    z = x[index]
    if z == ans:
        return print("\n We have tied by both choosing ", x(index))
    
    if ans == 'Rock' or ans == 'rock':
        if index == 1:
            return print("\nI have won by choosing Paper")
        else:
            return print("\nI have lost by choosing Scissors")
    elif ans == 'Paper' or ans == 'paper':
        if index == 0:
            return print("\nI have lost by choosing Rock")
        else:
            return print("\nI have won by choosing Scissors")
    else:
        if index == 0:
            return print("\nI have won by choosing Rock")
        else:
            return print("\nI have lost by choosing Paper")
    
    return print("IDK how you got this message, its an error")
    
if __name__ == '__main__':
    y = input("Would you like to play RPS with me? ")
    if y in ("Yes", "yes","y", "Y", "Yeah", "yeah", "sure", "Sure","Yea","yea"):
        playgame()
    else:
        print("\n Thanks anyway, maybe next time")
