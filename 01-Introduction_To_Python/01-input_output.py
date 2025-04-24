#INPUT
# input() is used to get user input as a string

name = input("Enter your name: ")
age = input("Enter your age: ")

#OUTPUT
# print() is used to display output
print("Hello " + name + ", you are " + age + " years old.")

# input() always returns a string, typecast if needed
age = int(input("Enter your age: "))

# Ask user for two numbers and print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum is: {sum}")



