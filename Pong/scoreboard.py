from turtle import Turtle

FONT = ('Press Start 2P', 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.__define_score()

    def __define_score(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 200)

    def show_scoreboard(self, player_1, player_2):
        self.write(f"{player_1.wins}   {player_2.wins}", move=False, align='center', font=FONT)

    def show_winner(self, winner):
        self.write(f"WINNER   {winner}", move=False, align='center', font=FONT)
