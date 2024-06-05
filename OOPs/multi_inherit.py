class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        #Interface
        raise NotImplementedError


class FlyingMixin:
    def fly(self):
        return f"{self.name} is flying"


class SwimmingMixin:
    def swim(self):
        return f"{self.name} is swimming"


class Bird(Animal, FlyingMixin):
    def speak(self):
        return "Bird sound"


class Fish(Animal, SwimmingMixin):
    def speak(self):
        return "Fish sound"


class Duck(Bird, SwimmingMixin):
    def speak(self):
        return "Quack!"


class Eagle(Bird):
    def speak(self):
        return "Screech!"


class Shark(Fish):
    def speak(self):
        return "Silent (because sharks don't make sounds)"


if __name__ == "__main__":
    duck = Duck("Donald")
    print(duck.speak())   # Quack!
    print(duck.fly())     # Donald is flying
    print(duck.swim())    # Donald is swimming

    eagle = Eagle("Eddie")
    print(eagle.speak())  # Screech!
    print(eagle.fly())    # Eddie is flying

    shark = Shark("Sam")
    print(shark.speak())  # Silent (because sharks don't make sounds)
    print(shark.swim())   # Sam is swimming
