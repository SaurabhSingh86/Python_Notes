# """ Calendar"""
#
# """ You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#
# Hello firstname lastname! You just delved into python.
#
# Function Description
#
# Complete the print_full_name function in the editor below.
#
# print_full_name has the following parameters:
#
# string first: the first name
# string last: the last name
# Prints
#
# string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
# Input Format
#
# The first line contains the first name, and the second line contains the last name.
#
# Constraints
#
# The length of the first and last names are each ≤ .
#
# Sample Input 0
#
# Ross
# Taylor
# Sample Output 0
#
# Hello Ross Taylor! You just delved into python.
# Explanation 0
#
# The input read by the program is stored as a string data type. A string is a collection of characters."""
#
# def print_full_name(first, last):
#     if len(first) <= 10 and len(last) <= 10:
#         print(f"Hello {first} {last}! You just delved into python.")
#         print("Hello {} {}! You just delved into python.".format(first, last))
#
# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)


input = ["(90, 180)", "(+90, +180)", " (90, -180)", "(90.0, 180.1)"]
# for i in l:
#     print(i)
#     l = list(i)
#     print(type(l))
#     print(l)
#     x, y = l
#     print(x)
#     print(y)

import re

def validate(data):
    # (latitude, longitude)
    pattern = r'\(' + r'[\+-]?(90(\.0+)?|[1-8]\d(\.[0-9]+)?|\d(\.[0-9]+)?), [\+-]?(180(\.0+)?|1[0-7]\d(\.[0-9]+)?|[1-9]\d(\.[0-9]+)?|\d(\.[0-9]+)?)' + r'\)'
    return re.search(pattern, data)

for i in range(int(input().strip())):
    if validate(input().strip()):
        print("Valid")
    else:
        print("Invalid")



import re

SIGN = '[\+-]?'
DECIMALS = '(\.[0-9]+)?'
ZEROS = '(\.0+)?'

LATITUDE =  f'{SIGN}(90{ZEROS}|[1-8]\d{DECIMALS}|\d{DECIMALS})'
LONGITUDE = f'{SIGN}(180{ZEROS}|1[0-7]\d{DECIMALS}|[1-9]\d{DECIMALS}|\d{DECIMALS})'

REGEX = f'\({LATITUDE}, {LONGITUDE}\)'
pattern = re.compile(REGEX)

def validate(value):
    return pattern.search(value)

for _ in range(int(input())):
    if validate(input()):
        print('Valid')
    else:
        print('Invalid')