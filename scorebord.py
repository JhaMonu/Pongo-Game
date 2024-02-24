from turtle import Turtle
class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scorebord_update()

    def scorebord_update(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(150, 200)
        self.write(self.r_score, align="right", font=("courier", 80, "normal"))


    def l_point(self):
        self.l_score += 1
        self.scorebord_update()


    def r_point(self):
        self.r_score += 1
        self.scorebord_update()




