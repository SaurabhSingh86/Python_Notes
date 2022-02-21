""" 1. Check whether the user given number is factorial or not using recursion """
# we can write this program most effective manner


# def factorial(required_fact, num=1, fact=1):
#     if num > 0:
#         fact *= num
#         if fact <= required_fact:
#             if fact == required_fact:
#                 return f'{required_fact} is factorial'
#             return factorial(required_fact, num + 1, fact)
#
#
# required_facto = int(input("Enter a number: "))
# print(factorial(required_facto))


""" 2. Write a recursion program to find the fibonacci series until the given range. """
# n = 20
#
#
# def fibo(num, a=0, b=1):
#     if a <= num:
#         print(a, end=" ")
#         c = a + b
#         return fibo(num, a=b, b=c)
#
#
# fibo(n)

""" 3. WARP to print the reverse of string values in the list """
# l = [1, "hello", "bye", 2, "thanks"]


# def reverse_(sequence, l1=[]):
#     if sequence:
#         if isinstance(sequence[0], str):
#             l1.append(sequence[0][::-1])
#             return reverse_(sequence[1:], l1)
#         return reverse_(sequence[1:], l1)
#     return l1
#
#
# list_ = [1, "hello", "bye", 2, "thanks"]
# print(reverse_(list_))


""" 4. WARP that prints the number 10, ten times """


# def display(num):
#     if num:
#         print(10)
#         return display(num - 1)
#
#
# display(10)

""" WARP to find the sum first n numbers """


# def sum_n_numbers(num, total=0):
#     if num > 0:
#         total += num
#         return sum_n_numbers(num - 1, total)
#     return total
#
#
# n = int(input("Enter a number: "))
# print(sum_n_numbers(n))
