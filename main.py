import turtle




screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput('Guess the state', "Another a state's name")
# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor)


turtle.mainloop()
