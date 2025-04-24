# Indentation and comments
# Python does not use curly braces {} to define code blocks.

# Instead, it uses indentation (spaces or tabs).

# The standard is 4 spaces per level.

# Incorrect Indentation Example
def greet(name):
if name:
    print("Hello,", name)
else:
    print("Hello, Stranger!")

# Error
# IndentationError: expected an indented block

# Correct Indentation Example
def greet(name):
    if name:
        print("Hello,", name)
    else:
        print("Hello, Stranger!")

greet("Alice")

# I'm a comment.
'''
multi
line 
comment
'''
"""
==================
multi
line 
comment
==================
"""
# include<stdio.h>
# void
#  main()
# {
# 								print("Hello world");
# 	'''
# 	input: integer
# 	output: nothing
# 	func: print a stroing
# 	'''
# 	'''
# 		input: integer
# 		output: nothing
# 		func: print a stroing
# 		'''
	
# 		'''
# 		input: integer
# 		output: nothing
# 		func: print a stroing
# 		'''

# 						}