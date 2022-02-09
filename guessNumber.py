from random import randint
from tkinter import *

def guessnumber(arg):
    '''root = Tk()
    canvas = Canvas(root, height = 600, width = 600, bg = "#263d42")
    canvas.pack()
    root.mainloop()'''
    x = randint(1,10)
    if not isinstance(arg, int):
        print('Silly goose2, please try again with a number this time')
    else:
        numGuess = 0
        while(True):
            if arg == x:
                if numGuess == 0:
                    return print("WOW! There was only a 10% chance for you to guess it right the first time!")
                elif numGuess < 5:
                    return print("Great job, you got it right in less than average tries")
                else:
                    return print("You got it right!")
            else:
                ans = input("Ah, sorry that is not the right number. Do you want to guess again? Y/N")
                if ans == 'Y' or ans == "y":
                    ans = input("Good sport, please tell me your next guess then")
                    arg = int(ans)
                    numGuess += 1
                else:
                    return print("Thank you for playing, better luck next time!")




if __name__ == '__main__':
    print('Please guess a number between 0 and 10')
    x = input()
    guessnumber(int(x))
