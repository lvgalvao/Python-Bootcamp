print("Welcome to the calculator.")
total_bill = int(input("What was the total bill ?"))
people_to_split = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

each_person = str(((total_bill * (tip_percentage/100)+total_bill) ) / people_to_split)
print("Each person should pay: " + each_person)

# print(type(total_bill))
# print(type(people_to_split))
# print(type(tip_percentage))

