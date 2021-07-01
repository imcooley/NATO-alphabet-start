import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phonetic_words = []

user_request = input("Enter a word: ").upper()

phonetic_words = [phonetic_dict[letter] for letter in user_request]
print(phonetic_words)