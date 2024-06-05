#Create a function
def greet(x,y):
    print('Hello World!')
    print('inside function')
#calling a function
greet(2,3)
print('Outside function')


def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')
#
f(6, 'bananas', 1.74)
# f(5, 'mangoes', 2.74)
f(qty=6,price=1.74, item='bananas' )
# # Too few arguments
# f(6, 'bananas')
# # Too many arguments
# f(6, 'bananas', 1.74, 'kumquats')
#
# #keyword arguments
# f(qty=6, item='bananas', price=1.74)
#
# f(qty=6, item='bananas', cost=1.74)
#
# f(item='bananas', price=1.74, qty=6)
#
# # Default Parameters
# def f(qty=6, item='bananas', price=1.74):
#     print(f'{qty} {item} cost ${price:.2f}')
# f(4, 'apples', 2.24)
#
# f(4, 'apples')
# f(4)
#
# f()
#
# f(item='kumquats', qty=9)
# f(price=2.29)