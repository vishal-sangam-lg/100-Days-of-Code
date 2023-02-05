from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creating the initial Snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Adds a new segment to the snake when it eats food"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves all the segments of snake starting from head to tail
        -> Segments follow the head and head is updated at the end"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Head is turned up. Since, all the segments follow the head, the snake moves up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Head is turned down. Since, all the segments follow the head, the snake moves down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Head is turned left. Since, all the segments follow the head, the snake moves left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Head is turned right. Since, all the segments follow the head, the snake moves right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
