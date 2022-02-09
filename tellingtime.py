
def tellingtime(input):
    '''Takes time in seconds from the user and tells them the amount of days, hours, minutes, and seconds it is.
        If the user does not call the function with the proper type, namely int, then they are prompted
        to try again.'''
    
    if isinstance(input, int):
        days = 0
        hours = 0
        minutes = 0
        seconds = input
        while seconds >= 0:
            if seconds >= 86400:
                days += 1
                seconds -= 86400
            elif seconds >= 3600:
                hours += 1
                seconds -= 3600
            elif seconds >= 60:
                minutes += 1
                seconds -= 60
            else:
                return print(input, "seconds is equivalent to", days,'days, ', hours,'hours,', minutes,'minutes and ', seconds,'seconds')
                
    else:
        print('You did not provide a proper number value using ' + input + ', please try again using strictly only numbers')

if __name__ == '__main__':
    print('Input the amount of seconds you wish to convert')
    arg = input()
    if arg.isnumeric():
        tellingtime(int(arg))
    else:
        tellingtime(arg)

    print('Would you like to play again? Yes/No')
    answer = input()
    while answer == 'Yes':
        print('Input the amount of seconds you wish to convert')
        arg = input()
        if arg.isnumeric():
           tellingtime(int(arg))
        else:
            tellingtime(arg)
        print('Would you like to play again? Yes/No')
        answer = input()
    print('Thank you for playing, goodbye')
