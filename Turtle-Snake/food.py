from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
