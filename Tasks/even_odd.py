# Q Check if a number is even/odd
num = int(input("Enter number to know even/odd"))
if num % 2 == 0:
    print("Number is Even Number")
else:
    print("Number is Odd Number")
'''
# Using lambda function   
odd_even = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(odd_even(num))
'''
