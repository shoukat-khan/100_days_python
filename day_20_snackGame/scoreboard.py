from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.highest_score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.goto(0, 270)

    self.update_scoreboard()
  
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} Highest_score: {self.highest_score}",  align="center", font=("Arial", 24, "normal"))
  
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()
  
  def game_over(self):

    if self.score > self.highest_score:
      self.highest_score = self.score
    self.score = 0
    self.update_scoreboard()

