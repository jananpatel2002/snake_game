from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("White")
        self.setpos(0, 270)
        self.refresh_scoreboard()

    def update_score(self):
        self.score += 1

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score} ", move=False, align="center",
                   font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh_scoreboard()
