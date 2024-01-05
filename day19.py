from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forwards():
    tim.forward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()