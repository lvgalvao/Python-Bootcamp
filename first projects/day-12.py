#The number guessing game
import random

def onboarding (name):
    print(f"Welcome {name} to 'the number guessing game', be fun")
    print("I'm thinking of a number between 1 and 100.")

def set_difficulty ():
    level = input("Dou you choose play in 'easy' or 'hard'? ")
    if level == "Easy":
        return easy_level
    else:
        return hard_level

def check_answer(answer, guess):
    global current_live
    if answer > guess:
        print(f"you chose {guess} , it's a number low than the number picked")
        current_live -= 1
        print(f"you have more {current_live} ")
    elif answer < guess:
        print(f"you chose {guess} , it's a number high than the number picked")
        current_live -= 1
        print(f"you have more {current_live} ")
    else:
        print(f"you won!")
        return

hard_level = 5
easy_level = 8

name_picked = input("Welcome to Cassino, what's your name? ")
# onboarding(name_picked)

number_picked = random.randrange(1,100)
print(number_picked)

current_live = set_difficulty ()
print(current_live)

while current_live > 1:
    global hint
    hint = int(input("What number I've choise? (it's between 1 to 100)"))
    check_answer(number_picked, hint)


if current_live == 0:
    print("You lose!")


# while current_live > 0 :
