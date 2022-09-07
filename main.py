import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Function that prints the coordinate of the screen when you click on it
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

num_answers = 0
missing_states = []
data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

while num_answers < 50:
    answer_state = screen.textinput(title=f"{num_answers}/50 States Correct", prompt="Take your time and answer: ").title()
    if answer_state == "Exit":
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Guessed States.csv")
        break
    if answer_state in states_list:
        Jim = turtle.Turtle()
        Jim.hideturtle()
        Jim.pu()
        state_data = data[data["state"] == answer_state]
        Jim.goto(int(state_data.x), int(state_data.y))
        Jim.write(state_data.state.item())  # return the first item of the data
        num_answers += 1
        missing_states.append(answer_state)
