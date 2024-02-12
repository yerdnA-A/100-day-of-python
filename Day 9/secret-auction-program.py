import os

bidder = {}

while True:
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: "))
    bidder[name] = bid
    new_bid = input("Are there any other bidders? (y/n): ").lower()
    os.system('clear')    
    if new_bid != 'y':
        break
    else:
        continue
winner = max(bidder, key=bidder.get)
print(f"The winner is {winner} with a bid of {bidder[winner]}")