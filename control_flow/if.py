# Q Check if a number is even/odd
# num = int(input("Enter number to know even/odd"))
# if num % 2 == 0:
# 	print("Numbe is Even Number")
# elif <expression1>:
#     print("we are in elif1")
# elif <expression2>:
#     print("we are in elif2")
# elif <expression3>:
#     print("we are in elif3")
# else:
# 	print("Numbe is ODD Number")



number = 23

guess = int(input('Guess an integer : '))
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # if number > 10:
    #     print("double digit number")
    # New block ends here

elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
# you must have guessed > number to reach here
print('Done')
# This last statement