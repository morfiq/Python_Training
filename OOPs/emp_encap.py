class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self):
        # print("inside make sound")
        raise NotImplementedError  # Placeholder for subclasses to implement

    def display_info(self):
        return f"I am {self._name}, a {self._species}"

    def eat(self, food):
        return f"{self._name} is eating {food}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def make_sound(self):
        return "Meow!"

# cat = Cat("tom")
# print(cat.make_sound())
# dog = Dog("Puppy")
# print(dog.make_sound())

# class Catwild(Animal):
#     def __init__(self, name):
#         super().__init__(name, "cat")
#
#     # def make_sound(self):
#     #     return "Meow!"
#
# cat2 = Catwild("tom")
# print(cat2.make_sound())
class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "snake")

    def make_sound(self):
        return "Hiss!"
#
#
# # Encapsulation demonstration
# dog = Dog("Buddy")
# print(dog._name)  # Direct access, but not recommended
#
# # Inheritance demonstration
# cat = Cat("Whiskers")
# print(cat.display_info())
# print(cat.make_sound())
#
# # Polymorphism demonstration
animals = [Dog("Rex"), Cat("Fluffy"), Snake("Slippy")]
for animal in animals:
    print(animal.display_info())
    print(animal.make_sound())
    print(animal.eat("food"))
