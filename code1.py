#Initialization

class Player_Human:
  def __init__(self, name, cards, cave):
    self.name = name

  def myname(self):
    print("Hello my name is " + self.name + ".")


 
class Player_IA:
  def __init__(self, name, cards, cave):
    self.name = name

  def myname(self):
    print("Hello my name is " + self.name + ". I'm a robot.")

p1=Player_Human("Francois")
p1.myname()

p2=Player_IA("Neuromancer")
p2.myname()
