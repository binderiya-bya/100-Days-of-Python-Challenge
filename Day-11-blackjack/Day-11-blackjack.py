###### Our Blackjack House Rules ######

from art import logo
import random
from replit import clear

# Step 1. Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """draws a new card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Step 2. Create a function called calculate_score() that takes a list of cards as input and returns the score. 
def calculate_score(input_cards):
  """Take a list of cards and return the score calculated from the cards
  """
  if sum(input_cards) == 21 and len(input_cards) == 2:   # it has to be only two cards
    return 0
  if 11 in input_cards and sum(input_cards) > 21:
    input_cards.remove(11)
    input_cards.append(1)
  return sum(input_cards)

# Step 3. Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(input_user_score, input_computer_score):
  if input_user_score == input_computer_score:
    print("It's a draw")
  elif input_computer_score == 0:
    print("A BlackJack! Computer wins and you lose.")
  elif input_user_score == 0:
    print("A BlackJack! You win! ")
  elif input_user_score >= 21:
    print("You lose.")
  elif input_computer_score >= 21:
    print("You win!")
  else:
    diff = input_user_score - input_computer_score
    if diff > 0:
      print("Wee, you win!")
    elif diff < 0:
      print("Close, but computer wins.")


# Step 4. Deal the user and computer 2 cards each using deal_card() and append(). Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends. 

# Step 5. If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended. 

# Step 6. The score will need to be rechecked with every new card drawn and the checks in Step 4 need to be repeated until the game ends.

# Step 7. Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Step 8. Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


def blackjack():

  print(logo)

  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  game_over = False

  while game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      draw_another_card = input("Type 'y' to draw another card or type 'n' to pass. ")
      if draw_another_card == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      elif draw_another_card == 'n': 
        game_over = True
      else:
        clear()
        print(logo)
        print("Your answer is invalid. Type only 'y' or 'n'. ")
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  compare(user_score, computer_score)

if input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ") == 'y':
  blackjack()
  
while input("Type 'y' to restart the game or 'n' to exit the game. ") == 'y':
  clear()
  blackjack()