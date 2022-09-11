from turtle import Turtle, Screen
import pandas as pd

FONT = ("Courier", 14, "normal")
IMAGE = "/Users/lucianogalvao/Code/100DaysofCode/project 25 us gaming using pandas/blank_states_img.gif"
CSV = "/Users/lucianogalvao/Code/100DaysofCode/project 25 us gaming using pandas/50_states.csv"

screen = Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)

turtle = Turtle()
turtle.shape(IMAGE)

df = pd.read_csv(CSV)
all_states = df["state"].to_list()

class name_on_map(Turtle):

    def __init__(self, contry, x, y) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x,y)
        self.write(f"{contry}", align="left",font=FONT)

score = 0
high_score = 0
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name").title()
    if guess == "Exit":
        missing_states = [n for n in all_states if n not in guessed_states]
        new_data_missing_states = pd.DataFrame(missing_states)
        new_data_missing_states.to_csv("save_country_missing.csv")
        break
    if guess in df.values:
        print(f"{guess} it's a state")
        country_x = int(df[df["state"]==guess]["x"])
        country_y = int(df[df["state"]==guess]["y"])
        name_on_map(guess,country_x, country_y)
        score += 1
        guessed_states.append(guess)
    else:
        print(f"{guess} it's not")

