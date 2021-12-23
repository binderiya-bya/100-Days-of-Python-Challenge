from art import logo
from art import vs
from game_data import data
import random


# Define a function that chooses winner
def compare(a, b):
    count_a = a['follower_count']
    count_b = b['follower_count']
    winner_temp = ""

    if count_a > count_b:
        winner_temp = 'A'
    elif count_a < count_b:
        winner_temp = 'B'
    return winner_temp


# track score
score = 0

# while loop till get it wrong
game_over = False
B = random.choice(data)

while not game_over:

    print(logo)
    # Randomly choose a person from dictionary list
    A = B
    B = random.choice(data)
    if A == B:
        A = random.choice(data)

    # Make an f string with the values
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    # Ask the input
    choice = input("Who has more followers? Type 'A' or 'B': ")

    # check winner against choice
    winner = compare(A, B)

    if choice == winner:
        score += 1
        print(f"You're right! Current score: {score}")

    elif choice != winner:
        print(f"Sorry, that's wrong. Final score: {score} ")
        game_over = True

