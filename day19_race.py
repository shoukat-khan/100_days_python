from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=600)
#draw a finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(380, 300)
finish_line.pendown()
finish_line.goto(380, -300)
finish_line.hideturtle()


#1st object
tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.penup()
tim.setposition(-370, 50)

#2nd object
tom = Turtle()
tom.shape("turtle")
tom.color("blue")
tom.penup()
tom.setposition(-370, -50)

#3rd object
tam = Turtle()
tam.shape("turtle")
tam.color("green")
tam.penup()
tam.setposition(-370, 100)

#4th object
tem = Turtle()
tem.shape("turtle")
tem.color("yellow")
tem.penup()
tem.setposition(-370, -100)


#make a loop to move the turtles
def move():
    while True:
        tim.forward(random.randint(1, 10))
        tom.forward(random.randint(1, 10))
        tam.forward(random.randint(1, 10))
        tem.forward(random.randint(1, 10))
        #CHECK FOR THE ONE WHO TOCHED THE END OF THE SCREEN AND DECLARE THE WINNER
        if tim.xcor() > 380:
            print("Red turtle is the winner")
            return "red"
        elif tom.xcor() > 380:
            print("Blue turtle is the winner")
            return "blue"
        elif tam.xcor() > 380:
            print("Green turtle is the winner")
            return "green"
        elif tem.xcor() > 380:
            print("Yellow turtle is the winner")
            return "yellow"
        else:
            continue



def race ():
    bet = screen.textinput("Place your bet", "Which turtle will win the ")

    print(f"You placed a bet on {bet} turtle")
    winner = move()
    print(f"The winner is {winner}")  
    if bet == winner:
        print("You won the bet")
    else:
        print("You lost the bet")
 

    

    







race()

screen.exitonclick()