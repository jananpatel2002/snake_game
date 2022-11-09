from turtle import Turtle


class Snake:
    def __init__(self):
        self.xcor = 20
        self.ycor = 0
        self.segment_list = []
        # This initializes the 3 squares
        for _ in range(3):
            snake = Turtle(shape="square")
            snake.speed("slowest")
            snake.hideturtle()
            snake.color("white")
            snake.penup()
            snake.showturtle()
            snake.setpos(self.xcor - 20, self.ycor)
            snake.showturtle()
            self.ycor = snake.ycor()
            self.xcor = snake.xcor()
            self.segment_list.append(snake)

    def move(self):

        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            self.segment_list[seg_num].goto(self.segment_list[seg_num - 1].pos())
            # print(seg_num)
        self.segment_list[0].forward(20)

