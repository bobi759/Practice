import time
from turtle import Screen
from paddle import Paddle
from ball import Ball, START_ROUND_SPEED
from scoreboard import Scoreboard
import controler

HEIGHT, WIDTH = 600, 800
PADDLE_STARTING_X = 350
game_in_on = True

screen = Screen()
controler.load_screen(screen, HEIGHT, WIDTH)
controler.render_center(HEIGHT)

ball = Ball()
paddle_1 = Paddle(-PADDLE_STARTING_X)
paddle_2 = Paddle(PADDLE_STARTING_X)
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")

screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")
scoreboard.show_scoreboard(paddle_1, paddle_2)

controler.start_message()
ball.start_new_game()
while game_in_on:
    ball.move()

    if not -280 < ball.ycor() < 280:
        ball.bounce(360)

    if (340 < ball.xcor() < 350) and (paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50):
        ball.bounce(180)

    if (-340 > ball.xcor() > -350) and (paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50):
        ball.bounce(180)

    if ball.xcor() < -380:
        paddle_2.wins += 1
        ball.start_player_1()
        scoreboard.clear()
        ball.b_speed = START_ROUND_SPEED
    #
    if ball.xcor() > 380:
        paddle_1.wins += 1
        ball.start_player_2()
        scoreboard.clear()
        ball.b_speed = START_ROUND_SPEED

    winner = controler.winner(paddle_1, paddle_2)
    if winner:
        scoreboard.clear()
        scoreboard.show_winner(winner)
        game_in_on = False
    else:
        scoreboard.show_scoreboard(paddle_1, paddle_2)

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
