# Importing packages

from turtle import Turtle, Screen
from prettytable import PrettyTable
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Timmy the Turtle

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.left(90)
timmy.circle(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Pokemon table

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# Coffee maker machine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
