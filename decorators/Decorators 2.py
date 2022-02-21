import time
from time import sleep

from collections import defaultdict

""" WADF convert the output into uppercase """

# def _upper(func):
#     def wrapper(*args, **kwargs):
#         upper_ = func(*args, **kwargs)
#         return upper_.upper()
#     return wrapper
#
# @_upper             # greet = _upper(greet)
# def greet(string):
#     print(string)
#
# greet("hello world")


""" Logging or info decorator """

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f'You called {func.__name__}')            # func.__name__  => get the name of the function
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log        # greet = log(greet)
# def greet():
#     return "Hello VS"
#
#
# # print(greet())
#
# @log
# def greeting(name):
#     return f'hello {name}'
#
#
# # print(greeting("Everyone"))
#
# @log
# def add(a, b):
#     return a + b
#
#
# # print(add(7, 3))


""" Reverse decorator  String => reverse it, not string => keep as it is """

# def reverse(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         return result
#     return wrapper
#
#
# @reverse
# def greet():
#     return "hello world"
#
#
# print(greet())
#
# @reverse
# def greeting(name):
#     return f"hey {name}"
#
#
# print(greeting("VS"))
#
#
# @reverse
# def add(a, b):
#     return a + b
#
#
# print(add(7, 3))


""" Positive decorator: return output in positive value """

# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, (int, float)):
#             return abs(res)
#         return res
#     return wrapper
#
#
# @positive
# def add_(a, b):
#     c = a + b
#     return c
#
#
# # print(add_(7, 3))                        # 10
#
# @positive
# def sub_(a, b, c):
#     return a - b - c
#
#
# # print(sub_(5, -3, 2))                    # 6
#
#
# @positive
# def mul_(a, b, c, d):
#     return a * b * c * d
#
#
# print(mul_(-2, -7, -1, 5))                  # 70
#
#
# @positive
# def greet():
#     return "hey Senorita!"
#
#
# print(greet())                              # hey Senorita!


""" Time decorator : find execution time """

# def time_(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'Execution time of function {func.__name__} is {end - start} seconds')
#         return res
#
#     return wrapper
#
#
# @time_
# def add(a, b):
#     sleep(2)
#     return a + b
#
#
# # print(add(8, 6))
#
#
# @time_
# def greet():
#     sleep(3)
#     return "hey beautiful people!"
#
#
# print(greet())
#
#
# @time_
# def greeting(name):
#     sleep(5)
#     return f'Hey {name} welcome to Python World!'
#
#
# print(greeting("Ss"))


""" Function count decorator """

# Method 1:
# _count = defaultdict(int)
#
#
# def func_count(func):
#     def wrapper(*args, **kwargs):
#         _count[func.__name__] += 1              # counting is extra functionality
#         print(_count)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @func_count
# def greeting(name):
#     return f'Hey {name} welcome to Python World!'
#
#
# @func_count
# def mul(a, b):
#     return a * b
#
#
# print(mul(7, 3))
# print(greeting("Ss"))
# print(mul(3, 7))
# print(greeting("VS"))
# print(mul(0, 1))
# print(greeting("GS"))


# Method 2:


# def _func_count(func):
#     func.count = 0
#
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         print(func(*args, **kwargs))
#         return f'Function {func.__name__} was invoked {func.count} times'
#
#     return wrapper
#
#
# @_func_count
# def greeting(name):
#     return f'Hey {name} welcome to Python World!'
#
#
# @_func_count
# def mul(a, b):
#     return a * b
#
#
# print(mul(7, 3))
# print(greeting("Ss"))
# print(mul(3, 7))
# print(greeting("VS"))


""" Max calls decorator """

# def max_calls(func):
#     func.count = 0                # *************** func.count = 0 not using func_count = 0
#
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         if func.count > 5:
#             raise ValueError (f'Maximum calls to function {func.__name__} exceeded')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @max_calls
# def greet():
#     return "Hey there! Happy birthday"
#
#
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())              # we get ValueError: Maximum calls to function greet exceeded


# @max_calls
# def greet(bank_name):
#     return f'Welcome to {bank_name} bank ATM'
#
#
# print(greet("SBI"))
# print(greet("UBI"))
# print(greet("Axis"))
# print(greet("HDFC"))
# print(greet("Yes"))
# print(greet("Kotak"))               # # we get ValueError: Maximum calls to function greet exceeded

""" repeat decorator: Execute the function n number of times"""


# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             func(*args, **kwargs)
#             sleep(2)
#     return wrapper
#
#
# @repeat
# def greet():
#     print("Hey there! Have a great day")
#
#
# greet()


# or we can also write that


# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             res = func(*args, **kwargs)
#             print(res)
#             sleep(2)
#
#     return wrapper
#
#
# @repeat
# def greet():
#     return "Hey there! Have a great day"
#
#
# greet()
#
#
# @repeat
# def add(a, b):
#     return a + b
#
#
# add(1, 3)


""" Cache Decorator: 
  Caches the argument & its result in a dict.
  if the function is called with the same argument, decorator will re-execute__________________
  it looks up for the result in dictionary & returns the result
  """


# def cache(func):
#     func_cache = {}             # attaching an empty dictionary
#
#     def wrapper(*args, **kwargs):
#         if args in func_cache:
#             print("Getting result from Cache")
#             return func_cache[args]
#         print('Executing func for the first time')
#         result = func(*args, **kwargs)
#         func_cache[args] = result
#         return result
#     return wrapper
#
#
# @cache
# def comp_sub(a, b):
#     sleep(10)
#     return a - b
#
#
# @cache
# def comp_mul(a, b, c):
#     sleep(8)
#     return a * b * c
#
#
# print(comp_sub(3, 15))          # Executing func for the first time => -12   it takes 10 seconds
# print(comp_sub(3, 15))          # Getting result from Cache         => -12   it gives immediately bcz save inside dict
# print(comp_mul(2, 3, -5))       # Executing func for the first time => -30   it takes 10 seconds
# print(comp_mul(2, 3, -5))       # Getting result from Cache         => -30   it gives immediately bcz save inside dict


""" Phone Decorator """

# numbers = [1234567890, 9876543210, 911234567890, 111234567890]
#
#
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:]
#         return str_number
#     else:
#         return str_number
#
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]                           # args = [(1234567890, 9876543210, 911234567890, 111234567890),]
#         processed_numbers = [add_prefix(number) for number in temp]
#         return func(processed_numbers)
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(phone_numbers):
#     for num in phone_numbers:
#         print(num)
#
#
# print_numbers(numbers)


""" validate """


def validate(*expected_types):
    def _validate(func):
        def wrapper(*args, **kwargs):
            for expected_type, actual_value in zip(expected_types, args):
                if not isinstance(actual_value, expected_type):
                    raise ValueError()
            return func(*args, **kwargs)
        return wrapper
    return _validate


@validate(float, float)
def sub(a, b):
    return a - b


@validate(int, float)
def mul(a, b):
    return a * b


@validate(str)
def greet(name):
    return f"Welcome {name} to Python World"


@validate(float, int)
def div(a, b):
    return f'Output of division { a / b}'


# print(sub(10.5, 20.5))
# print(sub(20, 20.5))

# print(mul(2.5, 2))
# print(mul(2, 5.5))

print(greet(5))
print(greet())





# def validate_types
# (expected_types, actual_values):
#     for expected_type, actual_value in zip(expected_types, actual_values):
#         if not isinstance(actual_value, expected_type):
#             raise TypeError()
#
#
# def validate(*expected_types):
#     def _validate(func):
#         def wrapper(*args, **kwargs):
#             validate_types(expected_types, args)
#             return func(*args, **kwargs)
#         return wrapper
#     return validate
#
#
# @validate(float, float)
# def sub(a, b):
#     return a - b
#
#
# @validate(int, float)
# def mul(a, b):
#     return a * b
#
#
# @validate(str)
# def greet():
#     return "Welcome to Python World"
#
#
# @