from user import User


def main():
    print("Hello!")
    city = input("What city do you grew up?")
    pet_name = input("What is your pet's name?")
    user = User(city=city, pet_name=pet_name)
    print("The name of your band will be " + user.band_name())


if __name__ == "__main__":
    main()
