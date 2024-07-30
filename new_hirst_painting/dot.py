from turtle import Turtle, Screen
from main import color_list
import random

def select_color():
    return random.choice(color_list)

def rgb_to_turtle_color(rgb):
    return "#%02x%02x%02x" % rgb

print(select_color())
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setposition(-370, -300)
def draw_dot(x):
    timmy.pendown()
    for _ in range(x):
        timmy.penup()
        timmy.dot(20,rgb_to_turtle_color(select_color()))
        timmy.forward(50)
        timmy.pendown()



def make_dot():

    for _ in range(10):
        timmy.penup()
        draw_dot(10)
        timmy.penup() 
        timmy.setposition(-370, timmy.ycor() + 50)

make_dot()
screen = Screen()
screen.exitonclick()

