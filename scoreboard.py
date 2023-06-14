from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
MESSAGE = "GAME OVER"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 415)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_highscore(self):
        with open ("data.txt") as file:
           return int(file.read())

    def write_highscore(self):
        with open ("data.txt", mode="w") as file:
            file.write(str(self.highscore))