import random

random_int= list(range(1, 101))
number = random.choice(random_int)

hard_easy = input("Hard or easy? (hard/easy) ").lower()
if hard_easy == "easy":
    turns = 10
else:
    turns = 5

user_guess = int(input("Guess a number between 1 - 100 : "))

def loop_till_end():
    if user_guess == number:
        return True
    elif user_guess > number:
        return "Greater".lower()
    elif user_guess < number:
        return "Smaller".lower()

while turns > 0:
    if loop_till_end() == "greater" or "smaller":
        turns -= 1
    print("Bue")



