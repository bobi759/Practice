from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.show_score()
        snake.extend()

    if not (-290 < snake.head.xcor() < 290 and -290 < snake.head.ycor() < 290):
        scoreboard.write_end("You bumped into a wall")
        game_is_on = False

    if snake.check_for_body_collision():
        scoreboard.write_end("You bumped into your tail")
        game_is_on = False



screen.exitonclick()
