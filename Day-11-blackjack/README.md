## Blackjack

# House Rules 

1. The deck is unlimited in size. 
2. There are no jokers. 
3. The Jack/Queen/King all count as 10.
4. The the Ace can count as 11 or 1.
5. Use the following list as the deck of cards:
 `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
6. The cards in the list have equal probability of being drawn.
7. Cards are not removed from the deck as they are drawn.
8. The computer is the dealer.

Use [this flowchart](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt) as a guideline.

# Instructions

Create all the functions necessary to be called in the game. 

### Step 1
Create a `deal_card()` function that uses the list of cards below to *return* a random card. 
The list of cards is `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]` and `11` refers to `Ace`.

### Step 2  
Create a function called `calculate_score()` that takes a list of cards as input and returns the scores: `user_score` and `computer_score`. If there is an Ace in the `user_score` and the score is more than `21`, replace `11` with `1` and return `0` as the score.

### Step 3  
Create a function called `compare()` and pass in the `user_score` and `computer_score`. If the computer and user both have the same score, then it's a draw.  

If the computer has a blackjack (`0`), then the user loses. If the user has a blackjack (`0`), then the user wins. If the `user_score` is over 21, then the user loses. If the `computer_score` is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

Let the game begin.

### Step 4  

Deal the user and computer `2` cards each using `deal_card()` and `append()`. 

Call `calculate_score()`. If the computer or the user has a blackjack (`0`) or if the user's score is over `21`, then the game `ends`. 

### Step 5

If the game has not ended, ask the user if they want to draw another card. If yes, then use the `deal_card()` function to add another card to the `user_cards` list. If no, then the game `ends`. 

### Step 6

The score will need to be rechecked with every new card drawn and the checks in Step 4 need to be repeated until the game `ends`.

### Step 7

Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than `17`.

### Step 8

Ask the user if they want to `restart` the game. If they answer yes, `clear` the console and `start` a new game of blackjack and show the `logo` from `art.py`.

