# # def greet():
# # print("hello")
# # print("how are you?")
# # print("what is your name?")

# # def greet_with_name(name):
# # print(f"hello {name}")
# # print(f"how are you {name}?")
# # print(f"what is your {name}")

# # greet_with_name("Jorge")

# def greet_with_two_parameters(name, location):
#     print(f"hello {name} are you from {location}")

# greet_with_two_parameters(location = "Jorge", name = "Brasil")

#Write your code below this line 👇


def paint_calc(height, width, cover):
    area = round(height * width, 2)
    number_of_cans = round(area/cover)
    print(f"your total area is {area}m and you need {number_of_cans} cans")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


