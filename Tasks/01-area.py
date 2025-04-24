# Q: Are of circle
from math import pi
radius = float(input("Enter the radius of the circle"))
area =  pi * radius **2
print(f"Area of the circle is {area} ")
# printing values to a limit on decimals
area_round = round(area, 4)
print(f"Area rounded to 4 decimals {area_round} ")
