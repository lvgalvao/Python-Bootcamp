from user import User

# 1. Create a greeting for your program.
print("Hello!")
# 2. Ask the user for the city that they grew up in.
city = input("What city do you grew up?")
# 3. Ask the user for the name of a pet.
pet_name = input("What is your pet's name?")
# 4. Combine the name of their city and pet and show them their band name.
user = User(city=city, pet_name=pet_name)
print("The name of your band will be " + user.band_name())
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
