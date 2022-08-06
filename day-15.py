

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
    "water": 0,
    "milk": 200,
    "coffee": 100,
}

currenty_resources = dict()
currenty_resources = resources



# inicio do day 15
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

while looping:
# choose = input("What would you like? (espresso/latte/cappuccino): ")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print("The resources are:")
        print(f"You have {currenty_resources['water']}ml of water")
        print(f"You have {currenty_resources['milk']}ml of milk")
        print(f"You have {currenty_resources['coffee']}ml of coffee")
    elif choice == "stop":
        looping = False
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            process_coins()