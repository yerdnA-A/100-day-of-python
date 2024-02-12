from human_anatomy import anatomy
import random

print("Hello! Welcome to hangan of Anatomy Human!")

world = random.choice(anatomy).lower()
key_world = ''
error_count = 0
key_world = '_' * len(world)


print(f'The secret world has {len(world)} letters\n{key_world}')

while True:
    user_choice = input("What's your choice? ")

    if user_choice in world:
        for i in range(len(world)):
            if user_choice == world[i]:
                key_world = key_world[:i] + user_choice + key_world[i + 1:]
        print(key_world)

        if key_world == world:
            print("You Win!")
            break
        else:
                    continue
    else:
        error_count += 1
        if error_count == 6:
            print("Your loose!")
            break
        else:
            continue
print('End')
