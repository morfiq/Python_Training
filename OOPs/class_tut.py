# class_tut.py

class Person:
  # Class body
  # defining constructor/ init method
  def __init__(self, personName, personAge):
    self.name = personName
    self.age = personAge
  def showName(self):
    print("This is a person with name:")
    print(self.name)


  def showAge(self):
    print(self.age)
#
person1 = Person("John", 28)
#
person1.showName()
person1.showAge()
person2 = Person("Jane", 28)
person2.showName()
person2.showAge()
Person.name()
#   # list of python class variables
#   # python class constructor
#   # python class method definitions
# cls = ClassName()
# print(cls)
# cls2 = ClassName()
# print(cls2)
# cls3 = ClassName()
# print(cls3)
# raise
# # # definition of the class starts here
# class Person:
#   # initializing the variables
#   name = "classPerson"
#   age = 22
#

#
#     # defining class methods
#
#   def showName(self):
#     print(self.name)
#
#   def showAge(self):
#     print(self.age)

    # end of the class definition

# print(dir(Person))
# # Create an object of the class
# person1 = Person("John", 23)
# print(dir(person1))
# # Create another object of the same class
# person2 = Person("Anne", 102)
# # call member methods of the objects
# print(Person.name)
# print(Person.age)
# Person.name = "NewPerson"
# person1.showAge()
# person1.showName()
# person2.showName()
# person2.showAge()
# print(Person.name)
# print(Person.age)
# # class definition
# class Job:
#   name = "Software Engineer"
#
#   # Define the method
#   def job_details(self):
#     print("place: New York")
#     print("Department: IT")
#     print("Salary: $100,000")
#
# # Create the Job object
# job1 = Job()
#
# # the class variable is Printed
# print("Name:",job1.name)
#
# # trigger the class method
# job1.job_details()
#
#
# #Constructor:
# # defining constructor
# # def __init__(self, personName, personAge):
# #   self.name = personName
# #   self.age = personAge
# #
# class Snake:
#
#     def __init__(self, name, wild= "yes"):
#       self.name = name
#       self.wild = wild
#
#     def change_name(self, new_name):
#       self.name = new_name
# # two variables are instantiated
# python = Snake("python")
# anaconda = Snake("anaconda")
# xyz = Snake("xyz", "No")
# xyz.change_name("abc")
# #
# # # print the names of the two variables
# print(python.name)
# print(python.wild)
# print(anaconda.name)
# print(anaconda.wild)
# print(xyz.name)
# print(xyz.wild)


# class Emp:
#   Company = 'Hexa'  # class variable shared by all instances
# print(Company) #Hexa

#   def __init__(self, name):
#     self.name = name  # instance variable unique to each instance
#
# e1 = Emp('Fido')
# e2 = Emp('Buddy')
# print(e1.Company)  # shared by all dogs
# # 'canine'
# print(e2.Company)  # shared by all dogs
# # 'canine'
# print(e1.name)  # unique to d
# # 'Fido'
# print(e2.name)  # unique to e
# 'Buddy'

#
class Polygon:
  # Initializing the number of sides
  def __init__(self, no_of_sides):
    self.n = no_of_sides
    self.sides = [0 for i in range(no_of_sides)]

  def inputSides(self):
    self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

  # method to display the length of each side of the polygon
  def dispSides(self):
    for i in range(self.n):
      print("Side", i + 1, "is", self.sides[i])


# class Triangle(Polygon):
#   # Initializing the number of sides of the triangle to 3 by
#   # calling the __init__ method of the Polygon class
#   def __init__(self):
#     Polygon.__init__(self, 3)
#
#   def findArea(self):
#     a, b, c = self.sides
#
#     # calculate the semi-perimeter
#     s = (a + b + c) / 2
#
#     # Using Heron's formula to calculate the area of the triangle
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print('The area of the triangle is %0.2f' % area)
#
# # Creating an instance of the Triangle class
# t = Triangle()
#
# # Prompting the user to enter the sides of the triangle
# t.inputSides()
#
# # Displaying the sides of the triangle
# t.dispSides()
#
# # Calculating and printing the area of the triangle
# t.findArea()
# print(comap)
# class Square(Polygon):
#   # Initializing the number of sides of the triangle to 3 by
#   # calling the __init__ method of the Polygon class
#   def __init__(self):
#     Polygon.__init__(self, 4)
#
#   def findArea(self):
#     a, b, c,d = self.sides
#
#     # calculate the semi-perimeter
#     s = a
#
#     # Using Heron's formula to calculate the area of the triangle
#     area = s*s
#     print('The area of the triangle is %0.2f' % area)
#
# # Creating an instance of the Triangle class
# t = Square()
# print(dir(t))
#
# # Prompting the user to enter the sides of the triangle
# t.inputSides()
#
# # Displaying the sides of the triangle
# t.dispSides()
#
# # Calculating and printing the area of the triangle
# t.findArea()
# class Animal:
#   def __init__(self, name):  # Constructor of the class
#     self.name = name
#
#   def talk(self):  # Abstract method, defined by convention only
#     raise NotImplementedError("Subclass must implement abstract method")

# class Cat(Animal):
#   def talk(self):
#     return 'Meow!'
# #
# cat = Cat("Kitty")
# print(cat.talk())
# class Dog(Animal):
#   def talk(self):
#     return 'Woof! Woof!'

# class Cow(Animal):
#
#
#     def talk(self):
#         return 'Moo! Moo!'
# cow1 = Cow("buddy")
# print(cow1.talk())
# #
# animals = [Cat('Missy'),
#            Cat('Mr. Mistoffelees'),
#            Dog('Lassie')]
#
# for animal in animals:
#   print(animal.name + ': ' + animal.talk())
# #
#
