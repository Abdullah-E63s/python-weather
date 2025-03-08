class Animal:
 def __init__(self, name):
    self.name = name
    self.isalive  = True
    
 def eat(self):
    print(f"{self.name} is eating.")

 def sleep(self):
    print(f"{self.name} is sleeping.")

class Dog(Animal):
 def speak():
    print("woof")
      

class Cat(Animal):
 def speak():
    print("Meow")

class Mouse(Animal):
 def speak():
    print("Squeak")

dog = Dog("scooby")
cat = Cat("Garfield")
mouse = Mouse("mickey")

print(dog.name)
print(dog.isalive)
print(dog.eat)
print(dog.sleep)

Dog.speak()
Cat.speak()
Mouse.speak()


