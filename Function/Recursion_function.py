# ~~~~~~~~~~~~~~~~~~~~>> Recursion <<~~~~~~~~~~~~~~~~~~~~~~~

# Function calling itself until the condition is being satisfied.
# used to avoid loops in some cases
# by using getrecursionlimit() => we find the recursion limit

# There are two methods to check recursion limit
# Method 1:
# import sys
# sys.getrecursionlimit()                     # nothing to display
# print(sys.getrecursionlimit())              # 1000

# Method 2:
from sys import getrecursionlimit
# getrecursionlimit()                           # nothing to display
# print(getrecursionlimit())                    # 1000


# by using setrecursionlimit()  => We can change the recursion limit
# Method 1:
import sys
# sys.setrecursionlimit(2000)                     # Nothing to display
# print(sys.setrecursionlimit(2000))              # None
# getrecursionlimit()                             # Nothing to display
# print(getrecursionlimit())                      # 2000

# sys.setrecursionlimit(500)
# print(sys.setrecursionlimit())                  # Type Error

# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())                  # 10

# Method 2
from sys import setrecursionlimit
# setrecursionlimit(1500)                         # nothing to display
# print(getrecursionlimit())                      # 1500


"""WA Recursive program to print number from 1 to 10 """
# Method 1:


# def count_(start, end):
#     if start <= end:
#         print(start, end=" ")
#         return count_(start + 1, end)
#
#
# count_(1, 10)


""" WA Recursive program to print number from 10 to 1 """


# def rev_count(start, end):
#     if start >= end:
#         print(start, end=" ")
#         return rev_count(start-1, end)
#
#
# rev_count(10, 1)


""" WA Recursive program to print number from -1 to -10 """


# def n_count(start, end):
#     if start >= end:
#         print(start, end=" ")
#         return n_count(start - 1, end)
#
#
# n_count(-1, -10)


""" WA Recursive program to print number from -10 to -1 """


# def n_rev_count(start, end):
#     if start <= end:
#         print(start, end=" ")
#         return n_rev_count(start + 1, end)
#
#
# n_rev_count(-10, -1)


""" WA Recursive program to add the digits of a number """


# def sum_(num, total=0):
#     if num > 0:
#         last = num % 10
#         total += last
#         return sum_(num//10, total)
#
#     return total
#
#
# print(sum_(1234))


""" WA Recursive program to find sum of first n numbers input = 4, output = 4+3+2+1"""

# Method 1: 1st preference


# def sum_digit(num, total=0):
#     if num > 0:
#         total += num
#         return sum_digit(num - 1, total)
#
#     return total
#
#
# print(sum_digit(6))


""" WA Recursive program to find factorial of number """


# def factorial(num, fact=1):
#     if num > 0:
#         fact *= num
#         return factorial(num-1, fact)
#     return fact
#
#
# print(factorial(5))


""" WA Recursive program to count the number of digit in a number """

# Method 1:
# def count_digit(num, count=0):
#     if num > 0:
#         count += 1
#         return count_digit(num//10, count)
#     return count
#
#
# print(count_digit(6149867))


# Method 2:
# def n_digit(num, count=0):
#     if num > 0:
#         last = num % 10
#         count += 1
#         return n_digit(num//10, count)
#     return count
#
#
# print(n_digit(1234506789))


""" WA Recursive program to reverse a string """

# Method 1:


# def reverse_(string, res=""):
#     if len(string) > 0:
#         res = string[0] + res
#         return reverse_(string[1::], res)
#     return res
#
#
# print(reverse_("VS Code"))

# Method 2:


def rev_string(string, i=0, res=""):
    if i < len(string):
        res = string[i] + res
        return rev_string(string, i+1, res)
    return res


print(rev_string("VS Code"))

# Method 2: ???????????????????????????????????????????????? is it correct ?


# def reverse_(s, res=""):
#     if s:
#         res = s[0] + res
#         return reverse_(s[1:], res)
#     return res
#
#
# string = "Python World"
# print(reverse_(string))


""" 1 WARP to print fibonacci series in the user-defined range """


# def fibo(num, step=1, a=0, b=1):
#     if step <= num:
#         print(a, end=" ")
#         c = a + b
#         # step += 1
#         return fibo(num, step+1, a=b, b=c)
#
#
# fibo(10)                          # 0 1 1 2 3 5 8 13 21 34

"""2 WARF that returns fibonacci series upto the number specified """

# def fibo(num, a=0, b=1):
#     if a <= num:
#         print(a, end=" ")
#         c = a + b
#         return fibo(num, a=b, b=c)
#
#
# fibo(10)                          # 0 1 1 2 3 5 8

# or

# def fibo(num, a=0, b=1):
#     if a <= num:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#         return fibo(num, a, b)
#
#
# fibo(10)                          # 0 1 1 2 3 5 8


""" 3. WARF to returns nth fibonacci number  """


# def fibo(num, step=1, a=0, b=1):
#     if step < num:
#         c = a + b
#         step += 1
#         return fibo(num, step, a=b, b=c)
#     return a
#
#
# print(fibo(10))                  # 8


""" 4. WARF that checks if the given number is fibonacci or not """


# def fibo(num, a=0, b=1):
#     if a <= num:
#         if a == num:
#             return f'{num} is a fibonacci number'
#         else:
#             c = a + b
#             return fibo(num, a=b, b=c)
#     return f'{num} is not a fibonacci number'
#
#
# print(fibo(10))


""" WARP to check weather a given number is Armstrong Number or not """
# Armstrong Number: It is a number which is equal to the sum of cube of its digits.
# e.g. 153 = 1^3 + 5^3 + 3^3 = 153 i.e. 153 is Armstrong number
# similarly 370


# def armstrong_no(num, total=0):
#     if num > 0:
#         last = num % 10
#         total += last**3
#         return armstrong_no(num//10, total)
#     return total
#
#
# num = 153
# a = num
# if armstrong_no(num) == a:
#     print(f'{a} is a Armstrong number')
# else:
#     print(f'{a} is not a Armstrong number')


"""Armstrong numbers """   #????????? is it right way or not


# def armstrong(num, total=0):
#     if num > 0:
#         last = num % 10
#         total += last**3
#         return armstrong(num//10, total)
#     if total == a:
#         return f'{a} is a armstrong number'
#     else:
#         return f'{a} is not a armstrong number'
#
#
# a = 153
# print(armstrong(a))

""" Prime or not """


# def prime(num, start=2):
#     if start <

""" Prime factor of a given number """

""" String is palindrome or not """

""" Number is palindrome or not """


""" What is the output of the following code ?"""


# def recursive_func(string):
#     print(string)
#     return recursive_func(string[1::])
# 
#
# recursive_func("hai")               # Recursion Error: Maximum recursion depth exceeded while calling a python object

""" WAP to check"""