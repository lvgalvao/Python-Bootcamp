#72

cont = ('zero','um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

# input a number between 0 and 5

# while True:
#     num_seleted = int(input(print("input a number between 0 and 5")))
#     if 0 <= num_seleted <= 5:
#         print("you selected a validad number")
#         break
#     else: 
#         print("you selected a bad number, choise again")


# show the top >= 5
print(cont[:5])

# show buttom <= 4
print(cont[-4:])

# show the tuppla sort by asc
# sort_tuple_list = tuple(sorted(cont, reverse=True))
# sort_tuple_list = tuple(sorted(cont))
# print(sort_tuple_list)
print(sorted(cont))

# how is the index from 'cinco'
print(cont.index('cinco'))

