# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in 
# the given sentence and calculates the number of letters in each word.

# Try Googling to find out how to convert a sentence into a list of words.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# Example Output
# {
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }

result = 0
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

result = {key:len(key) for (key) in sentence.split()}
print(result)

# Convert to JSON:
import json
y = json.dumps(result, indent=4)
print(y)
print(type(y))

with open("project 26 list comprehension NATO alphabet /Output/exe_02.json", "w") as file:
    json.dump(result, file, indent=4)

# print(result)

