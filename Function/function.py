# <<<<<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Function  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>>>>>>>

# A function is block of code which only runs when it is called
# Basically, we are using function for code redundancy or avoids repetition & makes the code.
# Types of function:-
    # 1. Built-in-function
    # 2. User-defined function

#1. Built-in-functions are functions that are predefined in the software to perform some specific task. e.g. print(), input(), id(), chr(), sum()
#2. User-defined-functions are functions that is defined by user in order to perform some specific task.


""" Returning Multiple values """


# def function(a, b):
#     return a
#
#
# print(function(10, 20))                 # (10, 20) output inside the tuple, for single value then 10


""" Question: WAF to add two numbers """
#
#
""" using both keyword & positional """
# def add_(a, /, *, b):
#     c = a + b
#     return c
# add_(5, b=7)
#
""" using positional only arguments """
# def add_(a, b, /):
#     c = a + b
#     return c
# add_(5, 7)
#
"""using keyword only arguments"""
# def add_(*, a, b):
#     c = a + b
#     return c
# add_(a=5, b=7)

"""WAF to return even number from 0 to 50 in a list """

# def even_(n):
#     res = []
#     for num in range(n+1):
#         if num % 2 == 0:
#             res.append(num)
#     return res
#
#
# n = int(input("Enter a number: "))
# print(even_(n))

# condition = if we pass 2 arguments:


# def even_(start, end):
#     l = []
#     for n in range(start, end):
#         if n % 2 == 0:
#             l.append(n)
#     return l
#
#
# print(even_(1, 50))


# Method 3: by using default parameter


# def even_(end, start=0):
#     l = []
#     for n in range(start, end+1):
#         if n % 2 == 0:
#             l.append(n)
#     return l
#
#
# print(even_(end=50))
# print(even_(start=21, end=60))


""" WAF to add three number but third value as a default parameters """


# def add_(a, b, c=0):
#     return a + b + c
#
#
# print(add_(10, 20))             # 30
# print(add_(10, 20, 30))         # 60


""" WAF that returns all the prime numbers in user defined range, if the user doesn't provide start index take it as 2 """

#
# def prime_num(end, start=2):
#     l = []
#     for num in range(start, end+1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 l.append(num)
#
#     return l
#
#
# print(prime_num(end=50))
# print(prime_num(start=21, end=60))

""" WAF to print fibonacci series in the user-defined range """


# def fibonacci(n):
#     a = 0
#     b = 1
#     i = 0
#     while i < n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#         i += 1
#
#
# fibonacci(10)                # 0 1 1 2 3 5 8 13 21 34


# Assignment 1
""" WAF that returns fibonacci series upto the number specified """


# def fibo(num):
#     a = 0
#     b = 1
#     while a <= num:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#
#
# fibo(15)                # 0 1 1 2 3 5 8 13


# Assignment 2
""" WAF that returns nth fibonacci number"""

# def fibo(nth_term):
#     a = 0
#     b = 1
#     i = 0
#     l = []
#     while i < nth_term:
#         l.append(a)
#         c = a + b
#         a = b
#         b = c
#         i += 1
#     print(l[-1])
#
# fibo(7)             # 8


""" WAF that checks if the given number is fibonacci or not """


"""" WAF that take integer & float data type as input or arguments & return it sum """


# def sum_(*args, total=0):
#     for i in args:
#         if isinstance(i, (int, float)):
#             total += i
#     return total
#
#
# print(sum_(7, 3, 4, 9))
# print(sum_(8, 6, 0.2, 2, 2.5, 8.2))


""" WAF that returns the number of positional arguments given to the function """
# Method 1: by using len() built-in-function


# def p_count(*args):
#     return len(args)
#
#
# print(p_count(73, 4.9, 6+4j, 4, 9, "VS", 'Python'))


# Method 2: without using built-in-function


# def p_count(*args, count=0):
#     for _ in args:
#         count += 1
#     return count
#
#
# print(p_count(73, 4.9, 6+4j, 4, 9, "VS", 'Python'))


""" WAF that takes variable number of positional arguments & returns all the integer value """


# def int_data(*args):
#     l = []
#     for i in args:
#         if isinstance(i, int):
#             l.append(i)
#     return l
#
#
# print(int_data('VS', 73, 8, 4+9j, 6.1))


""" WAF that takes multiple arguments & returns only the string in reversed order """


# def reverse_(*args):
#     l = []
#     for item in args:
#         if isinstance(item, str):
#             l.append(item[::-1])
#
#     return l
#
#
# print(reverse_('VS', "PYTHON", "Java", 2, 5.5, 4.1, 6+4j, True))


""" WAF that returns number of positional argument & number of keyword arguments """


# def count_(*args, **kwargs):
#     return len(args), len(kwargs)
#
#
# print(count_(1, 2, 3.5, a=5, b=10))


""" WAF that check if the given number of arguments is greater than 5 or not """


# def count_(*args):
#     if len(args) > 5:
#         return 'number of arguments > 5'
#
#     return 'number of argument < 5'
#
#
# print(count_(2, 2.5, 6+5j, "VS"))
# print(count_("VS", 86, 73, 4.9, 0.2, "Python"))


""" WAF to print message "Hai Everyone" if the user input is not present & if the user input is present print the user input """


# def display(msg="Hai Everyone"):
#     print(msg)
#
#
# display()
# display("Good Morning Guys")


""" WAF to check weather given number is Prime or not """

# def prime_(num):
#     if num > 1:
#         for i in range(2, num+1):
#             if num % i == 0:
#                 print(f'{num} is not Prime number')
#                 break
#         else:
#             print(f'{num} is Prime number')
#
#
# prime_(17)
# prime_(21)


# def prime_(num):
#     if num > 1:
#         for i in range(2, num+1):
#             if num % i == 0:
#                 return f'{num} is not Prime number'
#         return f'{num} is Prime number'
#
#
# print(prime_(7))
# print(prime_(12))


""" WAF to return last digit of a number """



""" WAF name tail that take a sequence as input & a number n & return last nth element from the sequence """


def tail(sequence, n):
    return sequence[-n:]


print(tail("Wonderland", 4))                                        # land
print(tail("AirIndia", 5))                                          # India
print(tail(["M.P.", "U.P.", "Delhi", "Goa"], 2))                    # ['Delhi', 'Goa']
print(tail(("Mango", "banana", "apple", "Grapes", "Papaya"), 2))    # ('Grapes', 'Papaya')

""" WAF named is perfect square that access a number & returns True, if it is a perfect square & returns False if it is not """
# Method 1: using import math
# from math import sqrt
#
#
# def is_perfect_square(num):
#     return num == sqrt(num) ** 2
#
#
# print(is_perfect_square(5))         # False
# print(is_perfect_square(36))        # True


# Method 2:


# def is_perfect_square(num):
#     sq = int(num ** 0.5)
#     if sq * sq == num:
#         return True
#     return False
#
#
# print(is_perfect_square(9))             # True
# print(is_perfect_square(10))            # False


# Method 3: using range


def is_perfect_square(num):
    for i in range(num):
        if i ** 2 == num:
            return True
        return False


print(is_perfect_square(9))


""" WAF to return a below output """
# func("TRACXN", 0)     # should print => RCN
# func("TRACXN", 1)     # should print => TAX


""" WAF that takes variable number of inputs & returns length of all the iterables """
# number = 12
#
#
# def prime_(num):    # 5
#     while num > 0:
#         for i in range(2, num): # 2, 5 --> i =5
#             if num % i == 0:
#                 break
#
#         else:
#             return num
#         num += 1
# a = [2, 4, 6, 9]
# print(prime_(a))


