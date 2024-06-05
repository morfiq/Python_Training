
#Generators
# for i in range(10):
#     print(i)
# def mygenerator(n):
# 	for x in range(n):
# 		print("x is:" +str(x))
# 		yield x ** 2
# sqr_next = mygenerator(10)
# print(next(sqr_next))
# print("do other tasks")
# print(next(sqr_next))
# print("do some other tasks")
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))

# sqr_next = mygenerator(3)
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
# print(next(sqr_next))
#
# def infinite_sequence():
# 	result = 1
# 	while True:
# 		yield result
# 		result *= 2
# values =  infinite_sequence()
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# def func1():
# 	print("base function")
#
# def func2(func_name):
# 	print("inside func2")
# 	func1()
# 	print("after func_name call")
# func2(func1)


# def wish():
# 	print("good morning")
# 	print("hello there")
#
# wish()
# ************
# good morning
# hello there
# ************


# def wish():
# 	print("good morning")
# 	print("hello there")
#decorator

# def mydecorator(function):
# 	def wrapper():
# 		print("++++++++++++++++++++")
# 		print("++++++++++++++++++++")
# 		function()
# 		print("********************")
# 		print("********************")
# 	return wrapper
#
# # basic decorating
# @mydecorator
# def hello_world():
# 	print("Hello Everyone!")
# 	print("Hope you are doing well!")
# 	print("Keep it up!!")
# #
# hello_world()
# print("====calling decoratore======")
# newfunc = mydecorator(hello_world)
# newfunc()

# level2 decorating
# @mydecorator
# def hello_world():
# 	print("Hello Everyone!")

# hello_world()
#decorator practical example 1
# def logger(function):
# 	def wrapper(*args, **kwargs):
# 		value = function(*args, **kwargs)
# 		with open('logfile.txt', 'a+') as f:
# 			fname = function.__name__
# 			print(f"{fname} returns value {value}")
# 			f.write(f"{fname} returns value {value}")
# 		return value
# 	return wrapper
#
# @logger
# def add(a,b):
# 	return a+b
# print(add(3,99))

# # #decorator practical example 2
import time
def timed(function):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		print("timestamp before:", start_time)
		value = function(*args, **kwargs)
		print("timestamp after:", time.time())
		time_taken = time.time() - start_time
		fname = function.__name__
		print(f"{fname} took  {time_taken} to execute!")
		return value
	return wrapper

@timed
def myfunc(x):
	result = 1
	for i in range(1,x):
		result *= i
	return result
print(myfunc(9999))

