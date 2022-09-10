import turtle
import pandas as pd

FONT = ("Courier", 14, "normal")


screen = turtle.Screen()
screen.title("U.S States Game")
image = "project 25 us gaming using pandas/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("project 25 us gaming using pandas/50_states.csv")

class name_on_map(turtle.Turtle):

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
        new_data = pd.DataFrame(guessed_states)
        new_data.to_csv("save_country.csv")
        break
    if guess in df.values:
        print(f"{guess} it's a state")
        country_x = int(df[df["state"]==guess]["x"])
        country_y = int(df[df["state"]==guess]["y"])
        name_on_map(guess,country_x, country_y)
        score += 1
        guessed_states.append(guess)
        if score > high_score:
            high_score = score
    else:
        print(f"{guess} it's not")

