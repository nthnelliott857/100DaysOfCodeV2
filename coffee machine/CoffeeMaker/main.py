from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
beverages = Menu()
register = MoneyMachine()


def make_coffee():
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice != "off":
        if choice == "report":
            coffee_machine.report()
            register.report()
        elif choice in beverages.get_items():
            drink = beverages.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink) and register.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
        make_coffee()


make_coffee()
