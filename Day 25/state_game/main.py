import turtle
import pandas

screen = turtle.Screen()
screen.title("Brasil State Game")
screen.setup(width=900 , height=900)
image = 'Day 25/state_game/Brazil_Map.gif'
screen.addshape(image)

turtle.shape(image)
turtle.speed(0)

data = pandas.read_csv('Day 25/state_game/estado_brasil.csv')
all_states = data.Estado.to_list()
guessed_states = []

while len(guessed_states) <= 27:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 States Correct",
                                    prompt="What's another state's name").title()
    
    if answer_state == 'Exit':
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.Estado == answer_state]
        t.goto(int(state_data.X), int(state_data.Y))
        t.write(answer_state)

with open("Day 25/state_game/states_to_learn.csv", 'w') as miss_state:
    for m in all_states:
        if m not in guessed_states:
            miss_state.write(f"{m}\n")