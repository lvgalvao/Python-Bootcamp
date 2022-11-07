# # import random

# # random_float = random.random() * 5
# # print(random_float)

# # _________

# # You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# # Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# # There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# # e.g. 1 means Heads 0 means Tails

# # import random
# # my_random_number = random.randint(0,1)
# # if my_random_number == 0:
# #     print("Heads")
# # else:
# #     print("Tails")


# # Instructions
# # You are going to write a program which will select a random name from a list of names. The person selected 
# # will have to pay for everybody's food bill.
# # Important: You are not allowed to use the choice() function.
# # Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# # For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
# # Example Input
# # Angela, Ben, Jenny, Michael, Chloe
# # Note: notice that there is a space between the comma and the next name.
# # Example Output
# # Michael is going to buy the meal today!

# # import random

# # name_string = input("write the name of all friends who eats together ")
# # names = name_string.split(", ")

# # # count the number of array
# # # select_random_person = random.randint(0,(len(names) - 1))

# # select_random_person = random.choice(names)
# # print(f"the person who will pay everything is {select_random_person}")

# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# # dirty_dozen = [fruits, vegetables]
 
# # print(dirty_dozen[1][1])

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# # split the number in 2 variables

# position_x = int(position[0])
# position_y = int(position[1])

# map[position_x - 1][position_y - 1] = "X"




# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇

import random

map_var = [rock, paper, scissors]
# rock = 0
# paper = 1
# scisoors = 2

player_1 = 0
option_player_1 = input("Choose rock, paper or scisoors ")

if option_player_1 == "rock":
    player_1 = map_var[0]
    print(f"player 1 choose \n {player_1}")
elif option_player_1 == "paper":
    player_1 = map_var[1]
    print(f"player 1 choose \n {player_1}")
else:
    player_1 = map_var[2]
    print(f"player 1 choose \n {player_1}")

player_2 = map_var[random.randint(0,2)]
print(f"player 2 choose {player_2}")

if player_1 == player_2:
    print("Draw")
elif player_1 == 0 and player_2 == 1:
    print("Player 2 wins")
elif player_1 == 0 and player_2 == 2:
    print("Player 1 wins")
elif player_1 == 1 and player_2 == 0:
    print("Player 1 wins")
elif player_1 == 1 and player_2 == 2:
    print("Player 2 wins")
elif player_1 == 2 and player_2 == 0:
    print("Player 2 wins")
elif player_1 == 2 and player_2 == 1:
    print("Player 1 wins")

