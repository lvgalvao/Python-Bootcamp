# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from email.errors import MessageError
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def output():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError as MessageError:
        print(f'O digito {MessageError} é invalido\n'
             f'Tente uma nova palavra')
        output()

    
output()
