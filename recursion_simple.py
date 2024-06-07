# def factorial(n):
#     return_value = 1
#     for i in range(2, n + 1):
#         return_value *= i
#     return return_value
# factorial(4)
#
# def factorial(n):
#     if n <= 1 :
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# factorial(4)




def count_leaf_items(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    count = 0
    linear_list = []
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
            linear_list.append(item)
    return count
names = ['Adam', ['Bob', ['Chet', 'Cat', ["qwerty"]], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(count_leaf_items(names))