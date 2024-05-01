from turtle import Turtle

STARTING_POSITIONS = [(x, 0) for x in range(0, -41, -20)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = self.__define_snake_segments()
        self.head = self.snake_segments[0]
        self.current_direction = "right"

    def __define_snake_segments(self):
        snake_parts = []
        for position in STARTING_POSITIONS:
            snake_parts.append(self.add_segment(position))
        return snake_parts

    @staticmethod
    def add_segment(position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        return new_segment

    def extend(self):
        self.snake_segments.append(self.add_segment(self.snake_segments[-1].position()))

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x, new_y = self.snake_segments[i - 1].xcor(), self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def check_for_body_collision(self):
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
