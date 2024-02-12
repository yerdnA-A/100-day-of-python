import random

rpc = ['rock', 'paper', 'scissors']
PcChoose = random.choice(rpc)

PlayerChoose = input("Whats do you choose ? Type Rock, Paper or Scissors.\n")


if PlayerChoose == PcChoose:
    print(f"Draw PC {PcChoose} you {PlayerChoose}")
elif PlayerChoose == 'rock':
    if PcChoose == 'paper':
        print(f"Pc win, PC {PcChoose} you {PlayerChoose}")
    else:
        print(f"You win, PC {PcChoose} you {PlayerChoose}")
elif PlayerChoose == 'paper':
    if PcChoose == 'scissors':
        print(f"Pc win, PC {PcChoose} you {PlayerChoose}")
    else:
        print(f"You win, PC {PcChoose} you {PlayerChoose}")
else:
    if PcChoose == 'rock':
        print(f"Pc win, PC {PcChoose} you {PlayerChoose}")
    else:
        print(f"You win, PC {PcChoose} you {PlayerChoose}")