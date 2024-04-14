import pandas

data = pandas.read_csv('Day 30/nato_phonetic_alphabet.csv')
while True:
    try:
        alphabetic = {row.letter: row.code for (index, row) in data.iterrows()}

        word = input('Enter a word: ').upper()
        word_code = [alphabetic[letter] for letter in word]
        print(word_code)
        break
    except KeyError:
        print("Sorry only letter in alphabet please")
        continue