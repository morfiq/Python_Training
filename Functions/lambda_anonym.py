# x = 4

# def double(n):
#     return n*2
# print(double(10))
#
double = lambda x, y, z: x*2+y*2+z*3
print(double(5, 3,2))

# cube = lambda x: x**3
# print(cube(4))

# result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"
# print(result(5))

# char_count = sorted(char_count, key = lambda x: (x[1] * -1, x[0]))
# print(list(map(cube, fibonacci(n))))
#     t = Fraction(reduce(lambda x,y: x*y, fracs)) # complete this line with a reduce statement
#
# names = [ 'Border', 'Alan', 'Cook', 'Zlatan', 'Jonas', 'Tom', 'Augustine']
# names.sort()
# names.sort(key=lambda x: len(x))
# print(names)

# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# full_name('guido', 'van rossum')
# 'Full name: Guido Van Rossum'
#
# >>> (lambda x, y: x + y)(2, 3)
5