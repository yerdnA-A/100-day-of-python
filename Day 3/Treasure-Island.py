print("   __________\n"
      "  /\____;;___\n"
      "  | /         /\n"
      "  `. ())oo() .\n"
      "  |\(%()*^^()^\n"
      " %| |-%-------|\n"
      "% \ | %  ))   |\n"
      "%  \|%________|\n"
      "Welcome to the treasure island")

choose = input("left or righ? ")
if choose != 'left':
    print("Fall in to a hole.\nGame Over.")
else:
    choose = input("Swim or wait? ")
    if choose != 'wait':
        print("Attacked by trout.\nGame Over.")
    else:
        choose = input("Which door ? Red, Blue or Yellow? ")
        if choose == 'red':
            print("Burned by fire. \nGame Over.")
        elif choose == 'blue':
            print("Eaten by beasts. \nGame Over.")
        elif choose == 'yellow':
            print("You win!")
        else:
            print("Game Over.")