from random import choice, randint
from turtle import Turtle

START_ROUND_SPEED = 15


class Ball(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.position = (0, 0)
        self.b_speed = START_ROUND_SPEED
        self.__draw_ball()

    def __draw_ball(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.fillcolor("white")
        self.goto(self.position)
        self.turtlesize(1, 1)

    def start_new_game(self):
        intervals = [(0, 20), (160, 180)]
        self.goto(0, 0)
        self.setheading(randint(*choice(intervals)))

    def start_player_1(self):
        intervals = [(0, 20), (340, 360)]
        self.goto(0, 0)
        self.setheading(randint(*choice(intervals)))

    def start_player_2(self):
        self.goto(0, 0)
        self.setheading(randint(160, 200))

    def move(self):
        self.forward(self.b_speed)

    def bounce(self, angle):
        new_heading = angle - self.heading()
        self.setheading(new_heading)
