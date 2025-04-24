# Q: Check if a number is prime
num = int(input("Enter number to check prime"))
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print(f"{num} is a PRIME number")
