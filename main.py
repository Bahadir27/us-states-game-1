import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
screen = turtle.Screen()
screen.title("US States Games")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)




game_on = True

while game_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What is the state?")
    data = pandas.read_csv("50_states.csv")
    # print(data.state)OOh
    state_data = data[data.state.str.lower() == answer_state.lower()]
    print(state_data)
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    is_empty = state_data.empty
    if not is_empty:
        state.goto(int(state_data.x), int(state_data.y))
        state.write(state_data.state)
        # city.write(arg=guess_city.state.to_string, move=False, align=ALIGNMENT, font=FONT)
        print(type((state_data.state.to_string())))







sas

# turtle.onscreenclick(get_mouse_click_coor)

# keeps the gif open
turtle.mainloop()

# Click exit
# screen.exitonclick()
