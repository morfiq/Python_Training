# def  say_hello():
#     # block belonging to the function
#     print('hello world')
# #     a=2
# #     b=3
# #     print('hello world')
# #     print(a+b)
# #     # End of function
# say_hello()
# CHECK_CONFIG = 22
# say_hello() # call the function
# say_hello() # call the function again
#
#
# Function Parameters
# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
# directly pass literal values

# x = 5
# y = 7
# # pass variables as arguments
# print_max(x, y)

# Local Variables
# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     # y = 3
#     # z = 4
#     print('Changed local x to', x)
#     # return x
# func(x)
# print("x:", x)
# print(a)
#
# print('x is still', x)
#
#
# #The global statement
# x = 50
# def func(y):
#     global x
#     print('x original value is', x)
#     x = 2
#     print('Changed global x to', x)
# func(x)
# print('Value of x is', x)
#
# Default Argument Values
# def say(message, times=1):
#     print(message * times)
# say('Hey')
# say('hexa', 3)
# say('hexa', 5)
# say()

# #Keyword Arguments
# def func(a, b=5, c=10, *seq, **kwapirs):
#     print('a is', a, 'and b is', b, 'and c is', c)
# func(3,7, 5)
# func(25, c=24)
# func(c=50, b=100)
# func(15, 14, c=12)
# myfunct(2,3,4,5,6)
# myfunct(2,3,4,5,6,...100)
# VarArgs parameters
# def myfunct(*args):
#     print(type(args))
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum/len(args))
#     # avg = sum/len(args)
#     # return sum/len(args)
# avg = myfunct(1,2,3,4,5,6,7,8, 20, 40)
# print(avg)



# def myfunctkw(**kwargs):
#     print(type(kwargs))
#     sum = 0
#     for i in kwargs:
#         sum += i
#     return sum/len(kwargs)
# avg = myfunctkw(John:61, james:73, bob:81))



# def total( **phonebook):
#     print(type(phonebook))
#     sum = 0
#     for k,v in phonebook.items():
#         sum += v
#     print("class avg:", sum/len(phonebook))
#iterate through all the items in tuple
# for single_item in numbers:
#     print('single_item', single_item)
# #iterate through all the items in dictionary
# for first_part, second_part in phonebook.items():
# print(first_part,second_part)
# total(Jack=71,John=65,Inge=83,Sam=93)
# #
# # #
# #
# The return statement

def maximum(x, y):
    if x > y:
        print("inside if")
        return x
    elif x == y:
        print("inside elif")
        return 'The numbers are equal'
    else:
        print("inside else")
        return y
    print("after all returns")
# #
max = maximum(33, 33)
print("max: ", max)
# max_val, pi, p2 = maximum(13, 1)
# print(max_val)
# print(pi)
# print(p2)

# def func(x, y):
#     print("value of X:", x)
#     print("value of y:", y)
#     x = 2
#     y = 3
#     z = 4
#     print("loacl vaue of X:", x)
#     print("loacl vaue of Y:", y)
#     return (x, y)
#
#
# a,b = func(4, 3)
# print("return value of func is ", a, b)
# print("return value of func is ", b)

# #
# DocStrings
# def print_max(x, y):
#     '''
#     input 2 ints'
#     output max value
#     Prints the maximum of two numbers.
#     The two values must be integers.
#     '''
#     # convert to integers, if possible
#     x = int(x)
#     y = int(y)
#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')
# print_max(3, 5)
# print(print_max.__doc__)
#
# def avg(*args):
#     """Returns the average of a list of numeric values."""
#     return sum(args) / len(args)

#
#
# def my_sum(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         print(x)
#         result += x
#     print("Total:", result)
#     return result
# my_sum(1, 2, 3)
# my_sum(1, 2, 3, 4, 5)
# my_sum()
#
#
# # # concatenate.py
# def concatenate(**kwargs):
#     result = ""
#     result1 = ""
#     print(type(kwargs))
#     print(kwargs)
#     # Iterating over the Python kwargs dictionary
#     for k,v in kwargs.items():
#         print(k," : ",v)
#     for arg in kwargs.values():
#         result += " "+arg
#     for arg in kwargs.keys():
#         result1 += arg
#     print(result1)
#     return result
# # #
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!", f="bbye", new="tutoarial"))

# *args
# **kwargs
#
# def total_fruits(**fruits):
#     total = 0
#     for amount in fruits.values():
#         total += amount
#     def testfunc():
#
#         return testval
#     return testfunc
# # #
# # outerfunct = total_fruits(val1,val2)
# # outerfunct()
# # #
# print(total_fruits(banana=5, mango=7, apple=8))
#
# Python function that returns multiple values
# def SwapTwoNumbers(a, b):
#     print("Before Swap: ", a, b)
#     a = a + b
#     b = a - b
#     a = a - b
#     sum = a+b
#     return a, b, sum
# a,b, sum = SwapTwoNumbers(17, 24)
# print("After Swap: ", a, b, sum)
#
# #passing list
# def my_function():
#
#   for x in food:
#     print(x)
#   print(food)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
# my_function(["pear"])
# print(fruits)
#
#
# Nested functions
# def function1(my_function):
#     my_function()
#     p = "Hello Pythonista"
#     def function2():
#         print(p)
#     function2()
# function1(my_function)