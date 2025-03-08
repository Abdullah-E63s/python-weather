class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f" {self.name} is eating")

    def sleep(self):
        print(f" {self.name} is sleeping")

class prey(Animal): #parent  classes
    def Flee (self):
        print(f" {self.name} is fleeing")

class predator(Animal): #parent classes
    def Hunt(self):
        print(f" {self.name} is hunting")

class Rabbit(prey): #children classes
    pass

class Hawk(predator): #children classes
    pass

class Fish(prey, predator): #children classes
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.eat()
hawk.Hunt()
rabbit.sleep()