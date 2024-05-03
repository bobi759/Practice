import turtle
from turtle import Turtle


def load_screen(screen, height, width):
    screen.setup(height=height, width=width)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(2)


def render_center(playground_height):
    center = Turtle()
    center.speed(0)
    center.hideturtle()
    center.color("white")
    center.penup()
    center.pensize(3)
    center.goto(0, playground_height / 2)
    center.setheading(270)
    while center.ycor() > -playground_height / 2:
        center.pendown()
        center.forward(20)
        center.penup()
        center.forward(10)


def start_message():
    turtle.TK.messagebox.showinfo(title="Rule:", message="The first player to win 10 rounds wins the game.\n"
                                                         "Press OK to start.")


def winner(player_1, player_2):
    if player_1.wins == 10:
        return "player_1"
    elif player_2.wins == 10:
        return "player_2"
    return None
