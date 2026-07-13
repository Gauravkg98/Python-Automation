from turtle import Turtle, Screen
import random as r

t= Turtle()
s = Screen()
s.colormode(255)
def random_color():
  red = r.randint(0,255)
  green = r.randint(0,255)
  blue = r.randint(0,255)
 
  return(red,blue,green)



def move_forward():
  t.forward(10)

def back_ward():
  t.backward(10)

def upward():
  t.left(10)
def downward():
  t.right(10)

#for penup and pendown

def pen_up():
  t.penup() 
def pen_down():
  t.pd()



def reset_screen():
  s.clear
  
  ()
  s.colormode(255)
  t.home()
  t.penup()
  s.bgcolor(random_color())
  t.pendown()
  t.pencolor(random_color())
  t.pensize(10)

t.pencolor(random_color())
t.pensize(10)
t.speed('fastest')
s.bgcolor(random_color())
s.listen()
s.onkey(key = "w", fun=move_forward)
s.onkey(key = "s", fun=back_ward)
s.onkey(key = "a", fun=upward)
s.onkey(key="d",fun=downward)


s.onkey(key="u", fun=pen_up)
s.onkey(key="n", fun=pen_down)
s.onkey(key="r", fun=reset_screen)


s.exitonclick()
