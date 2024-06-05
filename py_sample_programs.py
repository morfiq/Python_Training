# Area of circle
from math import pi
radius = float(input("Enter the radius of the circle"))
area =  pi * radius **2
print(f"Area of the circle is {area} ")
area_round = round(area, 4)
print(f"Area rounded to 4 decimals {area_round} ")


# Check if a number is prime
num = int(input("Enter number to check prime"))
for i in range(2, num):
	if num % i == 0:
		print("NOt prime")
		break
else:
	print(f"{num} is a PRIME number")


# Q Check if a number is even/odd
num = int(input("Enter number to know even/odd"))
if num % 2 == 0:
		print("Numbe is Even Number")
else:
	print("Numbe is ODD Number")
