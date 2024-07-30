from turtle import Turtle, Screen 
import time
import random
from snack import Snack
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

f= Food()
score= Scoreboard()



S=Snack()

screen.listen()
screen.onkey(S.up, "Up")
screen.onkey(S.down ,"Down")
screen.onkey(S.left, "Left")
screen.onkey(S.right, "Right")


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  S.move_snack()
  if S.seg[0].distance(f) < 15:
    f.refresh()
    S.add_snack()
    score.increase_score()

  if S.seg[0].xcor() > 380 or S.seg[0].xcor() < -380 or S.seg[0].ycor() > 380 or S.seg[0].ycor() < -380:
    score.game_over()
    S.reset_snack()

    
  for seg in S.seg[1:]:  #SLICE THE LIST TO AVOID HEAD COLLIDING WITH ITSELF
    if S.seg[0].distance(seg) < 10:
      score.game_over()
      S.reset_snack()

 

    

# Create a screen


screen.title("Snake Game")
screen.exitonclick()