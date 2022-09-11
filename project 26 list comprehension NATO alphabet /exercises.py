#list comprehension NATO alphabet
NUMBERS = [1 ,2 ,3]
NAMES = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_numbers_2 = []

#tradicional way to create a new list
for n in NUMBERS:
    new_item = n + 1
    new_numbers_2.append(new_item)
# print(new_numbers_2)

#pytonic code to create a new list
new_numbers = [n + 1 for n in NUMBERS]
# print(new_numbers)

#create a new list from a range, where the list items are double the values in the range
new_list_double = [n * 2 for n in range(1,4)]
# print(new_list_double)

#conditional list comprehension
# new_list = [new item for item in list if item]
new_list_names = [n for n in NAMES if len(n) <= 4]
# print(new_list_names)

#conditional list comprehension turn names UPPER
new_list_names_2 = [n.upper() for n in NAMES if len(n) > 4]
# print(new_list_names_2)

#squaring numbers using conditional list
NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in NUMBERS]
# print(squared_numbers)

#filtering even numbers
odd_numbers = [n for n in NUMBERS if n%2 == 0]
# print(odd_numbers)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both file

# task 1 , create new list using the numbers in these files
# task 1.1, create a class how read a txt file and strip the itens

from read_and_strip import Read_and_strip

# task 2 , create a new list when the numbers are commun in both list

# with open("/Users/lucianogalvao/Code/100DaysofCode/project 26 list comprehension NATO alphabet /file.txt") as file1:
#     list_file1 = file1.readlines()
#     new_list_file1_striped = []
#     for item in list_file1:
#         new_item_striped = item.strip()
#         new_list_file1_striped.append(new_item_striped)


# with open("/Users/lucianogalvao/Code/100DaysofCode/project 26 list comprehension NATO alphabet /file2.txt") as file2:
#     list_file2 = file2.readlines()
#     new_list_file2_striped = []
#     for item in list_file2:
#         new_item_striped_2 = item.strip()
#         new_list_file2_striped.append(new_item_striped_2)

list1 = Read_and_strip.read(url="/Users/lucianogalvao/Code/100DaysofCode/project 26 list comprehension NATO alphabet /file.txt")
list2 = Read_and_strip.read(url="/Users/lucianogalvao/Code/100DaysofCode/project 26 list comprehension NATO alphabet /file2.txt")

print(list1)
print(list2)

# task 2 , create a new list when the numbers are commun in both list

commun_numbers = [n for n in list1 if n in list2 ]
commun_numbers
print(commun_numbers)