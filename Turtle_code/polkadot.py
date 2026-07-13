
import turtle as turtle_module
import random as r
t = turtle_module.Turtle()

turtle_module.colormode(255)
def random_color():
  red = r.randint(0,255)
  blue = r.randint(0,255)
  green = r.randint(0,255)


  rand_col=(red,blue,green)
  return rand_col
num = 100
t.speed(10)

t.hideturtle()
#turtle is the arrow in graphgics
t.showturtle()
for dot_count in range(1,num):
  t.dot(20,(random_color()))
  t.penup()
  t.forward(50)
  t.pendown()
  if dot_count % 10 ==0:

    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
    t.pendown()


screen = turtle_module.Screen()
screen.screensize(1000,1000)
screen.exitonclick()