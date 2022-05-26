from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# construct objects
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        # check if resource is enough
        is_sufficient = coffee_maker.is_resource_sufficient(drink)

        # process the payment
        # only if the resource is sufficient and have enough money
        if is_sufficient and money_machine.make_payment(drink.cost):

            # make coffee
            coffee_maker.make_coffee(drink)
