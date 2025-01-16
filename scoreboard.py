from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.updatescore()


    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 48, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 48, "normal"))

    def l_win(self):
        self.l_score+=1
        self.updatescore()

    def r_win(self):
        self.r_score+=1
        self.updatescore()
