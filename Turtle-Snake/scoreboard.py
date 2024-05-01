from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Aerial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.setposition(0, 250)
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.score += 1
        self.write_score()

    def write_end(self,end_reason):
        self.clear()
        self.setposition(0, 250)
        self.write(f'Game ended! {end_reason}. Final score: {self.score}', align=ALIGNMENT, font=FONT)

