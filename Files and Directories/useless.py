'''file = open("Snake_Highscore.txt")
contents = file.read()
print(contents)
file.close()'''

with open("Snake_Highscore.txt") as file:
  contents = file.read()
  print(contents)

#relative path
with open("Snake_Highscore.txt", mode="w") as file:
  file.write("addingf a new text")