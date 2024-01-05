import random
from turtle import Turtle, Screen
import heroes

print(heroes.gen())

timmy_the_turle = Turtle()

timmy_the_turle.shape("turtle")
timmy_the_turle.color("red")
def forward_dashed_line(iterations):
    for i in range(iterations):
        timmy_the_turle.forward(10)
        timmy_the_turle.pu()
        timmy_the_turle.forward(10)
        timmy_the_turle.pd()

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turle.forward(120)
        timmy_the_turle.right(angle)

# for i in range(4, 20):
#     draw_shape(i)

colours = ["red", "blue", "yellow", "green", "firebrick", "gold", "pale violet red","blue violet"]

timmy_the_turle.width(3)
timmy_the_turle.speed(100)
def walk_random(forward_amount):
    timmy_the_turle.forward(forward_amount)
    left_or_right = random.randint(1,2)
    if left_or_right == 1:
        timmy_the_turle.right(90)
    elif left_or_right == 2:
        timmy_the_turle.left(90)
    red_amount_random = random.random()
    green_amount_random = random.random()
    blue_amount_random = random.random()
    timmy_the_turle.color((red_amount_random, green_amount_random, blue_amount_random))

while True:
    walk_random(15)

screen = Screen()
screen.exitonclick()