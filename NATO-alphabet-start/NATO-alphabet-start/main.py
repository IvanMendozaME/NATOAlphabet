student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
import csv
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}
print(dic_alphabet)



word = input("Introduce a word: ")
word = word.upper()
result = [dic_alphabet[i] for i in word if i in dic_alphabet.keys()]
print(result)


