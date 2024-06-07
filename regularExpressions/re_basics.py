# raw string
import re

# print('printing\traw\nstring')
# print(r'printing\traw\nstring')

test_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

caseyfm.com

321-555-4321
123.555.1234
123*555*1234

Mr. Ferman
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
#re.compile allows us to separate pattern into a variable and reuse that variable to perform multiple searches


# pattern = re.compile(r'abc')
# pattern = re.compile(r'caseyfm.com')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')
# #
# # # word boundaries
# # pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(test_to_search)
# for match in matches:
#     print(match)
# print(test_to_search[1:4])
#
# sentence = 'Start of the sentence ... sentence end'
# # pattern = re.compile(r'^Start')
#
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)
#
pattern = re.compile(r'[a-zA-Z0-9]{0,20}@[a-z]{1,10}.com')
# matches = pattern.finditer(test_to_search)
# for match in matches:
#     print(match)
#
with open('Regular-Expressions\\data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)