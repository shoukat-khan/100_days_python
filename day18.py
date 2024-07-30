from turtle import Turtle as t, Screen  #aliasing the class name

timmy= t() 
timmy.shape("turtle")
timmy.color("red")
# tim = t()
# tim.shape("turtle")
# tim.color("blue")

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# for i in range(360,361):
#   print(i)
#   for l in range(i):
#     timmy.forward(1)
#     timmy.right(360/i)
# make a random walk
import random
# direction = [0,90,180,270]
# timmy.pensize(10)
timmy.speed("fastest")
# for i in range(200):
#   timmy.color(random.random(),random.random(),random.random())
#   timmy.forward(30)
#   timmy.setheading(random.choice(direction))


for i in range (0,360):
  print(timmy.heading())
  timmy.setheading(i)
  timmy.circle(100)
  timmy.color(random.random(),random.random(),random.random())
  



screen= Screen()

screen.exitonclick()




