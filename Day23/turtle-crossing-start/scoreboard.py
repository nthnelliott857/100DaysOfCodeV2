from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.player.game_over()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)





