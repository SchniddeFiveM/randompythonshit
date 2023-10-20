
class Car:
    def __init__(self):
        self.HorsePower = None
        self.Brand = None
        self.Model = None
        self.Color = None
        self.year = None
        self.x_position = 1
        self.y_position = 1

    def drive(self, x, y):
        self.x_position += x
        self.y_position += y

## Audi RS6 2017
car1 = Car()
car1.HorsePower = 250
car1.Brand = "Audi "
car1.Model = "RS6"
car1.Color = "black"
car1.year = "2017"

print(car1.Brand + car1.Model)
print(car1.HorsePower)
print(car1.Color)
print(car1.year)
print("")
print(car1.x_position)
print(car1.y_position)
car1.drive(1, 5)
print(car1.x_position)
print(car1.y_position)

print(" ")
## BMW I7 2023
car2 = Car()
car2.HorsePower = 450
car2.Brand = "BMW "
car2.Model = "I7"
car2.Color = "black"
car2.year = "2023"

print(car2.Brand + car2.Model)
print(car2.HorsePower)
print(car2.Color)
print(car2.year)