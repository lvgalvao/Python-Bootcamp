#inicio do dia 16

from menu import MENU, resources
from resources import is_resources_sufficient, make_refil
from make_coffe import make_coffee
from payment_coffee import is_transaction_successful, process_coins

profit = 0
currenty_resources = dict()
currenty_resources = resources
looping = True

while looping:
# choose = input("What would you like? (espresso/latte/cappuccino): ")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print("The resources are:")
        print(f"You have {currenty_resources['water']}ml of water")
        print(f"You have {currenty_resources['milk']}ml of milk")
        print(f"You have {currenty_resources['coffee']}ml of coffee")
        print(f"You have {profit} $ profit")
    elif choice == "stop":
        looping = False
    elif choice == "refil":
        make_refil(currenty_resources, profit)
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
