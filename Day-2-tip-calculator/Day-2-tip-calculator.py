#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
welcome = "Welcome to the Tip Calculator!"

print(welcome)
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip_calc = (total_bill/split) * (1 + tip/100)
# tip_calc_round = round(tip_calc,2)
tip_calc_round = "{:.2f}".format(tip_calc)

print(f"Each person should pay: ${tip_calc_round}")