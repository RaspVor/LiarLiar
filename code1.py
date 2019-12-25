#Functions

class Player:
  def __init__(self, name):
    self.name = name

  def myname(self):
    print("Hello my name is " + self.name)

p1=Player("Francois")
p1.myname()
