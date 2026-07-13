import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260420.csv")
gray_squirel = data[data["Primary Fur Color"]=="Gray"]
Cinnamon_squirel = data[data["Primary Fur Color"]=="Cinnamon"]
black_squirel = data[data["Primary Fur Color"]=="Black"]

gray_squirel_count =len(gray_squirel)
Cinnamon_squirel_count =len(Cinnamon_squirel)
black_squirel_count = len(black_squirel)

data_dict={
"Fun Color":["Gray","Cinnamon","Black"],
"Count" : [gray_squirel_count, Cinnamon_squirel_count,black_squirel_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirel_count.csv")