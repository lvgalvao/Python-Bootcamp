
CSV_DICT = "project 26 list comprehension NATO alphabet /Input/nato_phonetic_alphabet.csv"

import pandas as pd

#TODO 1. Create a dictionary in this format: Convert the CSV in a Dictionary

df = pd.read_csv(CSV_DICT)
# print(df)

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# df_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(df_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("enter a word :").upper()
output_list = [phonetic_dict[letter] for letter in name]

# phonetic_code = [df_dict.values() for split_name_list in df_dict.keys()]
# print(phonetic_code)

print(output_list)