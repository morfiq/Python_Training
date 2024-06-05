# my_pets = ['alfred', 'tabitha', 'william', 'arla']
# uppered_pets = []
#
# for pet in my_pets:
#     pet_ = pet.upper()
#     uppered_pets.append(pet_)
# # #
# print("regular method:")
# print(uppered_pets)
# # Python 3
# # my_pets = ['alfred', 'tabitha', 'william', 'arla', 'ifhi']
# #
# print('with map==')
# print("map method:")
# uppered_pets = list(map(str.upper, my_pets))
# # #
# print(uppered_pets)


# import math
# numbers = [1, 2, 3, 4, 5, 6, 7]
# facto_list = list(map(math.factorial, numbers))
# #
# #
# print(facto_list)

def to_fahrenheit(c):
    return 9 / 5 * c + 32

# def to_celsius(f):
#     return (f - 32) * 5 / 9
celsius_temps = [37, 40, 42, 43]
# # Convert to Fahrenheit
print(list(map(to_fahrenheit, celsius_temps)))
# #
# #
# fahr_temps = [212, 104, 176]
# # Convert to Celsius
# list(map(to_celsius, fahr_temps))

# salary = [100, 110, 120, 130, 140]
#
# def sal_hike(sal):
#     return sal*1.1
# new_sal = list(map(sal_hike, salary))
# print(new_sal)


