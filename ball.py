from turtle import Turtle, Screen
# import time

screen = Screen
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
       x = self.xcor() + self.x_move
       y = self.ycor() + self.y_move
       self.goto(x, y)


    def bounce_y(self):
        self.y_move *= -1
        # self.screen.sleep(0.1)


    def bounce_x(self):
        self.x_move *= -1
        # self.screen.sleep(0.1)



    def reset_possotion(self):
        self.goto(0,0)
        self.bounce_x()

    def reset_agian(self):
        self.goto(0,0)
        self.bounce_x()

