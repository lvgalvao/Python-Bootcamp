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

year = int(input("which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap!")
        else:
            print("Don't leap")
    else:
        print("Don't leap")
else:
    print ("Don't leap!")
