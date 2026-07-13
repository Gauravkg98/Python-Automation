import datetime as dt

now =dt.datetime.now()

year = now.year
month = now.month

doy = now.weekday()

hour = now.hour
#print(f"{now}   {year}   {month}   {doy}   {hour}")

dob = dt.datetime(year=1998, month = 03, day = 25, hour=5)
print(dob)