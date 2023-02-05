from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """Moves the turtle up by a constant"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Moves the turtle to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Returns true if turtle has crossed the finishing line"""
        return self.ycor() > FINISH_LINE_Y
