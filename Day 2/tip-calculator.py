print("Welcome to the tip calculator")
bill = float(input("Wha was the total bill? "))
split = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15? "))

total = (bill * tip / 100) + bill
total_each = total / split

print(f"Each person should pay ${total_each:.2f}")