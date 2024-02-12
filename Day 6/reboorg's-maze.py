'''object_here(6)
while True:
    pause()
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            continue
    elif right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    if at_goal():
        done()
    else:
        continue'''