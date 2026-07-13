import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data =pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



'''def get_mouse_click_coor(x,y):
  print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
'''
gussed_answers=[]
while len(gussed_answers) <50:

  answer_state = screen.textinput(title ="Guess the State", prompt="What's another state's name?").title()
  print(answer_state)

  
  if answer_state =="Exit":
    missing_states = []
    for state in all_states:
      if state not in gussed_answers:
        missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("All States.csv")
    break
    


  if answer_state in all_states:
    gussed_answers.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state ==answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())

  
#to keep the screen window on
#turtle.mainloop()

#screen.exitonclick()