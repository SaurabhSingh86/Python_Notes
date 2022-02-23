"""
Que. Can we use multiple constructor inside a single class?
Ans: Yes we can, but if we have multiple constructor(__init__) in a class then it will consider the latest one.
    By default, constructor will return None
"""
# ------------------------------------------------------------------------------------------------------------------- #

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d


# p1 = Point(1, 2)                # TypeError: __init__() missing 2 required positional arguments: 'c' and 'd'
# p2 = Point(1, 2, 3)             # TypeError: __init__() missing 1 required positional argument: 'd'
# p3 = Point(1, 2, 3, 4)          # Accept

# ===>>> Constructor overloading is not possible in Python.
#        If we define multiple constructors then the last constructor will be considered.


"""
How to solve such kind of problem in Python?
==>> by using default value
"""

# class Point:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#
# p1 = Point()
# print(p1.__dict__)              # {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# p2 = Point(1)
# print(p2.__dict__)              # {'a': 1, 'b': 0, 'c': 0, 'd': 0}
# p3 = Point(7, 3)
# print(p3.__dict__)              # {'a': 7, 'b': 3, 'c': 0, 'd': 0}
# p4 = Point(8, 6, 2)
# print(p4.__dict__)              # {'a': 8, 'b': 6, 'c': 2, 'd': 0}
# p5 = Point(7, 3, 4, 1)
# print(p5.__dict__)              # {'a': 7, 'b': 3, 'c': 4, 'd': 1}


# ------------------------------------------------------------------------------------------------------------------

# ===>>> callable : is a built-in-function
#                   any method have __call__ attribute then it called callable.
#                   function is callable
#                   int, float, string are not callable
#                   boolean output it means True(if it is callable), False(if it is not callable)

# ------------------------------------------------------------------------------------------------------------------

# def add(a, b):
#     return a + b
#
#
# print(dir(add))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__'
#  , '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__']

# print(add(1, 2))        # 3
# i.e. callable

# class Greeting:
#     def __init__(self, name):
#         self.name = name
#
#
# g = Greeting("Rossum")
# print(dir(g))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'name']

# g()         # TypeError: 'Greeting' object is not callable
# there is no __call__ attributes inside this class so this class not callable

"""
How we can make Greeting class callable
"""


# class Greeting:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         return f'hello {self.name}'
#
#
# g = Greeting("Rossum")
# print(dir(g))
# ['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'name']

# there is __new__ now it becomes callable

# print(g)                # <__main__.Greeting object at 0x0000018D9CEB9948>
# print(g())              # hello Rossum


# class Greeting:
#     def __init__(self, name):
#         print(f'Hello {name}')

# Greeting("Guido")           # Hello Guido


# class Spam:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self):
#         print('Executing __call__', self.a)

# ?????????????????????? not getting
# class Squares:
#     def __call__(self, numbers):
#         squares = []              # using list comprehension also
#         for number in numbers:    # return [number ** 2 for number in numbers]
#             squares.append(number ** 2)
#         return squares
#
#
# s = Squares()
# print(s)


# class Squares:
#
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def __call__(self):
#         return [number ** 2 for number in self.numbers]
#
#
# s1 = Squares([5, 2, 3])
# print(s1())
#
# s2 = Squares((1, 2, 3, 10))
# print(s2())


# class Even:
#     def __call__