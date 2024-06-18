# Q: print Fizz for multiple of 3, Buzz for multiple of 5,
# FizzBuzz for multiple of 3 and 5 else print number in a range

num = int(input("Enter the range of numbers"))
for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
