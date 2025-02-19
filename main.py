import pandas as pd
import turtle

# how to get x, y of screen in turtle
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the State',
                                    prompt="What's another state name?").title()

    if answer_state == 'Exit':
        missing_states= [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame({'state': missing_states})
        new_data.to_csv("states_to_learn.csv", index=False)

        break

    if answer_state in all_states:

        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(x=state_data['x'].item(), y=state_data['y'].item())
        t.write(state_data.state.item())





screen.exitonclick()

