from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 or ball.xcor()>380 or ball.distance(l_paddle)<50 or ball.xcor()<-380:
        ball.bounce_x()

    #ball misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_win()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_win()



screen.exitonclick()
