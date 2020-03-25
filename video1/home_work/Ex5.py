import math

radius = float(input("Input radius of circle: "))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))