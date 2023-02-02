from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Continuously move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball in y-axis when it hits top or bottom walls"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce the ball in x-axis when it hits paddle and increase speed"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball position to center and start it in opposite direction"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
