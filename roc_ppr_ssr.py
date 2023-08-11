# Rock Paper Scissors ASCII Art
from random import random, randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
pc_choice = randint(0,2)

your_choice = int(input("0 for Rock, 1 for Paper, 2 for Scissors "))
if your_choice >= 3:
    print("Wrong choice!! YOU LOSE!")
    exit(0)
print(f"You choose: {images[your_choice]}")
print(f"Computer choose: {images[pc_choice]}")

if your_choice == pc_choice:
    print("Draw. . . . ")
elif your_choice == 2 and pc_choice == 0:
    print("You lose!!!")
elif pc_choice == 2 and your_choice == 0:
    print("You win ....")
elif your_choice > pc_choice:
    print("you win ....")
elif pc_choice > your_choice:
    print("You lose!!!!")