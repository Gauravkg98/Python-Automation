import turtle as t

turtle_colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "cyan"
]

def draw_shape(num_sides):
  angle=(360/num_sides)
  for _ in range(num_sides):
    
    t.forward(50)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(50)
    t.left(angle)
    
    


for shape_side_n in range(3,11):
  t.color(turtle_colors[shape_side_n-2])
  draw_shape(shape_side_n)

t.done()