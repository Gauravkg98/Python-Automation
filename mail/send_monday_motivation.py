import datetime as dt
import smtplib 
import random 
now = dt.datetime.now()
my_email = 'absndm#gmail.com'
password ='asdfgh'

weekday = now.weekday()
if weekday ==0 :
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

  print(quote)
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs='asdf@gmail.com', 
    msg = f"Subject: MOnday Motivation\n\n This is the Monday motivation Quote : {quote}")