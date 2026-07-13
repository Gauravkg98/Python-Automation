from tkinter import *
from PIL import Image, ImageTk 
import json

PINK ="#e2979c"
RED = "#7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME ="Courier"
WORK_MIN=1
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps = 0
timer=None
#Count timer

import time
import math
'''count = 5
while True:
  time.sleep(1)
  count -=1  '''

def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text ="00:00")
  title_label.config(text="Timer")
  check_marks.config(text="")
def start_timer():
  global reps
  reps +=1

  work_sec = WORK_MIN *60
  short_break_sec = SHORT_BREAK_MIN *60
  long_break_sec = LONG_BREAK_MIN * 60

  
  if reps % 8 ==0:
    count_down(long_break_sec)
    title_label.config(text="BREAK", fg= RED)

  elif reps % 2==0:
    count_down(short_break_sec)
    title_label.config(text="BREAK", fg= PINK)
  else:
    count_down(work_sec)
    title_label.config(text="WORK", fg= GREEN)

def count_down(count):
  count_min = math.floor(count/60)
  count_sec = count %60
  if count_sec < 0:
    count_sec =f"0{count_sec}"

  canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
  #print(count)
  if count>0:
    global timer
    timer=window.after(1000,count_down, count-1)
  else:
    start_timer()
    mark=""
    work_sessions=math.floor(reps/2)
    for _ in range(work_sessions):
      mark +="✓"
    check_marks.config(text=mark)


# UI Setup 

window = Tk()
window.title("Pomodoro")
window.config( padx=10,pady=10,bg=YELLOW)

title_label = Label(text="Timer",fg = GREEN,font=(FONT_NAME,35,"bold"))
title_label.grid(column=1, row = 1)
canvas= Canvas(width=270, height=300, bg=YELLOW, highlightthickness=0)

tomato_img=ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(135,150, image=tomato_img)
timer_text = canvas.create_text(100,150,text="00:00",fill="blue",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=0)
start_timer()
start_button = Button(text="Start",highlightthickness=0, command= start_timer)
start_button.grid(column=0, row =2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row =2)

check_marks = Label(text="✓",fg= "black",bg=YELLOW)
check_marks.grid(column = 1, row =3)
#canvas.pack()
window.mainloop()