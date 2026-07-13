from tkinter import *
from PIL import Image, ImageTk
import pandas
import random
try: 

  data =pandas.read_csv("filename.csv")
  to_learn = data.to_dict(orient="records")
  current_card ={}
except FileNotFoundError:
  original_data = pandas.read.csv("frenchwords.csv")
  to_learn = original_data.to_dict(orient = "records")
else:
  to_learn = data.to_dict(orient="records")


def next_card():
  global current_card,flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  print(current_card['French'])
  canvas.itemconfig(card_title, text='French',fill='black')
  canvas.itemconfig(card_word,text = current_card['French'],fill='black')
  canvas.itemconfig(card_background,image = card_front_img)
  window.after(3000, func=flipCard)
  flip_timer=window.after(3000,func =flipCard)


def flipCard():
  canvas.itemconfig(card_title, text ="English",fill='white')
  canvas.itemconfig(card_word,text = current_card["English"] ,fill='white')
  canvas.itemconfig(card_background,image = card_backimage)

def is_known():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv("words_to_learn.csv",index=False)

  next_card


LIME_GREEN="#addfad"
FONT = ("Ariel",40,"italic")
window = Tk()
window.title("Flashy")
window.config(bg=LIME_GREEN,padx=50,pady=50)

flip_timer = window.after(3000, func=flipCard)



canvas = Canvas(height=500, width=800,highlightthickness=0,bg="white")

card_front_img = ImageTk.PhotoImage(file="white_bg.png")
card_backimage = ImageTk.PhotoImage(file="tomato.png")
card_background = canvas.create_image(300,200,image =card_front_img)
card_title = canvas.create_text(400,150,text="", font=FONT)
card_word  = canvas.create_text(400,263,text = "",font=FONT)
#canvas.config(bg="white",highlightbackground=0)
canvas.grid(row=0,column=0,columnspan=3)

crossImage = ImageTk.PhotoImage(file="wrong.png")
unknow_button =Button(image=crossImage,command=next_card)
unknow_button.grid(row=1,column=0)


tickImage = ImageTk.PhotoImage(file="tick.png")
know_button =Button(image=tickImage,command=next_card)
know_button.grid(row=1,column=1)



window.mainloop()