# # inicio do dia 03
# # height = int(input("Qual sua altura?"))
# # if height != 190:
# #     print("Pode ir")
# # else:
# #     print("Não pode ir")

# # criar um programa para avaliar se é ímpar ou par
# var = int(input("insira um numero"))

# if var % 2 == 1:
#     print("impar")
# else:
#     print("par")

# peso = int(input("qual o seu peso?"))

# if peso > 50:
#     print("voce é pesado")
#     idade = int(input("qual sua idade?"))
#     if idade > 18:
#         print("voce pode dirigir")
#     else:
#         print("voce é magro e novo")
# elif peso > 30:
#     print("voce é médio")
# else:
#     print("voce é magro")

# height = float(input("what is your height in m? "))
# weight = float(input("what is your weight in kg? "))

# imc = weight / (height ** 2)
# if imc > 35:
#     print("clinically obese")
# elif imc > 30:
#     print("obese")
# elif imc > 25:
#     print("overweight")
# elif imc > 18.5:
#     print("normalweight")
# else:
#     print("underweight")

# which year do you want to check?

# year = int(input("which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap!")
#         else:
#             print("Don't leap")
#     else:
#         print("Leap!")
# else:
#     print ("Don't leap!")

#which pizza do you like?
# pizza price for small is 15, for medium is 20 and large is 25.
# peperoni for small is 2, for medium and large is 3.

# bill = 0

# size = input("choose a size")
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill +=25

# add_peperoni = input("voce quer peperoni?")
# if add_peperoni == "Sim":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# add_chesse = input("voce quer queijo")
# if add_chesse == "Sim":
#     bill += 2

# print(f"Your final bill is ${bill}")

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# count the number of the letters in TRUE occurs in name1 and name2

# from collections import Counter
# counter1 = Counter(name1)
# counter2 = Counter(name2)
# digito1 = str(counter1['T'] + counter1['R'] + counter1['U'] + counter1['E'] + counter2['T'] + counter2['R'] + counter2['U'] + counter2['E'])
# digito2 = str(counter1['L'] + counter1['O'] + counter1['V'] + counter1['E'] + counter2['L'] + counter2['O'] + counter2['V'] + counter2['E'])
# combine_digito1_and_digito2 = digito1 + digito2
# print(combine_digito1_and_digito2)


# Combine the 2 strings in justcount the number of the letters in LOVE occurs in name1 and name2
# Then combine these numbers to make a 2 digit number.
# Then check if the number
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."


#Write your code below this line 👇

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# combine the 2 strings in one
combined_names = name1 + name2

# pass the string to lower case
combined_names_lower = combined_names.lower()

#count the occurs
# from collections import Counter
# counter = Counter(combined_names_lower)
# digito1 = str(counter['t'] + counter['r'] + counter['u'] + counter['e'])
# digito2 = str(counter['l'] + counter['o'] + counter['v'] + counter['e'])

digito1 = str(combined_names_lower.count("t") + combined_names_lower.count("r") + combined_names_lower.count("u") + combined_names_lower.count("e"))
digito2 = str(combined_names_lower.count("l") + combined_names_lower.count("o") + combined_names_lower.count("v") + combined_names_lower.count("e"))

combine_digito1_and_digito2 = digito1 + digito2

love_number = digito1 + digito2
# print(combine_digito1_and_digito2)
print(love_number)

