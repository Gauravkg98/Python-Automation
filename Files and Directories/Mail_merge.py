PLACEHOLDER = "[name]"
with open("Names.txt") as data:
  #return list as each line
  names = data.readlines()

with open("Letter.txt") as letterfile:
  letter_conetnets = letterfile.read()
  for name in names:
    stripped_name = name.strip()
    new_letter = letter_conetnets.replace(PLACEHOLDER, stripped_name)
    with open(f"F:\Swimdat\Python_codes\Files and Directories\Letter_for_{stripped_name}.docx", mode = "w") as comp_letter:
      comp_letter.write(new_letter)
    


  


