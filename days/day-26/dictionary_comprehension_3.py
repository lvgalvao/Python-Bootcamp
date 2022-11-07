# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each 
# temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Write your code 👇 below:

weather_f = {key:((value * 9/5) + 32) for (key, value) in weather_c.items()}
print(weather_f)

#save to a json file
import json
with open("project 26 list comprehension NATO alphabet /Output/weather_f.json", "w") as file:
    json.dump(weather_f, file, indent=4)
