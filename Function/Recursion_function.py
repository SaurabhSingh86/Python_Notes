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
#         total += num % 10
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

""" WA Recursive program to reverse a string """


