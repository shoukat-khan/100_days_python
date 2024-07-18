def turn_left():
  None

def move():
  None

def at_goal():
  None

def front_is_clear():
  None

def right_is_clear():
  None


def move_right():
    turn_left()
    turn_left()
    turn_left()

    
    
while not at_goal():
    
   if right_is_clear() and not front_is_clear() :
    move_right()
    move()
   elif front_is_clear():
    move()
   else:
    turn_left()