""" WAP to print 1 to 10 """

# for number in range(1, 11):
#     print(number)

""" WAP to print 10 to 1 """

# for number in range(10, 0, -1):
#     print(number)

""" WAP to print -1 to -10 """

# for num in range(-1, -11, -1):
#     print(num)

""" WAP to print -10 to -1 """

# for num in range(-10, 0):
#     print(num)

""" WAP to print even numbers from 1 to 50 """

# for num in range(1, 51):      # here we are not going to take range(0, 51) bcz interviewer tell starting from 1 to 50
#     if num % 2 == 0:
#         print(num)

""" WAP to print odd numbers from 1 to 50 """

# for num in range(1, 51, 2):                   # for num in range(1,51):
#     print(num)                                      # if num % 2 != 0:
                                                            # print(num)

""" ===> Traversing Through String <=== """

""" WAP to print all the character in a string """
string = "pleasant"

# Method 1
# for char in range(len(string)):
#     print(string[char])           # print(string[char], end=" ")

# Method 2
# for char in string:
#     print(char)                     # print(char, end=" ")

""" ===> Traversing Through List <=== """

list_ = [10, 20, 30, 40, 50]

# for item in list_:
#     print(item, end=" ")

# by using range

# for index in range(len(list_)):
#     print(list_[index], end=' ')

""" ===> Traversing Through set <=== """
# set_ = {"hai", "hello", "how", "are", "you"}
# for element in set_:
#     print(element, end=' ')

""" ===> Traversing Through dictionary <=== """
# d = {"one": 1, "two": 2, "three": 3 }
#
# for key in d:
#     # print(d[key])
#     print(key, d[key], sep="-->")

""" WAP to print index & the element in a string """
# string = "Million dollar smile"
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

# unpacking

# for index, item in enumerate(s):
#     print(index, "-->", item)


# unpacking an iterable
#=> Merge list
# l = [1, 2, 3]
# l1 = [5, 6, 7]
# print(*l, *l1)

# a, b, c = l
# print(a)
# print(b)
# print(c)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# max_ = l[-1]
# min_ = l[0]
# print(max_)
# print(min_)

# find max & min
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# min_, *rest, max_ = l

# print(max_)
# print(min_)
# print(rest)

# find first two largest number
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n1, n2, *n = l

# print(n1)
# print(n2)
# print(n)

# find last number
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# *n, last = l

# print(last)
# print(n)

# last two numbers
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# *n, n2, n1 = l

# print(n1)
# print(n2)
# print(n)


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

#Method 2 by using slicing
# for item in s[::2]:
#     print(item, end=" ")

"""WAP to print odd index character in a sting"""

"""WAP to print the digit present inside the string"""
# string = "1v2ydi99"

# for char in string:
#     if char.isdigit():
#         print(char, end=" ")

# for char in string:
#     if "0" <= char <= "9":
#         print(char, end=" ")


"""WAP to count number of digit present in the sting"""

