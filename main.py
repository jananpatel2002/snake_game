from turtle import Screen
from snake import Snake
import time

snake_squares = []
xcor = 20
ycor = 0  # default positions before increments


# def move_forward():
#     for square in snake_squares:
#         square.forward(20)
#     screen.update()


# def move_backwards():
#     for square in snake_squares:
#         square.backward(20)
#     screen.update()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

# screen.listen()
# screen.onkey(fun=move_forward, key="Right")
# screen.onkey(fun=move_backwards, key="Left")


snake = Snake()
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # the last square is where the second to last square is

# if -280 < snake_squares[0].xcor() < 280:
#     print("Hello there")


screen.exitonclick()
