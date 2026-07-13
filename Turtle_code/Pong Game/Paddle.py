from turtle import Turtle

class paddle(Turtle):
  
  def __init__(self,position):
    super().__init__()
    self =Turtle()
    self.shape("square")
    self.color("yellow")
    self.shapesize(stretch_wid=5,stretch_len=1)
    self.penup()
    self.goto(position)

  def go_up(self):
    new__y=self.ycor()+20
    self.goto(self.xcor(),new__y)

  def go_down(self):
    new__y=self.ycor()-20
    self.goto(self.cor(),new__y)
