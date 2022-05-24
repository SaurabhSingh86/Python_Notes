""" find the missing item in the list"""
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# ----------------------------------------------------------------------------------------------------------------------
""" """
# input = 25
# output = 425

# ----------------------------------------------------------------------------------------------------------------------
""" Swap two number without using third variable """


def swap(a, b):
    a, b = b, a
    print(f'value of a is {a}, value of b is {b}')

swap(5, 10)


# ----------------------------------------------------------------------------------------------------------------------
""" Swap two number with using third variable """
def swap(a, b):
    c = a
    a = b
    b = c
    print(f'value of a is {a}, value of b is {b}')

swap(10, 20)

# ---------------------------------------------------------------------------------------------------------------------
"""WAP to check the sum of any two elements that is present inside the list is 7 & print each element in the form of 
tuples """
# l = [1, 2, 3, 4, 5, 6]
# l2 = l
# a = 7

# for i in range(len(l)):
#     for j in range(len(l2)-1):
#         if l[i] + l2[j] == a:
#             print((l[i], l2[j]))

# for i in range(len(l)-1):
#     if l[i] + l[i+1] == a:
#         print((l[i], l[i+1]))
# # ---------------------------------------------------------------------------------------------------------------------
""" find the second highest value in the given dictionary"""
# d = {"a": 20, "b": 10, "c": 30, "d": 30}

# ---------------------------------------------------------------------------------------------------------------------
""" to check open bracer are close or not """
s1 = "([{([{}])})"
s2 = "([{([{})})"
open_b = 0
close_b = 0
for braces in s1:
    if braces in '({[':
        open_b += 1
    else:
        close_b += 1

if open_b == close_b:
    print(f'No of open braces are equal to close braces')
else:
    print(f'No of open braces is not equal to close braces')
# ---------------------------------------------------------------------------------------------------------------------
""" merge two dictionaries"""
# d1 = {"a":1, "b":2}
# d2 = {"c":3, "d":4}
# d3 = {}
# d3 ={**d1, **d2}
# print(d3)
# print({**d1, **d2})

# ---------------------------------------------------------------------------------------------------------------------
""" merge two tuples"""
# t1 = (1, "a", 2)
# t2 = ('b', True)
# print((t1 + t2))      # using concatenation

# t3 = ("c",)
#
# print((t2 + t3))

# ---------------------------------------------------------------------------------------------------------------------
""" merge two lists """
l1 = [1, 2, 3]
l2 = [4, 5]
l3 = *l1, *l2                   # (1, 2, 3, 4, 5)
l4 = [*l1, *l2]                 # [1, 2, 3, 4, 5]
l5 = l1 + l2                    # [1, 2, 3, 4, 5]
print(l3)
print(l4)
print(l5)



# ---------------------------------------------------------------------------------------------------------------------
# t1 = ("hello")               # print(type(t))          # <class 'str'>
# t2 = ("hello",)              # print(type(t))          # <class 'tuple'>
# ---------------------------------------------------------------------------------------------------------------------
""" using zip what will be the output """
# t1 = (1, 2, "c")
# t2 = ("d", 3)
# for i, j in zip(t1, t2):
#     print((i, j), end=" ")
# ---------------------------------------------------------------------------------------------------------------------
# s = "sonyindia"
# # output = "india", "ia"
#
# ss = "i"
# for index, char in enumerate(s):
#     if char == ss:
#         print(s[index:])

# ---------------------------------------------------------------------------------------------------------------------
"""take a string check that is palindrome or not"""
# input = input("enter your string:")

# 1 method
# res = ""
# for char in reversed(input):
#     res += char
# if input == res:
#     print("string is pallindrom:")
# else:
#     print("string is not pallindrome:")

# 2 method
# if input == input[::-1]:
#     print("string is pallindrom:")
# else:
#     print("string is not pallindrome:")

# ---------------------------------------------------------------------------------------------------------------------
""" WAP to count the no of substring that is present inside the given string """
# s = "ABCDCDC"
# substring = "CDC"
# # x = s.count(substring)
# # print(x)
# count = 0
# for num in range(len(s)):
#     if s[num:].startswith(substring):
#         count += 1
# print(count)

# ---------------------------------------------------------------------------------------------------------------------
""" find the duplicates elements from the collections """
s = "abcabccba"
# l = [1, 2, 3, 2, 1]
#
# for i in set(l):
#     if l.count(i) > 1:
#         print(i, end=" ")

# for i in set(s):
#     if s.count(i) > 1:
#         print(i, end=" ")

# ---------------------------------------------------------------------------------------------------------------------

# x = range(0, 11)
# print(x.stop)
# ---------------------------------------------------------------------------------------------------------------------
s1 = "hai"
s2 = "row"
s3 = "how"
for i, j, k in zip(s1, s2, s3):
    print(i,j,k)


l1 = [1, 2]
l2 = [3, 4, 5]
l3 = [6, 7, 8, 9]
for i, j, k in zip(l1, l2, l3):
    r = i, j, k
    print(i, j, k)
    print(type(r))
print()
# it means data loss in above e.g to avoid this we have to use zip longest
from  itertools import zip_longest

for i, j , k in zip_longest(l1, l2, l3, fillvalue="-"):
    print(i, j, k)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
