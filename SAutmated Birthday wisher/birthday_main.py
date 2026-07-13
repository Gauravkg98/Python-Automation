from  datetime import datetime
import pandas
import random
import smtplib


today = datetime.datetime.month()
today_tuple = (today.month, today.day)
my_email =""
my_pass = ""
data = pandas.read_csv("birthdays.csv")
'''
birthday_dict = {
  (birthday_month, birthday_day): data_row
}

'''

birthday_dict = {(data_row["month"], data_row['day']): data_row for (index, data_row) in data.iterrows() }

if today_tuple in birthday_dict :
  birthday_person = birthday_dict[today_tuple]
  file_path =f"letter_{random.randint(1,3)}.txt"
  with open(file_path,"r") as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]",birthday_person["name"])

  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email,my_pass)
    connection.sendmail(frpm_addr =my_email,to_addrs=birthday_person["email"],
                        msg=f"Subject: Happy Birthday!!!\n\n {contents}")


