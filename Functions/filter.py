# # Python 3
# dromes = ["demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk"]
# #
# palindromes = list(filter(lambda word: word == word[::-1], dromes))
# #
# print(palindromes)
# word = "qwerty"
# print(word[::-1])
# testlam = lambda a,b: a+b
# print(testlam(2,4))

# import math
#
# math.sqrt(-16)
# import math
# #
# def is_positive(num):
#     return num >= 0
# #
# #
# def sanitized_sqrt(numbers):
#     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
#     return list(cleaned_iter)
# #
# #
# sanitized_sqrt([25, 9, 81, -16, 0])


# salary = [80, 90, 85, 110, 120, 130, 140]
#
# def grade100(sal):
#     return sal < 100
# new_sal = list(filter(grade100, salary))
# print(new_sal)