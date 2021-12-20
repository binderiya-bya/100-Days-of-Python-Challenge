from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def auction_winner(auction_dict):
  highest_bid = 0
  winner = ""
  for bidder in auction_dict:
    bid_amount = auction_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  clear()    
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
more_bidders = True
auction_dict = {}

while more_bidders == True:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $")) 
  auction_dict[name] = bid
  ask = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if ask == 'no':  
    more_bidders = False
    auction_winner(auction_dict)
  elif ask == 'yes':
    clear()