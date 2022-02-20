""" WAF to print 1 to 10 """


# def series(start, end):
#     for num in range(start, end + 1):
#         print(num, end=" ")
#
#
# series(1, 10)

""" WAF to print 10 to 1 """


# def series(start, end):
#     for num in range(start, end-1, -1):
#         print(num, end=" ")
#
#
# series(10, 1)


""" WAF to print -1 to -10 """


# def series(start, end):
#     for num in range(start, end-1, -1):
#         print(num, end=" ")
#
# series(-1, -10)


""" WAF to print -10 to -1 """


# def series(start, end):
#     for num in range(start, end+1):
#         print(num, end=" ")
#
#
# series(-10, -1)


""" WAF to print even numbers from 1 to 50 """


# def even_num(start, end):
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             print(num, end=" ")
#
#
# even_num(1, 50)




""" WAF to print odd numbers from 1 to 50 """


# def odd_num(start, end):
#     for num in range(start, end+1):
#         if num % 2 != 0:
#             print(num, end=" ")
#
#
# odd_num(1, 50)



""" ===> Traversing Through String <=== """

""" WAF to print all the character in a string """

# def char(string):
#     for char in string:
#         print(char, end=" ")
#
#
# char("pleasant")


""" ===> Traversing Through List <=== """


# def list_(*args):
#     for element in args:
#         print(element, end=" ")
#
#
# list_([1, 2, 3], [10, 20, 30, 40, 50])



""" ===> Traversing Through set <=== """



""" ===> Traversing Through dictionary <=== """

""" WAF to print index & the element in a string """
# string = "Million dollar smile"

# def func(sequence):

# s = "aesthetic"

# Method 1
# for item in range(len(s)):
#     print(s[item], "-->", item)

# Method 2  by using enumerate function         enumerate(s) => enumerate_object => either type casting or range
# => using type casting
# s = "aesthetic"
# a = enumerate(s)
# print(list(a))

# => using range
# for item in enumerate(s):
#     print(item, end=' ')

# for item in enumerate(s):
#     print(item[0], item[1])


# for index, item in enumerate(s):
#     print(index, "-->", item)


"""WAP to traverse through a string in reverse order"""
# string = "Million dollar smile"

# Method 1 => by using range

# for item in range(len(string)-1, -1, -1):
#     print(string[item], end=" ")

# MEthod 2 => by using slicing

# for item in string[::-1]:
#     print(item, end=" ")

# Method 3 => by using reversed function
# for item in reversed(string):
#     print(item, end=" ")


"""WAP to count number of characters present in the given string without using built-in-function"""
# s = "hello v"
# count = 0
# for _ in s:
#     count += 1
# print(count)

"""WAP to print even index character in a sting"""
s = "precious"
# for item in range(0, len(s), 2):
#     print(s[item])

# Method 2 by using slicing
# for item in s[::2]:
#     print(item, end=" ")

"""WAP to print odd index character in a sting"""

"""WAP to print the digit present inside the string"""
# string = "s1v2y3d7zi99n"

# for char in string:
#     if char.isdigit():
#         print(char, end=" ")

# for char in string:
#     if "0" <= char <= "9":
#         print(char, end=" ")


"""WAP to count number of digit present in the sting"""
