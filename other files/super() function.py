class Shape:
    def __init__(self, color, is_filled):
        self.color= color
        self.is_filled = is_filled
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'unfilled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        super().describe()
        print(f"it is a Circle with an area of {3.14 * self.radius * self.radius} cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
        super().describe()
        print(f"it is a Square with an area of {self.width * self.width} cm^2")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled )
        self.width = width
        self.height = height
        super().describe()
        print(f"it is a Triangle with an area of {(self.width * self.height)/2} cm^2")
        

circle = Circle("red", True, 5)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

square = Square("Blue", False, 6)

print(square.color)
print(square.is_filled)
print(f"{square.width} cm")

triangle = Triangle("Yellow" , True , 7 , 8)


print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")

circle.describe()
square.describe()
triangle.describe()

