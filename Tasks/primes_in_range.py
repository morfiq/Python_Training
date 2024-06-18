range_num = int(input("Enter number up to which to find prime numbers"))
prime_list = []

for num in range(1, range_num + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_list.append(num)
print(prime_list)
