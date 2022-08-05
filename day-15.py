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


# inicio do day 15

#create a coffee machine

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