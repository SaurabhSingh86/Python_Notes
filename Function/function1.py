# # Question: WAF to add two numbers
#
#
# """ using both keyword & positional """
# def add_(a, /, *, b):
#     c = a + b
#     return c
# add_(5, b=7)
#
# """ using positional only arguments """
# def add_(a, b, /):
#     c = a + b
#     return c
# add_(5, 7)
#
# """using keyword only arguments"""
# def add_(*, a, b):
#     c = a + b
#     return c
# add_(a=5, b=7)

"""WAF to return even no in a list """

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


# s = "hello world"
#
# d = {item: index for index, item in enumerate(s)}
# print(d)

s = "python is a language, python programming is easy"
l = s.split()

d = {for word in l}