from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the level"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level by 1"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Prints Game Over on screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="left", font=FONT)
