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

# values = []
# for len in range(0,5):
#     value = int(input(f'digite um valor para a posição {len}:'))
#     values.append(value)
#     print(value)
#     print(values)
# print(values)

# print(f'{max(values)} na posicao ', end='')
# for i, v in enumerate(values):
#     if v == max(values):
#         print(f'{i}... ')

# print(f'o valor minimo foi {min(values)} na posicao ', end='')
# for i, v in enumerate(values):
#     if v == min(values):
#         print(f'{i}...', end='')

#usuario digite n numeros
#caso o numero seja repetido nao adicionar e informar o usuário para digitar um novo numero
#exibir a lista em ordem crescente

# list = []
# append_list = True
# #usuario digite n numeros
# while append_list is True:
#     global num_candidato
#     num_candidato = input('digite um valor: ')
#     if num_candidato in list:
#         print('valor duplicado, não foi adicionado')
#     else:
#         print('valor adicionar com sucesso')
#         list.append(num_candidato)
#     keep = input(print('Quer continuar? [S/N]'))
#     if keep == 'N':
#         append_list = False
# #usuario digite n numeros

# print(list.sort())

# numeros = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in numeros:
#         numeros.append(n)
#         print('numero adicionado com sucesso')
#     else:
#         print('numero duplicado, nao adicionado')
#     r = str(input('Quer continuar? [S/N]'))
#     if r in 'Nn':
#         break

# print('-='* 30)
# print(f'voce digitou os valores {numeros}')
# numeros.sort()
# print(f'voce digitou os valores {numeros}')

#crie um programa onde o usuario possa

#make a function where the users type 5 numbers e put this numbers in a list ordered, dont use sort()

# sort_list = list()
# for c in range(0,5):
#     number = int(input('digite um numero :'))
#     if c == 0:
#         sort_list.append(number)
#     elif number >= sort_list[-1]:
#         sort_list.append(number)
#     else:
#         pos = 0
#         while pos < len(sort_list):
#             if number <= sort_list[pos]:
#                 sort_list.insert(pos,number)
#                 break
#             pos += 1

# print(sort_list)

pessoas = {'nome': 'gustavo', 'sexo': 'm'}
print(pessoas.items())

brasi
