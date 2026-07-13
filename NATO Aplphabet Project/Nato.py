import pandas

data= pandas.read_csv("F:\\Swimdat\\Python_codes\\NATO Aplphabet Project\\NATO_Code_list.csv")
print(data.to_dict())
phonetic_data={row.letter:row.code for (ind, row) in data.iterrows()}

'''for index, row in data.iterrows():
  if row['code']=="Alfa":
    print("-----",index, row)'''

#print(phonetic_data)

word = input("Enter a word").upper()
output_list =[phonetic_data[letter] for  letter in word]
print(output_list)