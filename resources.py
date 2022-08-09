from day_16 import currenty_resources

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if the ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= currenty_resources[item]:
            print(f"Sorry there is not {item} enought")
            return False
    return True

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