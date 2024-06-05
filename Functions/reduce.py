from functools import reduce
#
# # Use map to print the square of each numbers rounded
# # to three decimal places
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
#
# # Use filter to print only the names that are less than
# # or equal to seven letters
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
#
# # Use reduce to print the product of these numbers
# my_numbers = [4, 6, 9, 23, 5]
#
# # Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# filter_result = list(filter(lambda name: name, my_names, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    print(first, ":numbers:", second)
    return first + second

result = reduce(custom_sum, numbers)
print(result)

#
# import functools
# import operator
# import os
#
# files = os.listdir(os.path.expanduser("~"))
#
# functools.reduce(operator.add, map(os.path.getsize, files))

from functools import reduce
# from timeit import timeit
#
# # Using a user-defined function
# def add(a, b):
#     return a + b
#
# use_add = "functools.reduce(add, range(100))"
# print(timeit(use_add, "import functools", globals={"add": add}))


# Using a lambda expression
use_lambda = "functools.reduce(lambda x, y: x + y, range(100))"
print(timeit(use_lambda, "import functools"))


# Using operator.add()
use_operator_add = "functools.reduce(operator.add, range(100))"
print(timeit(use_operator_add, "import functools, operator"))


# Using sum()
print(timeit("sum(range(100))", globals={"sum": sum}))




