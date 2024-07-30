#class
import turtle
import prettytable
# timmy = turtle.Turtle()
# screen = turtle.Screen()
# timmy.shape("turtle")    
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# screen.canvheight = 40
# timmy.color("red","blue")  # change color of turtle
# screen.exitonclick()


timmy =prettytable.PrettyTable()

# print("Hello, I am Timmy the turtle")
# timmy.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# timmy.add_row(["Adelaide", 1295, 1158259, 600.5])
# timmy.add_row(["Brisbane", 5905, 1857594, 1146.4])
# timmy.add_row(["Darwin", 112, 120900, 1714.7])
# timmy.add_column("City name", ["Adelaide", "Brisbane", "Darwin"]) # add column to table with name "City name"
# print(timmy)

class user:
  def __call__(self, id, name):
    self.id = id
    self.name = name
    print(f"User id: {self.id}, name: {self.name}")

    def __str__(self):
      return f"User id: {self.id}, name: {self.name}"
    
    def id_change(self, id):
      self.id = id
      print(f"User id: {self.id}, name: {self.name}")





User= user(77, "John")