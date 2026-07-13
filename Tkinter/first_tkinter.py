from  tkinter import *
window = Tk()
window.title("First GUI")
window.minsize(width = 500, height=300)
window.config(padx=20,pady=20,bg="orange")

#label
my_label =Label(text="this is a label", font=("Aerial",24,"bold"),bg="orange",fg="red")
#my_label.pack()


#both are same
my_label["text"]="New Text"
my_label.config(text="new text")

#my_label.place(x=0,y=0) absolute

#grid system relative to other system
my_label.grid(column=2,row=1)

def button_clicked():
  print("button clicked")
  w = imput.get()
  my_label.config(text = w)
#button
button = Button(text="click me", command = button_clicked)
#button.pack()
#button.place(x=200,y=0)
button.grid(column=2,row=2)

imput = Entry(width =10)
#imput.pack()
#mput.place(x=200,y=30)
imput.grid(column=2,row=4)

print(imput.get())
#must use mainloop to hold the window use at last of code to reflect everything
window.mainloop()