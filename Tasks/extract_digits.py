# The // operator performs a floor division (also called integer division).
# The division is performed and then rounded to the next smallest whole number
# The end parameter on the print function adds a whitespace at
# the end of the printed value
num = int(input("Enter the number to extract digits in reverse order"))
while num > 0: #When num hits 0 stop the loop
    digit = num % 10 #digit=4 - last digit of 1234 = 4
    num = num // 10 #num=123 - 1234/10 = 123.4, drop 0.4 = 123
    print(digit)

