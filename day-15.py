MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
currenty_resources = dict()
currenty_resources = resources



# inicio do day53 15
#create a coffee machine
looping = True

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if the ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= currenty_resources[item]:
            print(f"Sorry there is not {item} enought")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total +=int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficiente."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ☕ ")

def make_refil(resources, current_money):
    """Add ingredients to the machine for 1$"""
    global profit
    cost_refil = 1
    if profit >= cost_refil:
        for item in resources:
            resources[item] += 300
        profit -=cost_refil
        print(f"now your machine has coffee")
    else:
        print("You need money to the refil")

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
