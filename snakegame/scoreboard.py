from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
FILE = "data.txt"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE, mode="r") as data:
            self.high_score = int(data.read())
        print(f"High Score from file: {self.high_score}")
        self.color("White")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.print()

    def print(self):
        self.clear()
        self.write(arg=f"Score: {self.score} " f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score()
        self.score = 0
        self.print()

    def write_new_high_score(self):
        with open(FILE, mode="w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
