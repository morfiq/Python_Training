# class_basics.py

# import math
# #
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return round(math.pi * self.radius ** 2, 2)
#     def perimeter(self):
#         return 2*math.pi*self.radius
#
# # from circle import Circle
# #
# circle_1 = Circle(42)
# # print(circle_1)
# circle_2 = Circle(7)
# # print(circle_2)
# print(circle_1.radius)
# print(circle_1.calculate_area())
# print(circle_1.perimeter())
# print(Circle.radius)
# #
# circle_1
#
# circle_2
# Accessing Attributes and Methods
# obj.attribute_name
#
# obj.method_name()
#
# # Creating Objects From a Class in Python
# from class_basics import Circle
#
# circle_1 = Circle(42)
# circle_2 = Circle(7)
#
# circle_1
#
# circle_2
#
# # Class Attributes
class ObjectCounter:
    num_instances = 0
    def __init__(self, name):
        self.name = name
        ObjectCounter.num_instances += 1

p1 = ObjectCounter("John")
# ObjectCounter()
p2 = ObjectCounter("Jane")
p3 = ObjectCounter("James")

print(p2)
print(p3)
print(ObjectCounter.num_instances)
print(p2.num_instances)
print(p1.name)
print(p2.name)
print(p3.name)
# #
# #
counter = ObjectCounter("qwerty")
print(counter.num_instances)
ObjectCounter.num_instances = 5
print(counter.num_instances)
print(p1.num_instances)
print(p2.num_instances)
print(p3.num_instances)
p4 = ObjectCounter("Johnny")
print(p4.num_instances)
# #
#
# # instance Attributes
from car import Car
#
toyota_camry = Car("Toyota", "Camry", 2022, "Red")
print(toyota_camry.make)

print(toyota_camry.model)

print(toyota_camry.color)

print(toyota_camry.speed)
toyota_camry.speed = 150
print(toyota_camry.speed)
