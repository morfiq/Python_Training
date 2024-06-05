# any([0, 0.0, False, (), '0']), all([1, 0.0001, True, (False,)])
# (True, True)            #   ^^^-- truthy non-empty string
# any([0, 0.0, False, (), '']), all([1, 0.0001, True, (False,), {}])
# (False, False)
#
#
#
# List comprehensions
# new_list = [expression for member in iterable]
# squares = []
# for i in range(10):
#     squares.append(i * i)
# print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# mylist = ['a','b','c','d']
# squares = ["compre_"+i for i in mylist]
# print(squares)
#
#
# >>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
# >>> TAX_RATE = .08
# >>> def get_price_with_tax(txn):
# ...     return txn * (1 + TAX_RATE)
# >>> final_prices = [get_price_with_tax(i) for i in txns]
# >>> final_prices
#
#
# #Walrus operator
# >>> import random
# >>> def get_weather_data():
# ...     return random.randrange(90, 110)
# >>> hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
# >>> hot_temps
# [107, 102, 109, 104, 107, 109, 108, 101, 104]
#
# #Dictionary comprehensions
dict2 = {1:1,2:2,3:3}
dict1 = {i:i*i for i in range(6)}
print(dict1)

#
# def first_n(n):
#     '''Build and return a list'''
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     # print(nums)
#     return nums
# sum_of_first_n = sum(first_n(10000000))
# print(sum_of_first_n)

# Using the generator pattern (an iterable)
# class first_n(object):
#     def __init__(self, n):
#         self.n = n
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#
#     # Python 3 compatibility
#     def __next__(self):
#         return self.next()
#
#
#     def next(self):
#         if self.num < self.n:
#             cur, self.num = self.num, self.num+1
#             return cur
#         raise StopIteration()
#
#
# sum_of_first_n = sum(first_n(10000000))
# print(sum_of_first_n)

# yield
# next