import math
pi = 3.14
class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * pi * self.radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def grow(self):
        self.radius += 1

    def get_radius(self):
        return self.radius

print("Welcome to Circle Tester.")
radius = input("Enter a radius. ")
circle = Circle(radius)
print(f"Diameter:", circle.calculate_diameter())
print(f"Circumference:", circle.calculate_circumference())
print(f"Area:", circle.calculate_area())
while True:
    response = input("Would you like to grow your circle? y/n ")
    if response == "y":
        print("Standby while your circle grows...")
        (circle.grow())
        print(f"Diameter:", circle.calculate_diameter())
        print(f"Circumference:", circle.calculate_circumference())
        print(f"Area:", circle.calculate_area())
    if response == "n":
        print("Goodbye!")
        break