# The ‘pass’ statement in Python is a placeholder for future code.
# It does nothing when executed, but prevents errors in places
# # where empty code is not allowed
# def my_function():

#     # pass

# my_function()

# Output:
# No output, because the function does nothing.
# The ‘pass’ statement can be particularly useful when you’re sketching out the structure
# of your code and you’re not yet ready to implement certain parts. It allows you to create
# a syntactically correct Python script that runs without throwing errors,
# even though some parts of it are still under construction.
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)

# Output:
# 1
# 3
# 5
# 7
# 9
