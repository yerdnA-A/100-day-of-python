import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []
pc_cards = []

def calc_score(cards):
    score = 0
    for card in cards:
        score += card
    return score

for i in range(0,2):
    user_cards.append(random.choice(cards))

pc_cards.append(random.choice(cards))

user_score = calc_score(user_cards)
pc_score = calc_score(pc_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {pc_cards}")

while True:

    if user_score >= 21:
        break

    prox = input("Type 'y' to get another card, type 'n' to pass: ")

    if prox == 'y':
        user_cards.append(random.choice(cards))
        user_score = calc_score(user_cards)
        pc_cards.append(random.choice(cards))
        pc_score = calc_score(pc_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")
        if user_score >= 21:
            break
        else:
            continue
    else:
        break

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
if user_score == pc_score:
    print("Draw")
elif 21 >= user_score > pc_score:
    print("You win")
else:
    print("You lose")