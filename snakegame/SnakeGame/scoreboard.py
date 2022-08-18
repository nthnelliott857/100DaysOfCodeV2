from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.print()

    def print(self):
        self.write(arg=f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)