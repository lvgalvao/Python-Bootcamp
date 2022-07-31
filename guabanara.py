# # #72

# # cont = ('zero','um', 'dois', 'tres', 'quatro',
# #         'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

# # # input a number between 0 and 5

# # # while True:
# # #     num_seleted = int(input(print("input a number between 0 and 5")))
# # #     if 0 <= num_seleted <= 5:
# # #         print("you selected a validad number")
# # #         break
# # #     else: 
# # #         print("you selected a bad number, choise again")


# # # show the top >= 5
# # print(cont[:5])

# # # show buttom <= 4
# # print(cont[-4:])

# # # show the tuppla sort by asc
# # # sort_tuple_list = tuple(sorted(cont, reverse=True))
# # # sort_tuple_list = tuple(sorted(cont))
# # # print(sort_tuple_list)
# # print(sorted(cont))

# # # how is the index from 'cinco'
# # print(cont.index('cinco'))

# # 73 init

# from random import randint
# numeros = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))

# # for cont in numeros:
# #     print('f{cont}', end='')

# print(numeros)
# print(sorted(numeros))
# print(max(numeros))
# print(min(numeros))

# atividade 74 finish

# desenvolva um progrma que leia quatro valores do teclado
# e guarde-os em uma tupla

# carrinho = ('bola', 5,
#             'playstation', 10,
#             'vitrola', 3)

# for pos in range(0,len(carrinho)):
#     if pos % 2 == 0:
#         print(f'{carrinho[pos]} custa {carrinho[(pos-1)]}')

# crie um programa que tenha uma tupla com várias palavras, depois disso, voce deve mostra
# para cada palavra, quais sao as suas 'vogais'

# carrinho = ('bola',
#             'plabystataion',
#             'viatrbola')

# for p in carrinho:
#     print(f'\nNa palavra {p.upper()} temos ', end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end='')
# start list exercices

#read 5 values from a input and save then in a list

#max and min values and ther index

values = []
for len in range(0,5):
    value = int(input(f'digite um valor para a posição {len}:'))
    values.append(value)
    print(value)
    print(values)
print(values)

print(f'{max(values)} na posicao ', end='')
for i, v in enumerate(values):
    if v == max(values):
        print(f'{i}... ')

print(f'o valor minimo foi {min(values)} na posicao ', end='')
for i, v in enumerate(values):
    if v == min(values):
        print(f'{i}...', end='')
