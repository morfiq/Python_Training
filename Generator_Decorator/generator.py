#Generators
import sys
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for element in x:
# 	print(element)
print(sys.getsizeof(x))

y = range(1,21)
# for i in y:
# 	print(i)
print(sys.getsizeof(y))

# print(sys.getsizeof(list(y)))
#
#
# y = map(lambda i: i**2, x)
# print(y)
# for i in y:
# 	print(i)
# import time
# def mygenerator(n):
# 	for x in range(n):
# 		yield x
# sqr_next = mygenerator(5)
# print(next(sqr_next))
# # sqr_next.
# print(type(sqr_next))
# print("do other job")
# # # time.sleep(3)
# print(next(sqr_next))
# print("do another job")
# print(next(sqr_next))
# # print(next(sqr_next))
# # print(next(sqr_next))
# print("new for loop")
# for i in sqr_next:
# 	print(i)
