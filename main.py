import turtle
import pandas



screen = turtle.Screen()
guessed = 0
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states = pandas.read_csv('50_states.csv')
states_names_list = states['state'].to_list()

game = True
while game:
    answer_state = screen.textinput(f'Guess the state {guessed}/50', "Another a state's name").title()
    if answer_state in states_names_list:
        state_row = states[states.state == answer_state]
        x_cor = state_row.x
        y_cor = state_row.y
        guessed += 1









# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor)


turtle.mainloop()
