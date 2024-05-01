from turtle import Turtle, Screen
from random import choice
from colorgram import extract


CIRCLE_RADIUS = 20
ROWS_COUNT = 8
starting_x = -250
STARTING_Y = -250
WINDOWS_X = 600
WINDOWS_Y = 620
drawing_speed = 0

colors = extract("dots.jpg", 30)
colors.pop(0)

screen = Screen()
screen.setup(WINDOWS_X,WINDOWS_Y)


def set_start(turtle):
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(starting_x, STARTING_Y)


def draw_circle(turtle: Turtle, circle_radius, draw_speed, colors_array):
    color = "#{:02x}{:02x}{:02x}".format(*choice(colors_array).rgb)
    turtle.speed(draw_speed)
    turtle.width(3)

    turtle.hideturtle()
    turtle.penup()
    turtle.right(90)
    turtle.forward(circle_radius)
    turtle.left(90)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(circle_radius)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(circle_radius)
    turtle.right(90)
    turtle.forward(50)


def draw_line(turtle, row_x, row_y, radius, draw_speed):
    turtle.speed(draw_speed)
    turtle.setpos(row_x, row_y)

    for _ in range(6):
        draw_circle(turtle, radius, draw_speed, colors)
        turtle.forward(50)


def draw_picture(rows_count, start_of_picture_x, start_of_picture_y):
    set_start(timmy_the_turtle)
    for _ in range(rows_count):
        draw_line(timmy_the_turtle, start_of_picture_x, start_of_picture_y, CIRCLE_RADIUS, drawing_speed)
        start_of_picture_y += 75


timmy_the_turtle = Turtle()
draw_picture(ROWS_COUNT, starting_x, STARTING_Y)



screen.exitonclick()
