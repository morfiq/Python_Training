def fibonacci(n):
    # return a list of fibonacci numbers
    a,b = 0,1
    fib = [0,1]
    if not n:
        return []
    if n<=1:
        return [0]
    if n<=2:
        return fib
    for i in range(n-2):
        a, b = b, a+b
        fib.append(b)
    return fib

fibo_len = int(input("Enter the number of fibonacci series elements to print"))
print(fibonacci(fibo_len))
