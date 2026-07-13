import statistics

Folder ="F:\\wimdat"
filename = "Darius-13-100m-FLY.txt"


def read_swim_data(filename):
  
  swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

  with open (Folder+filename) as file:
    lines = file.readlines()
    times = lines[0].strip().split(",")
  convert = []
  for t in times:
    if ":" in t:
      minutes, rest = t.split(":")
      seconds, hunderth = rest.split(".")
    else:
      mintues = 0
      seconds,hunderth = t.split(":")
  
  convert.append((int(minutes)*60*100)+(int(seconds)*100)+int(hunderth))

  average=statistics.mean(convert)
  min_secs, hunderths =str(round(average/100,2)).split(".") 
  min_secs = int(min_secs)

  minutes = min_secs
  seconds = min_secs - (minutes*60)
  average = str(mintues)+" : "+str(seconds)+" . "+int(hunderths)
  print(swimmer)

  return swimmer, age, stroke, distance, times, average

