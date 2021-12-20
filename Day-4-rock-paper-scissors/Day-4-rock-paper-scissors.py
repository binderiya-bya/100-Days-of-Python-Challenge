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
---'   ____)____
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

#Write your code below this line 👇

ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

set = [rock, paper, scissors]

if ans==0 or ans==1 or ans==2:
  print(set[ans])
else: 
  print("Please choose from 0, 1, or 2.")

import random 
ans_com = random.randint(0,2)

if ans==0 or ans==1 or ans==2:
  print(f"Computer chose: \n{set[ans_com]}")

if ans==0 and ans_com==0:
  print("Try again.")
elif ans==0 and ans_com==1:
  print("You lost!")
elif ans==0 and ans_com==2:
  print("You win!")

if ans==1 and ans_com==0:
  print("You win!")
elif ans==1 and ans_com==1:
  print("Try again.")
elif ans==1 and ans_com==2:
  print("You lost!")

if ans==2 and ans_com==0:
  print("You lose!")
elif ans==2 and ans_com==1:
  print("You win!")
elif ans==2 and ans_com==2:
  print("Try again.")