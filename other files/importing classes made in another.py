from car import Car

car_1 = Car('chevy', 'Corvette', 2022, 'black')
car_2 = Car('Ford', 'Mustang', 2022, 'white')
car_3 = Car('lamborghini', 'Aventador', 2022, 'white')

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

print(car_3.make)
print(car_3.model)
print(car_3.year)
print(car_3.color)


car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()

car_3.drive()
car_3.stop()