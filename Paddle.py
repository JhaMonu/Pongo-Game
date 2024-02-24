from turtle import Turtle

class PADDLE(Turtle):

    def __init__(self, possition):
        super().__init__()
        self.forward(20)
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(possition)

    def go_up(self):
        new = self.ycor() + 20
        self.goto(self.xcor(), new)

    def go_down(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)


