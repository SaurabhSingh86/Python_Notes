# ~~~~~~~~~~~~~~~~~~~~~~~~   Operators     ~~~~~~~~~~~~~~~~~
# Operators are set of symbols that have a specific meaning associated with in it, we can't modify the meaning we can
# only utilize as per out requirement in the programs.

# There are 7 types of operators-
#     1. Arithmetic operator
#     2. Relational operator
#     3. Logical operator
#     4. Bitwise operator
#     5. Assignment operator
#     6. Positional operator
#     7. Membership operator

## 1. Arithmetic operator =>    +, -, *, **, /, //, %
"""
>>> # addition
>>> 2 + 3
5

>>> 1.4 + 9.6
11.0

>>> 2 + 6j + 7 + 4j
(9+10j)

>>> True + False
1

>>> "hai" + "hello"
'haihello'

>>> [1, 2, 3] + ["a", "b"]
[1, 2, 3, 'a', 'b']

>>> "hai" + [1, 2, 3]
TypeError: can only concatenate str (not "list") to str

>>> [1, 2, 3] + 7
TypeError: can only concatenate list (not "int") to list

>>> [1, 2, 3] + [7]
[1, 2, 3, 7]

>>> (1, 2, 3) + ("hai",)
(1, 2, 3, 'hai')

>>> {1, 2, 3} + {4, 5, 6}
TypeError: unsupported operand type(s) for +: 'set' and 'set'

>>> dict(a=1, b=2) + dict(c=3, d=4)
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


>>> # subtraction
>>> 1 - 3
-2

>>> 3.2 - 2
1.2000000000000002

>>> 1 + 2j -(2+3j)
(-1-1j)

>>> True - True
0

>>> "hai" - "hello"
TypeError: unsupported operand type(s) for -: 'str' and 'str'

>>> [1, 2, 3] - [1, 4, 5]
TypeError: unsupported operand type(s) for -: 'list' and 'list'

>>> {1, 2, 3, 4} - {3, 4}
{1, 2}

>>> dict(a=1, b=2) - dict(c=3, d=4)
TypeError: unsupported operand type(s) for -: 'dict' and 'dict'

>>> # multiplication
>>> 2 * 5
10

>>> 1.2 * 5.7
6.84

>>> 2 + 3j *(1 + 6j)
(-16+3j)

>>> 2 + 3j * 2
(2+6j)

>>> True * 2
2

>>> "hi" * 3
'hihihi'

>>> "hai" * 1.2
TypeError: can't multiply sequence by non-int of type 'float'

>>> [1, 2, 3] * 2
[1, 2, 3, 1, 2, 3]

>>> (1, 2, 3) * 2
(1, 2, 3, 1, 2, 3)

>>> {1, 2, 3} * 2               ???????????????????????????????????
TypeError: unsupported operand type(s) for *: 'set' and 'int'

>>> {"a" : 1, "b": 2} * 2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'


>>> # division
>>> 2 / 4
0.5

>>> 1.2 / 5
0.24

>>> 2 + 3j / 2 + 5j
(2+6.5j)

>>> 6 / False
ZeroDivisionError: division by zero

>>> 6 / True
6.0

>>> "hai" / 2
TypeError: unsupported operand type(s) for /: 'str' and 'int'

>>> # floor division
>>> 2 / 3
0.6666666666666666

>>> 2 // 3
0

>>> -5 / 3
-1.6666666666666667

>>> -5 // 3
-2

>>> # modulus
>>> 2 % 3
2

>>> 10 % 6
4

>>> # exponent
>>> 3 ** 3
27

>>> 7 ** 2
49

>>> 7 ** 1.2
10.330412131161864

>>> a = -2
>>> abs(a)
2

>>> divmod(2, 3)
(0, 2)

>>> round(1.234)
1

>>> round(1.234, 2)
1.23

>>> round(1.2345, 3)
1.234

>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']



# Relational Operator : ==, !=, >, <, >=, <=

>>> # relational
>>> 2 < 3
True

>>> 1.4 > 8.2
False

>>> True > False
True

>>> "hai" > "hello"
False

>>> "hel" > "hello"
False

>>> [1, 2, 3] < [2, 3, 4]
True

>>> [2, 3, 5] < [2, 3, 4]
False

>>> [1, 2, 3] > [ "a", "b", "c"]
TypeError: '>' not supported between instances of 'int' and 'str'

>>> {1, 2, 3} > {3, 4, 5}
False

>>> {1, 2, 3} > {0, 4, 5}
False

>>> {1, 2, 3} == {1, 2, 3}
True

>>> {1, 2, 3} < {1, 2, 4}
False

>>> {"a": 1, "b": 2} > {"a" : 4}
TypeError: '>' not supported between instances of 'dict' and 'dict'

>>> {"a": 1, "b": 2} == {"a" : 4}
False

# Logical Operator: and, or, not

>>> # logical operators
>>> 2 and 3
3

>>> 4 and 2
2

>>> 2 or 3
2

>>> 4 or 2
4

>>> 2 and 0
0

>>> 0 and 2
0

>>> 1 and 0 and 5
0

>>> 1 and 0 and 0.0
0

>>> 1 or 0 or 5
1

>>> 0 or 0.0 or False or 1
1
>>> 0 or 0.0 or 1 or False
1
>>> not 2
False

>>> not 0
True

>>> all([1, 2, 3, 0])
False

>>> all([1, 2, 3, 4])
True

>>> any([1, 2, 3, 4, 0])
True

>>> any([0, 0.0, False, str(), tuple()])
False

>>> # identity operator
>>> a = 5
>>> b = 5
>>> a == b
True
>>> id
<built-in function id>

>>> id(a) == id(b)
True

>>> a is b
True
>>>
>>> l = [1, 2, 3]
>>> l1 = l[:]
>>> l == l1
True

>>> l is l1
False                               ?????????????????????????????????

>>>
>>> list1 = [1, 2, 3, [4, 5]]
>>> list2 = list1[:]
>>> list1 == list2
True
>>> list1 is list2
False

>>> list1[3] is list2[3]
True


>>> # membership
>>> l = [1, 2, 3, 4]
>>> l.index(3)
2

>>> l.index(5)
ValueError: 5 is not in list

>>> 3 in l
True

>>> 5 in l
False

>>> 3 not in l
False

>>> 5 not in l
True

>>> 3 in 3
TypeError: argument of type 'int' is not iterable

>>> (1, 2) in l
False

>>> 1, 2 in l
(1, True)
"""