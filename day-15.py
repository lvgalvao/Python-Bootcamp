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

currenty_resources = dict()
currenty_resources = resources


# inicio do day 15
#create a coffee machine
looping = True

while looping:
# choose = input("What would you like? (espresso/latte/cappuccino): ")
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "report":
        print("The resources are:")
        print(f"You have {currenty_resources['water']}ml of water")
        print(f"You have {currenty_resources['milk']}ml of milk")
        print(f"You have {currenty_resources['coffee']}ml of coffee")
    elif choose == "stop":
        looping = False
    elif choose == "espresso":
        # Compare resourcers if espresso < resourcers than consumin and serv")
        if (MENU["espresso"]["ingredients"]["water"]) <= currenty_resources["water"]: 
            if (MENU["espresso"]["ingredients"]["coffee"]) <= currenty_resources["coffee"]:
                print("Tome o seu espresso")
                for key in currenty_resources:   
                    currenty_resources[key] -= MENU["espresso"]["ingredients"][key]
                    print(currenty_resources) 
            else:
                print("Sem recurso disponível")
        else:
            print("Sem recurso disponível")    










print("Please insert coins.")
qte_quarters = int(input("How many quarters? "))
qte_dimes = int(input("How many dimes? "))
qte_nickles = int(input("How many nickles? "))
qte_pennies =int(input("How many pennies? "))

#print report


#check resources sufficient

# def report_quantity():


def exchange (cost, quarters, dimes, nickles, penies):
    total_money_input = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + penies * 0.01
    if total_money_input > cost:
        troco = total_money_input - cost
        print(f"você terá {troco}")
    else:
        print("dinheiro insuficiente")

# choose = input("What would you like? (espresso/latte/cappuccino): ")

# process coins

print("Please insert coins.")
qte_quarters = int(input("How many quarters? "))
qte_dimes = int(input("How many dimes? "))
qte_nickles = int(input("How many nickles? "))
qte_pennies =int(input("How many pennies? "))

exchange(5, qte_quarters, qte_dimes, qte_nickles, qte_pennies)

