class StudentFighter(object):
   def __init__(self, strength, health, name):
       self.strength = strength
       self. name = name
       self.health = health
kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")
print(kalu.name, kalu.strength, kalu.health)
print(david.name, david.strength, david.health)

class StudentFighter(object):
    def __init__(self, strength, health,name):
        self.strength = strength
        self.name = name
        self.health = health
    def attack(self, opponent):
        opponent.health -= self.strength
        message = "{} has {} health points remaining".format(opponent.name, opponent.health)
        print(message)
kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")
kalu.attack(david)

class StudentFighter(object):
    def __init__(self, strength, health, name):
        self.strenght = strength
        self.name = name
        self.health = health
    def attack(self, opponent):
        multiplier = randint(1, 4)
        damage = multiplier * self.strength
        git remote add origin https://github.com/sally2002313/studentFighter.git  
    
