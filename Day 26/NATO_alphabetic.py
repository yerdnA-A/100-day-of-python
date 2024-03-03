import pandas


data = pandas.read_csv('Day 26/nato_phonetic_alphabet.csv')



alphabetic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input('Enter a word: ').upper()
word_code = [alphabetic[letter] for letter in word]
print(word_code)
