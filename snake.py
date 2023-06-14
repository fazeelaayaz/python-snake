from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.speed("fastest")
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num - 1].xcor()
            new_y = self.turtles[turt_num - 1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for tur in self.turtles:
            tur.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]