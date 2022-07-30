#72
7
cont = ('zero','um', 'dois', 'tres', 'quatro',
        'cinco')

# input a number between 0 and 5

while True:
    num_seleted = int(input(print("input a number between 0 and 5")))
    if 0 <= num_seleted <= 5:
        print("you selected a validad number")
        break
    else: 
        print("you selected a bad number, choise again")


# validated then
print(cont[num_seleted])


# show that selected number write

