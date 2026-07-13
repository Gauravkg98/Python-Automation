from turtle import Turtle, Screen
from Paddle import paddle
from ball import Ball
from Scoreboard import scoreb
import time
s = Screen()

s.bgcolor("black")
s.setup(width=800,height=600)
s.title("PONG")
s.tracer(0)

r_paddle =paddle((350,0))
l_paddle =paddle((-350,0))
score = scoreb()
s.listen()

s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")

s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
  time.sleep(b.move_speed())
  s.update()
  b=Ball()
  b.move()


  #detect collison ewwith ball
  if b.ycor()> 280 or b.ycor()<-280:
    #need to bounce
    b.bounce_y()
  #detect collison with paddle
  if b.distance(r_paddle)<50 and b.xcor()>320 or b.distance(l_paddle)<50 and b.xcor()< -320 : 
    b.bounce_x()

  #detect r paddle misses ball
  if b.xcor()>380:
    b.reset_position()
    score.l_point()
  #detect l paddle misses ball
  if b.xcor()<-380:
    b.reset_position()
    score.l_point()
s.exitonclick()