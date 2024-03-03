number = [1,2,3]
new_numbers = [n + 1 for n in number]
print(new_numbers)

name = 'Andrey'
new_letters = [letter for letter in name]
print(new_letters)

new_range = [n * 2 for n in range(1,5)]
print(new_range)

names = ['Andrey', 'Rhian', 'Lima', 'Caio', 'Lucas']
short_names = [name for name in names if len(name) <= 4]
print(short_names)

upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)