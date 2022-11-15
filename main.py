from turtle import Screen
from food import Food
from scoreboard import Scoreboard
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

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")

game_is_on = True
# Game is on until the x or y goes over lines
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if (snake.segment_list[0].distance(food)) < 20:  # Checks if the distance between the snake and the food is < 20
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        scoreboard.refresh_scoreboard()

    if -300 < snake.segment_list[0].xcor() < 300 and -300 < snake.segment_list[0].ycor() < 300:
        game_is_on = True
    else:
        game_is_on = False
    for segment in snake.segment_list:
        if snake.segment_list[0] == segment:
            pass
        elif snake.segment_list[0].distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()

print("Game Over")
screen.exitonclick()
