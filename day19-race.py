from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Who will win?")

tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x=-230, y=-100)

adam = Turtle(shape="turtle")
adam.penup()
adam.color("blue")
adam.goto(x=-230, y=-66)

dar = Turtle(shape="turtle")
dar.penup()
dar.color("green")
dar.goto(x=-230, y=-33)

jim = Turtle(shape="turtle")
jim.penup()
jim.color("yellow")
jim.goto(x=-230, y=0)

joe = Turtle(shape="turtle")
joe.penup()
joe.color("purple")
joe.goto(x=-230, y=33)

grace = Turtle(shape="turtle")
grace.penup()
grace.color("orange")
grace.goto(x=-230, y=66)

screen.exitonclick()
