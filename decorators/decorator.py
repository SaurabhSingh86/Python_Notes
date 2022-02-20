# ~~~~~~~~~~~~~~~~~~~~~>>>> Decorators  <<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A Decorator takes in a function, add some functionality & returns it.
# This is also called metaprogramming because a part of the program tries to modify another part of the program -
# - at compile time.
# A single decorator can decorate any number of functions.

# Types:-
#     1. Built-in-decorators: @classmethod, @staticmethod
#     2. User-defined decorators: created by users

# First class Functions:

#   * first class functions are the one which is treated as any other object in Python like string, list, dicts etc
#   * you can pass a function to another function, you can return a function from another function, just like any
#     other functions.
#   * A Decorator is a function, which takes another function as an argument, add some extra functionality, & returns
#     another function without altering the source code of original function.


# General Structure of a Decorator:-
#   => function should be nested function
#   => outer function must accept one parameter
#   => the parameter in outer function should be called inside nested function
#   => outer function must return inner function's address


# def outer(func):
#     def inner(*args, **kwargs):
#         func (*args, **kwargs)
#     return inner


""" WADF """

# def spam(func):
#     def wrapper(*args, **kwargs):
#         print("inside spam")
#         func(*args, **kwargs)
#     return wrapper
#
#
# @spam       # add = spam(add)
# def add(a, b):
#     print(f'sum of two numbers are: {a + b}')
#
#
# add(1, 2)


# ====>> Note
# Whenever a function is decorated using @ decorated function interpreter interpret it as main function = decorator of-
# -main function, when the interpreter execute @ decorator function to major changes will happen
#   1=> Outer functions parameters (func) takes the address of main function
#   2=> The main function will take the address of wrapper function
# The process of calling a function with different name is called "Monkey Patching".


""" WADF to count the total number arguments """

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Total no of arguments are: ", len(args) + len(kwargs))
#         func(*args, **kwargs)
#     return wrapper
#
# @outer              # add = outer(add)
# def add(a, b, c):
#     print(f'sum of numbers are: {a + b + c}')
#
#
# add(7, 3, 4)


""" WADF to input some delay before executing any function """

# import time
#
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)                   # here I'm taking 2 seconds delay
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @delay
# def display():
#     return "in display"
#
#
# print(display())


""" WAD which takes a string & reverse it """

# def reverse_(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)                 # or return func((*args, **kwargs)[::-1]
#         return res[::-1]
#     return wrapper
#
# @reverse_           # spam = reverse_(spam)
# def spam(string):
#     return string
#
#
# print(spam("VS Code"))


""" WAD which takes a list of string & reverse it """

sequence = ["hai", 73, "hello", 86, "Python", 99]

"""WADF to execute a function for 3 times """

# def repeat_(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#     return wrapper
#
#
# @repeat_            # add = repeat(add)
# def add(a, b):
#     print(a+b)
#
#
# add(7, 3)


""" WADF which execute the function for n times """

# def p_outer(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return outer
#
#
# @p_outer(3)
# def add(a, b):
#     print(f'Sum of both no. are: {a + b}')
#
#
# add(49, 61)
#
#
# @p_outer(2)
# def sub(a, b):
#     print(f'Subtraction of both no. are: {a - b}')
#
#
# sub(4, 9)


""" WADF which inputs a delay of n seconds """

# import time
#
#
# def p_outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#
#         return wrapper
#
#     return delay
#
#
# @p_outer(3)
# def mult(a, b):
#     print(f'Product of both number: {a * b}')
#
#
# @p_outer(2)
# def div(a, b):
#     print(f'Output of division: {a / b}')
#
#
# mult(7, 3)
# div(20, 2)


""" WADF that calculates time of execution of a function """
# import time
#
# def p_outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             func(*args, **kwargs)
#             end = time.time()
#             print(f'Time of execution is: {end - start}')
#         return wrapper
#     return delay
#
#
#
# @p_outer(2)
# def sub(a, b):
#     print(f'Output of a-b is {a - b}')
#
#
# sub(10, 20)


# ~~~~~~~~~~ Assignment  ====>>>

""" 1. WADF to count the no of arguments passed to a function """
# Method: 1


# def spam(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return f' Total no of arguments {len(args) + len(kwargs)}'
#         #return f'Total no of positional arguments {len(args)} & keyword arguments {len(kwargs)}'
#     return wrapper
#
# @spam
# def c_arg(a, b, c, d):
#     return a, b, c, d
#
#
# print(c_arg(1, 2, 3, d=5))


# Method 2:


# def spam(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         p_count = 0
#         k_count = 0
#         for _ in args:
#             p_count += 1
#         for _ in kwargs:
#             k_count += 1
#
#         return p_count, k_count
#     return wrapper
#
# @spam
# def c_arg(a, b, c, d):
#     return a, b, c, d
# #
# print(c_arg(1, 2, 3, d=5))


# Method 3:

# def count_(func):
#     def wrapper(*args, **kwargs):
#         print(f"Total no of arguments is : {len(args) + len(kwargs)}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @count_
# def add(a, b, c):
#     return f'sum of numbers are: {a + b + c}'
#
#
# print(add(1, b=2, c=3))


""" WADF to print "hello world" message if the user has not given input """

# def p_outer(s='hello world'):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(s)
#             return func(*args, **kwargs)
#         return wrapper
#     return outer
#
#
# @p_outer('Python')
# def display(msg="Python world"):
#     return msg
#
#
# @p_outer()
# def display1(msg="Python world"):
#     return msg
#
#
# display()                   # Python
# print(display())            # Python,  # Python world
#
#
# display1()                  # hello world
# print(display())            # Python,   # Python world



""" returns only positive values after subtraction"""

# # Method 1:
# def positive_result(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
#
# @positive_result
# def sub(a, b):
#     return a - b
#
#
# print(sub(73, 86))
#
#
# # Method 2:
#
# def positive_result(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, (int, complex)):
#             return abs(res)
#         return res
#     return wrapper
#
#
# @positive_result
# def sub(a, b):
#     return a - b
#
#
# @positive_result
# def mul(a, b, c, d):
#     return a * b * c * d
#
#
# @positive_result
# def greet():
#     return "Hello Everyone"
#
#
# @positive_result
# def greeting(name):
#     return f'Hey {name}!! \n Welcome to Python world.'
#
#
# print(sub(73, 86))                  # 13
# print(mul(-1, -2, -3, d=4))         # 24
# print(greet())                      # Hello Everyone
# print(greeting("Senorita"))         # Hey Senorita!!  #  Welcome to Python world.


""" WADP to return the length of the given iterable """

# def count_(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return f'Total no of length of the given iterable: {len(args) + len(kwargs)}'
#     return wrapper
#
#
# def spam(iterable):
#     return iterable
#
#
# print(spam([1, 2, 3, 4, 5, 6]))


# def spam(func):
#     def wrapper(a, b, c):
#         return func(a, b, c)      # to avoid this we use variable no of arguments i.e. *args & **kwargs
#     return wrapper
#
#
# @spam
# def func(a, b, c):
#     return a+b+c
#
#
# print(func(1, 3, 5))
