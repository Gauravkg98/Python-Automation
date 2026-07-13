import smtplib

my_email = 'aaabcInfo@gmail.com'
password = 'asdf'


'''
connection = smtplib.STMP('smtp.gmail.com')

#to secure our connection only recevier can read mail
connection.starttls()
connection.login(user=my_email,password = password)
connection.sendmail(from_addr = my_email, to_addr = "newmail@yahoo.com",
                    msg="Subject:hello\n\n This is the body of my email.")
connection.close()

'''

with smtplib.STMP('smtp.gmail.com') as connection:
#to secure our connection only recevier can read mail
  connection.starttls()
  connection.login(user=my_email,password = password)
  connection.sendmail(from_addr = my_email, to_addr = "newmail@yahoo.com",
  msg="Subject:hello\n\n This is the body of my email.")


  