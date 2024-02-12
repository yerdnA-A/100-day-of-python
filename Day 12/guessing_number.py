import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
secret_number = random.randint(1,100)

dif = input("Choose a difficulty. Type 'easy' or 'hard': ")

if dif == 'easy':
    attempts = 10
else:
    attempts = 5

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}")
        break
    elif guess > secret_number:
        print("Too high")
        print("Guess again")
    else:
        print("Too low")
        print("Guess again")

    if attempts == 0:
        print(f"You no have attempts! The answer was {secret_number}")
        break

    