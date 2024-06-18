# Palindrome of string
from timeit import timeit


def palindrome_v1(s):
    return s == s[::-1]


def palindrome_v2(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


def palindrome_v3(s):
    for c1, c2 in zip(s, reversed(s)):
        if c1 != c2:
            return False
    return True


S = input("Enter a string to check if it is palindrome")
# qwertytrewq
f1 = palindrome_v1(S)
if f1 == True:
    print("Given string is palindrome!")
else:
    print("Not a palindrome")

f2 = palindrome_v2(S)
if f2 == True:
    print("Given string is palindrome!")
else:
    print("Not a palindrome")

f3 = palindrome_v3(S)
if f3 == True:
    print("Given string is palindrome!")
else:
    print("Not a palindrome")
# each method had different performance check below for best method
for func in palindrome_v1, palindrome_v2, palindrome_v3:
    print('Time take by method:', func.__name__, timeit(lambda: func(S)))
