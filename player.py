from turtle import Turtle



class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(2, 2)
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(0, -270)


    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


    def finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False