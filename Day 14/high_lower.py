import os
import random
from game_data import data

score = 0
while True:

    if score == 0:
        A = random.choice(data)
        B = random.choice(data)
        print(f"Compare A: {A['name']} {A['description']} {A['country']}")
        print("Or")
        print(f"Compare B: {B['name']} {B['description']} {B['country']}")
    else:
        A = random.choice(data)
        B = win
        print(f"Compare A: {A['name']} {A['description']} {A['country']}")
        print("Or")
        print(f"Against B: {B['name']} {B['description']} {B['country']}")

    A_follow = A['follower_count']   
    B_follow = B['follower_count']

    choice = input("Who has more followers? Type A or B: ")

    os.system('clear')

    if choice == 'a' and A_follow > B_follow:
        score += 1
        print(f"You're right! Current score: {score}")
        win = A
    elif choice == 'b' and B_follow > A_follow:
        score += 1
        print(f"You're right! Current score: {score}")
        win = B
    else:
        break

print(f"You lose, your score {score}")