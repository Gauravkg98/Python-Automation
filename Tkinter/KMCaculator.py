from tkinter import *

window = Tk()
window.minsize(width=500, height=700)
window.title("Convert Miles to KM")



inpput_1 = Entry(width=20)
inpput_1.grid(column=0,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row =0)

isequal_label = Label(text="is equal to")
isequal_label.grid(column=0,row = 1)

label_1 =Label(text="0",font=("Aerial",12))
label_1.grid(column=1, row=1)


label_KM = Label(text="KM")
label_KM.grid(column =2,row =1)


def calculate():
  val = float(inpput_1.get())*1.6
  label_1.config(text=f"{val}  KM")

button = Button(text="calculate", command =calculate)
button.grid(column=1,row=2)

window.mainloop()