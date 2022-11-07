from tip import Tip
from calculator import Calculator


def main():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill ? $"))
    number_of_people_to_split_the_bill = int(
        input("How many people to split the bill ? $")
    )
    percentage = float(
        input("What percentage tip would you like to give? 10, 12, or 15?")
    )
    calculator = Calculator(Tip())
    result = calculator.tip_calculator(
        total_bill, number_of_people_to_split_the_bill, percentage, True
    )
    print(f"Each person should pay: ${result}")


if __name__ == "__main__":
    main()
