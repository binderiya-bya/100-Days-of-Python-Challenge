#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

# Global constants
EASY_LEVEL = 10
HARD_LEVEL = 5

# Make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

# Function to check user's guess against actual answer
def check_answer(guess, number, attempts):
  """Checks answer against guess. Returns the number of attempts remaining."""
  if guess > number:
    print("Too high.")
    return attempts - 1
  elif guess < number:
    print("Too low")
    return attempts - 1
  else:
    print(f"You win! Hooray! The answer was {number}")

def game():

  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")

  # Choose a number between 1 and 100
  number = random.randint(1,100)
  # print(number)

  # Set difficulty
  attempts = set_difficulty()

  # Repeat the guessing functionatly if get it wrong
  guess = 0
  while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number")

    # Let the user guess a number
    guess = int(input("Make a guess: "))
    
    # Track the number of attempts and reduce by 1 if they get it wrong
    attempts = check_answer(guess, number, attempts)

    if attempts==0:
      print(f"Oops, you've run out of guesses. You lose. The answer was {number}.")
      return
    elif guess != number:
      print("Guess again.")

game()

if input("Type 'y' to restart the game or 'n' to exit: ") == 'y':
  clear()
  game()