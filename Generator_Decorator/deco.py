# decorator
import time
def mydecorator(function):
	def wrapper():
		print("********************")
		print("hello_world started")
		print("#####################")
		function()
		print("hello_world ended")
		print("#####################")
	return wrapper
# basic decorating
def hello_world():
	time.sleep(1)
	print("Hello Everyone!")




	

newfunc = mydecorator(hello_world)
newfunc()

# level2 decorating
@mydecorator
def hello_world():
	print("Hello Everyone!")

# code reuse
# modify existing