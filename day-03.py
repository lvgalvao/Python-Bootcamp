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

peso = int(input("qual o seu peso?"))

if peso > 50:
    print("voce é pesado")
    idade = int(input("qual sua idade?"))
    if idade > 18:
        print("voce pode dirigir")
    else:
        print("voce é magro e novo")
elif peso > 30:
    print("voce é médio")
else:
    print("voce é magro")