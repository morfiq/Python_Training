# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print asterisks for the current row
        for k in range(1, 2 * i):
            print("*", end="")
        print()


full_pyramid(5)


# printing pyramids with recursion
def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)


def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)


def pyramid_rec(n, current_row=1):
    if current_row > n:
        return
    spaces = n - current_row
    stars = 2 * current_row - 1
    # Print spaces
    print_space(spaces)
    # Print stars
    print_star(stars)
    # Move to the next line for the next row
    print()
    # Print the pyramid for the next row
    pyramid_rec(n, current_row + 1)


# Print the pyramid pattern
pyramid_rec(5)

# print alphabet pyramids
n = 5
alph = 65
for i in range(0, n):
    print(" " * (n - i), end=" ")
    for j in range(0, i + 1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()


# print number pyramids
def number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for j in range(2 * i - 1):
            print(j + 1, end="")
        # Move to the next line after each row
        print()


# Example usage
num_rows = 5
number_pyramid(num_rows)


# Print inverted full pyramid pattern
def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop for leading spaces in each row
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks in each row
        for k in range(2 * i - 1):
            print("*", end="")
        # Move to the next line after each row
        print("")


# Call the function to print the inverted full pyramid
inverted_full_pyramid(5)


# Print a half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")


half_pyramid(5)

# Half pyramid with recursion
def half_pyramid_rec(n):
    if n > 0:
        # Call the function recursively with a smaller value of n
        half_pyramid_rec(n - 1)

        # Print '*' characters for the current row
        print('*' * n)


# Call the function to print the half pyramid pattern
print_half_pyramid(5)
