from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_x):
        Turtle.__init__(self)
        self.starting_x = starting_x
        self.p_speed = 20
        self.__draw_paddle()
        self.wins = 0

    def __draw_paddle(self):
        self.goto(self.starting_x, 0)
        self.shape("square")
        self.pencolor("white")
        self.fillcolor("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()

    def move_up(self):
        if self.ycor() + self.p_speed > 240:
            return
        new_y = self.ycor() + self.p_speed
        self.sety(new_y)

    def move_down(self):
        if self.ycor() - self.p_speed < -240:
            return
        new_y = self.ycor() - self.p_speed
        self.sety(new_y)
