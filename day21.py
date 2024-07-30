class animal:
  def __init__(self):
    self.no_of_eys = 2
    self.no_of_legs = 4

  def breath(self):
    print("Inhale, Exhale")


class dog(animal):   # Inheritance from animal class to dog class
  def __init__(self):
    super().__init__()    #must call the __init__ method of the parent class
    self.sound = "bark"

  def bark(self):
    print(self.sound)
    
  def breath(self):
    super().breath()  # call the breath method of the  
    print("Dog breathes through nose")


dog1 = dog()
dog1.bark()
dog1.breath()