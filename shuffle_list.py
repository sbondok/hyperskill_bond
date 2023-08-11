from random import shuffle

def shuffle_list(mylist):
    """Shuffle a given list and return it to variable """
    shuffle(mylist)
    return mylist



def user_guess():
    """Grap the user guess and return it as a number"""
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Guess 'O' position (0 , 1, 2) ")
    return int(guess)

def check_guessed(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess")
        print(mylist)

# INITIAL LIST
list_1 = [' ', 'O',' ']

# SHUFFLE THE LIST
result = shuffle_list(list_1)

# GET THE USER GUESS
guess = user_guess()

# CHECK THE RESULT
check_guessed(result, guess)