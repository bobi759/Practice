import random
from turtle import Turtle, Screen, textinput


def create_turtle(t_color, turtle_x, turtle_y):
    global STARTING_Y
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color(t_color)
    timmy.penup()
    timmy.goto(turtle_x, turtle_y)
    STARTING_Y += 50
    return timmy


def winner_of_race(turtles_of_race, maximum_pace, finish_line_x):
    while all(t.pos()[0] < finish_line_x for t in turtles_of_race):
        [turtle.forward(random.randint(0, maximum_pace)) for turtle in turtles_of_race]
    return [t for t in turtles_of_race if t.pos()[0] >= finish_line_x][0]


def race_result(user_guess, winner_color):
    return "Congratulation. Your bet was right!" if user_guess == winner_color else f"You lost. The winner was the {winner_color} turtle. "


screen = Screen()
screen.setup(height=600, width=700)

STARTING_X, STARTING_Y, FINISH_LINE_X = -320, -150, 300
MAX_PACE = 20

user_bet = textinput("Make a bet", "Which turtle will finish first? ")
colors = ["red", "yellow", "orange", "blue", "green", "violet", "indigo"]
turtles = [create_turtle(color, STARTING_X, STARTING_Y) for color in colors]
turtle_winner = winner_of_race(turtles, MAX_PACE, FINISH_LINE_X)
print(race_result(user_bet, turtle_winner.fillcolor()))
screen.exitonclick()
