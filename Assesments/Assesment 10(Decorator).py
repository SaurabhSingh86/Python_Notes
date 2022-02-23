""" 1. WADF to decorate the add function. output = 1 added with 2 is 3"""


# def decorate_add(func):
#     def wrapper(*args, **kwargs):
#         a, b = args
#         return f'{a} added with {b} is {func(*args, **kwargs)}'
#     return wrapper
#
#
# @decorate_add
# def add(x, y):
#     return x + y
#
#
# print(add(1, 2))


""" 
2. Create a decorator function to decorate the div function to throw an error when 0 is used as divisor 
output 2 divided by 1 is 2
       2 divided by 0 is not possible 0 can not be a divisor
"""


# def div_decorate(func):
#     def wrapper(*args, **kwargs):
#         a, b = args
#         if b == 0:
#             return f'{b} can not be a divisor'
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @div_decorate
# def div_(x, y):
#     return x / y
#
#
# print(div_(2, 1))
# print(div_(2, 0))


""" 3. Create a decorator function then do these:-
a) decorate a normal function
b) decorate a decorate function
c) use decorator function and decorated decorator function to decorate a normal function
"""


# def add_greet(func):
#     def wrapper(*args, **kwargs):
#         print("Hello Everyone!!")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def decorate_python_intro(func):
#     def wrapper(*args, **kwargs):
#         print("Welcome to Python World")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @add_greet
# @decorate_python_intro
# def python_intro():
#     return "Python is very simple language."
#
#
# print(python_intro())
