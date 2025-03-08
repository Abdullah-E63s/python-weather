from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("You stop the carr")

class Motorcycle(Vehicle):
    def go(self):
        print ("u ride the motorcycle")

    def stop(self):
        print("you stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("you row the boat")

    def stop(self):
        print("you stop the boat")

car = Car()

car.go()
car.stop()

motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()

boat = Boat()
boat.go()
boat.stop()