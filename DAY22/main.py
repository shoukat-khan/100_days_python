from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen= Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800,700)
paddle = Paddle((380,0))
paddle2 = Paddle((-390,0))
bal= Ball()
score= Scoreboard()
screen.listen()
screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")


game_is_on = True
while game_is_on:
  time.sleep(0.1)
  bal.move()
  if bal.ycor() > 325 or bal.ycor() < -325:
    bal.bounce_y()
  if bal.distance(paddle) < 50 and 370 >bal.xcor() > 350 or bal.distance(paddle2) < 50 and  -370 <bal.xcor() < -350:
    print(bal.xcor()) 
    bal.bounce_x()
  if bal.xcor() > 400:
    score.l_point()
    bal.reset_position()
  if bal.xcor() < -400:
    bal.reset_position()
    score.r_point()

screen.exitonclick()