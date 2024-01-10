import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

def get_coords_click(x, y):
    print(x, y)

turtle.onscreenclick(get_coords_click)
data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter another states name:").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



turtle.mainloop()