import csv

with open("weather_data.csv") as wether:
  data = csv.reader(wether)
  temp = []
  for row in data:
    #print(row)
    #print(row[1])
    if row[1] != "Temperature (Â°C)":
      temp.append(row[1])
  #print(temp)

import pandas
data = pandas. read_csv("weather_data.csv")
#print(data)
#print(data["Weekday"])

data_dict = data.to_dict()
#print(data_dict)
tempr = data["Temperature (°C)"].to_list()
#print(len(tempr))
#print(data["Temperature (°C)"].mean())

#Get data in columns

#print(data["Condition"])
#print(data.Condition)

# Get Data in Row
#print(data[data.Condition]=="Monday")
#print(data[data.Temperature (°C)== data.Temperature (°C).max()])

monday =data[data.Weekday =="Monday"]
monday_temp = monday.temp[0]
monday_temp*9/5 +32

#create new dataframe
new_data = {
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [25, 30, 22],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}