import pdb

def func_print():
    print("dummy code")
    a = 2
    b ="wertyu"
    print("leaving func")
def calculate_factorial(n):
    print("at the top")

    pdb.set_trace()  # Set a breakpoint here
    factorial = 1
    func_print()
    for i in range(n):
      factorial *= i
    return factorial

def func2():
    number = int(input("Enter a number to calculate its factorial: "))

    factorial = calculate_factorial(number)
    print(f"The factorial of {number} is {factorial}")


func2()
calculate_factorial(3)