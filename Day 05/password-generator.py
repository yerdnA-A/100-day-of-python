import random
import string
print("Welcome to the PyPassword Generator!")
many_letter = int(input("Hom many letter you like in your password?\n"))
many_symbol = int(input("How many symbols you like?\n"))
many_number = int(input("And numbers?\n"))

password = []

for i in range(0,many_letter):
    password.append(random.choice(string.ascii_letters))


for i in range(0, many_symbol):
    password.append(random.choice(string.punctuation))


for i in range(0,many_number):
    password.append(random.randint(0,9))

random.shuffle(password)

passwordAll = ''.join(map(str, password))
print(f"Here's your password: {passwordAll}")