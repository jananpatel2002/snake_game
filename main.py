from turtle import Screen, Turtle
import time

snake_squares = []
xcor = 20
ycor = 0  # default positions before increments


def move_forward():
    for square in snake_squares:
        square.forward(20)
    screen.update()


def move_backwards():
    for square in snake_squares:
        square.backward(20)
    screen.update()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backwards, key="Down")

for _ in range(3):
    snake = Turtle(shape="square")
    snake.speed("slowest")
    snake.hideturtle()
    snake.color("white")
    snake.penup()
    snake.showturtle()
    snake.setpos(xcor - 20, ycor)
    snake.showturtle()
    ycor = snake.ycor()
    xcor = snake.xcor()
    snake_squares.append(snake)
screen.update()

if -280 < snake_squares[0].xcor() < 280:
    print("Hello there")

screen.exitonclick()
