from turtle import Turtle, Screen 

tim = Turtle()
tim.shape("turtle")

screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(key="w", fun=move_forward )
screen.onkeypress(key="s", fun=move_backward )  
screen.onkeypress(key="a", fun=turn_left )
screen.onkeypress(key="d", fun=turn_right )
screen.onkeypress(key="c", fun=clear ) 

#when the key is presses for long time




screen.listen()
screen.exitonclick()
