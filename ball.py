from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
        self.move_speed=0.1

    def move(self):
        x_cor=self.xcor()+self.x
        y_cor=self.ycor()+self.y
        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y*=-1

    def bounce_x(self):
        self.x*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_y()
