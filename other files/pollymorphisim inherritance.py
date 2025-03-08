from abc import ABC, abstractmethod 

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
        

class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(shape):
    def __init__(self, base , height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2
    
class pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings



shapes = [Circle(4), Square(5), Triangle(6, 7), pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm²")