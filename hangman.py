from random import *
from words import wordlist

def playgame(lives):
    if lives > 25:
        lives = 15
        print("\nSorry, lives have been set to the maximum of 15")
    

    validword = get_valid_word()
    
    guess = '_' * len(validword)
    get_progress(guess)
    guesses = []
   
    while lives > 0:
        if guess.find('_') == -1:
            return print("\nCongratulations, you have won! The answer was:", guess)
        print("")
        userguess = input("\nPlease guess a letter: ")

        '''If the guess is not the right format'''
        if len(userguess) > 1 or not userguess.isalpha():
            print("\nYour guess was not in the right format, please try again.")
            continue

        '''forces guess into lowercase'''
        userguess = userguess.lower()

        '''If the guess is new, add to list of guesses and see if its a right guess or not'''
        if not userguess in guesses:
            guesses.append(userguess)
            '''If guess is in the word'''
            if validword.find(userguess) != -1:
                '''Finding indicies for multiple instances of a certain letter'''
                indicies = []
                temp = validword
                if validword.count(userguess) > 1:
                    
                    while temp.find(userguess) != -1:
                        indicies.append(temp.find(userguess))
                        
                        temp = temp[:temp.find(userguess)] + '9' + temp[temp.find(userguess)+1:]
                        
                        
                else:
                    indicies.append(temp.find(userguess))
                   

                guess_list = list(guess)
                for z in indicies:
                    guess_list[z] = userguess
                guess = "".join(guess_list)

                '''If guess is not in word'''
            else:
                lives -= 1
                print("\nSorry, that guess is incorrect. You have lost a life.","\n", lives, " lives remaining.")

        else:
            print("\nYou have already guessed that letter, try again")

        get_progress(guess)
        print("\n")
        print("\nThe letters you guessed are:","\n",guesses)
    return print("\nSorry, you have lost! The answer was ", validword, "\nThe letters you guessed were:","\n", guesses)



def get_progress(input):
    print("\nProgress: ")
    i = 0
    while i < len(input):
        cur = input[i]
        print(cur, " ", end="")
        i += 1
    return
 

def get_valid_word():
    x = choice(wordlist)
    while '-' in x or ' ' in x:
        x = choice(wordlist)
    return x


if __name__ == '__main__':
    y = input("\nPlease input the number of lives you want: ")
    if y.isnumeric():
        playgame(int(y))
    else:
        print("Please enter a number next time")