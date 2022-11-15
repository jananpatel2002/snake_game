from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
starting_positions = [(0, 0), (0, -20), (0, 40)]


class Snake:

    def __init__(self):
        self.xcor = 20
        self.ycor = 0
        self.segment_list = []
        # This initializes the 3 squares
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.speed("fastest")
        snake.hideturtle()
        snake.color("white")
        snake.penup()
        snake.showturtle()
        snake.setpos(position)
        snake.showturtle()
        self.segment_list.append(snake)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):  # Loops through all the segments to segment_list[0]
            self.segment_list[seg_num].goto(self.segment_list[seg_num - 1].pos())

        self.segment_list[0].forward(20)

    def up(self):
        if not self.segment_list[0].heading() == DOWN:
            self.segment_list[0].setheading(UP)

    def down(self):
        if not self.segment_list[0].heading() == UP:
            self.segment_list[0].setheading(DOWN)

    def left(self):
        if not self.segment_list[0].heading() == RIGHT:
            self.segment_list[0].setheading(LEFT)

    def right(self):
        if not self.segment_list[0].heading() == LEFT:
            self.segment_list[0].setheading(RIGHT)
