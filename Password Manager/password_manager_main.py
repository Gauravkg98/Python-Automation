from PIL import Image, ImageTk 
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)






#Password Generate
def generate_password():
  lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  numbers= list(range(1,11))
  special_chars = [
      '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
      '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
      ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
  ]

  nr_letters= random.randint(8,10)
  nr_symbols = random.randint(2,4)
  nr_numbers = random.randint(2,4)
  password_letters =[random.choice(lowercase_alphabets) for _ in range (nr_letters)]
  password_symbols =[random.choice(special_chars) for _ in range (nr_symbols)]
  password_numbers =[random.choice(numbers) for _ in range (nr_numbers)]
  
  password_list = password_letters +password_symbols + password_numbers

  #a= random.shuffle(password_list)
  print(password_list)
  password = "".join(password_list)
  print(password)
  password_entry.insert(0,password)
  pyperclip.copy()

def saved():
  website =website_entry.get()
  email =email_entry.get()
  password =password_entry.get()
  new_data={
    website:{
      "email":email,
      "password":password,
    }
  }
  if len(website) ==0 or len(password)==0:
    messagebox.showinfo(title="oooPs",message=" You left any filed empty")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f" These are the details entered: \nEmail : {email} \nPassword : {password}\n IS it ok to save")

    if is_ok:
      try:
        with open ("data.json","r") as data_file:
          #only for first time
          #json.dump(new_data,data_file)
          
          #readingold data
          data = json.load(data_file)
      except FileNotFoundError:
          with open("data.json","w") as data_file:
            json.dump(data_file)

        
      else:
          #updating old data
          data.update(new_data)

        
          with open("data.json","w") as data_file:
            #saving updated data
            json.dump(data,data_file,indent=4)
          
            print(data)
            website_entry.delete(0, END)
            password_entry.delete(0,END)

            messagebox.showinfo(title="Thank you",message="Password Saved")

 

image_lock = ImageTk.PhotoImage(file="lock_1.png")
canvas= Canvas(width=512, height=512, highlightthickness=0)
canvas.grid(row=0,column=1)
canvas.create_image(256,256, image=image_lock)
#canvas.pack()


#Labels
website_label =Label(text="Website : ",fg="blue")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username : ",fg="blue")
email_label.grid(row=2,column=0)
password= Label(text="password : ",fg="blue")
password.grid(row=3,column=0)

#Entries 
website_entry = Entry(width =21)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry= Entry(width =21)
email_entry.insert(0,"example@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry= Entry(21)
password_entry.grid(row=3,column=1)


def findPassword():
 website=website_entry.get()
 try: 
  with open("data.json") as data_file:
      data = json.load(data_file)
      print(data)
 except FileNotFoundError:
      messagebox.showinfo(title="Error", message="No Data File Found.")
 else:
    if website in data:
      email = data[website]["email"]
      password - data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No Details for{website} exists. ")

  
#button
search_button = Button(text="Search",width=13,command=findPassword)
search_button.grid(row=1,column =2)


generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Radiobutton(text="Add",width=36,command=saved)
add_button.grid(row =4,column=1,columnspan=2)

window.mainloop()