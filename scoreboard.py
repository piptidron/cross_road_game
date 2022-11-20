from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()

    def next_level(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 72, "normal"))

    def finish_board(self):
        self.goto(0, 0)
        self.write("You have won! ", align="center", font=("Courier", 50, "normal"))
