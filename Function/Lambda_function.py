# <<<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~ Lambda function / Anonymous function  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>>>>>

# A Anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in python, anonymous function is defined using the lambda keyword
# syntax:          lambda arg1, arg2, arg3: Expression

""" WA Lambda function to check if the given number is even or not """

# even = lambda num: num % 2 == 0
# print(even(73))      # False
# print(even(86))      # True


""" WALF that multiplies two numbers """

# multiply = lambda num1, num2: num1 * num2
# print(multiply(10, 20))             # 200
# print(multiply(2.5, 10))            # 25.0
# print(multiply(2+5j, 10))           # (20+50j)

""" WALF that returns last element of the sequence """

# element = lambda sequence: sequence[-1]
#
# print(element([10, 20, "Python", "Selenium", "VS"]))              # VS


""" WALF that checks if the given string is Palindrome or not """

# Method 1:
# palindrome = lambda item: item == item[::-1]
# print(palindrome("mom"))                        #  True

# Method 2:
# palindrome = lambda item: f'{item} is Palindrome' if item == item[::-1] else f'{item} is not Palindrome'
#
# print(palindrome("madam"))
# print(palindrome("fashion"))


""" WALF that check weather the given number is even or odd & print the number in both cases """

# number = lambda num: f'{num} is even number' if num % 2 == 0 else f'{num} is odd number'
# print(number(49))
# print(number(20))

""" WALF to find greatest number between two numbers """

# greatest = lambda num1, num2: f'{num1} is greater' if num1 > num2 else f'{num2} is greater'
# print(greatest(86, 73))             # 86 is greater
# print(greatest(30.2, 49.9))         # 49.9 is greater
# print(greatest(2+5j, 5+2j))         # Type Error

""" WALF to find greatest number among three numbers """

# greatest = lambda n1, n2, n3: f'{n1} is greatest' if n1 > n2 and n1 > n3 else f'{n2} is greatest' if n2 > n3 else f'{n3} is greatest '
# print(greatest(10, 21, 51))             # 51 is greatest
# print(greatest(20, 10.52, 5.05))        # 20 is greatest
# print(greatest(101, 115.5, 110))        # 115.5 is greatest


""" WALF to cube the number """

# cube = lambda num: num ** 3
# print(cube(10))                         # 1000

""" WAP to find the output of the given expression. Expression a^2 + b^2 + 2ab"""


# expression = lambda num1, num2: num1 ** 2 + num2 ** 2 + 2 * num1 * num2
# print(expression(2, 3))                 # 25


