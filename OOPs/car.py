# car.py
class Myclassname:
    def __init__(self):
        print("inside init")
    pass

mycls1 = Myclassname()
mycls2 = Myclassname()
# str = "eryu"
# str + "ertyui"
# str.



class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
    def tax(self, ex_price):
        return .14*ex_price
