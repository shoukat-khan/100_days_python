colour =["white", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown","cyan"]
import turtle
import random
class Snack:
  def __init__(self):
    self.seg=[]
    self.create_snack()

  def create_snack(self):
    #remove the previous segments of the snake
    for _ in range(3):
      new_segment = turtle.Turtle("square")
      new_segment.shape("square")
      new_segment.color(random.choice(colour))
      new_segment.penup()
      new_segment.goto(x=0+(_*(-20)), y=0)
      self.seg.append(new_segment)

  def move_snack(self):
    for seg in range(len(self.seg)-1, 0, -1):
      new_x = self.seg[seg-1].xcor()
      new_y = self.seg[seg-1].ycor()
      self.seg[seg].goto(new_x, new_y)
    self.seg[0].forward(20)
    self.seg[0].shape("triangle")

  def up(self):
    if self.seg[0].heading() != 270:
      self.seg[0].setheading(90)

  def down(self):
    if self.seg[0].heading() != 90:
      self.seg[0].setheading(270)

  def left(self):
    if self.seg[0].heading() != 0:
      self.seg[0].setheading(180)
    
  def right(self):
    if self.seg[0].heading() != 180:
      self.seg[0].setheading(0)

  def add_snack(self):
    new_segment = turtle.Turtle("square")
    new_segment.shape("square")
    new_segment.color(random.choice(colour))
    new_segment.penup()
    new_segment.goto(self.seg[-1].xcor(), self.seg[-1].ycor())
    self.seg.append(new_segment)

#remove the last segment of the snake
#donot make the goto method to the last segment
#use append to add a new segment to the snake

  def reset_snack(self):
    for seg in self.seg:
      seg.reset()
    self.seg.clear()
    self.create_snack()


