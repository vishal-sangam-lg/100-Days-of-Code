import turtle
from turtle import Turtle, Screen
import random

# import heroes

tim = Turtle()
turtle.colormode(255)

# tim.shape("turtle")
# tim.color("red")

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(num_sides):
    """Draws any shape given the number of sides as input"""
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


# Draw all shapes
# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(i)

# Draw Random Walk
# tim.speed("fastest")
# tim.pensize(15)
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Draw a Spirograph
def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

# print(heroes.gen())

screen = Screen()
screen.exitonclick()
