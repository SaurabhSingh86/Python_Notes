"""Lumen interview questions """

""" 
1) Introduce Yourself
Very Good afternoon,
My name is Saurabh Singh. I am basically from Rewa M.P.
If I talk about my educational background, I did my schooling in Rewa.
I’ve completed my graduation in Bachelor of Engineering with Mechanical stream (my Thesis was “Automatic Shading 
system for car by using solar Energy”). 
And also completed my post-graduation in Mtech with Thermal Engineering (my master thesis was “Transient Thermal 
Analysis of car brake rotor disc by using ANSYS software through FEA method”.)


---------------------------------------------------------------------------------------------------------------------
2) Explain about Project and Roles and Responsibilities
Talking about my professional Experience
I have 2+ years experiences in software Industry.
I worked in HDAO info system pvt ltd, Bengaluru Karnataka as a Automation Engineers. In this job, I participated/worked 
in a project-

Project Name: Online Ticket Booking System
Client Name: That was internal project of this company
Role: Automation Engineer
Testing tools: Python-Selenium, Git, Jira, Pycharm, Postman
Brief introduction: (purpose)
It’ll provide range of choice for Flights, Trains, Buses and Hotels for travelers.
The main purpose of this project was it provides a single platform for all forms of ticket booking. This project 
provides clients with an option to book tickets online and to search online for confirmation. Customers can book 
airline tickets, bus tickets, and train tickets and they can book or reserve hotels using this method.

Main features:  
Main features of this projects were:
Flights, Buses, Trains, Hotels, Others
My responsibilities were-
First Understand the requirements
Test Execution Manually in the initial stages of development.
Identifying the defect, preparing Bug report & raising the defect using Jira.
Responsible for Identifying Test Scenarios and Test Case Development.
Developed test automation framework using Pytest unit testing framework.
Responsible for Daily and Weekly Status Reports.

---------------------------------------------------------------------------------------------------------------------
3) Explain Framework And oops concept

# ---------------------------------------------------------------------------------------------------------------------

4) Where did you use Abstract class in your Project


# ---------------------------------------------------------------------------------------------------------------------
"""

""" Method overloading and method overriding,explain with example"""


# ---------------------------------------------------------------------------------------------------------------------

""" 5) Where did you use list and tuple in your Project """
# When I was working on my project i worked on list & tuple
# list was used         => [airlines names]         # Air Asia, Air India, Go First, IndiGo, SpiceJet, Vistara
# tuple was used        => (stores the multiple data like airlines name, stopage)
# dictionary was used   => {"airlines_name1":[no_of_stopage, durations, checkin_weight, meal],
#                           "airlines_name2":[no_of_stopage, durations, checkin_weight, meal]
#                            }
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
""" count the no of characters in a string without using len """
s = "langauge"
count = 0
for _ in s:
    count += 1
print(count)

# ---------------------------------------------------------------------------------------------------------------------
""" find prime no to given range (100, 200)"""
# for num in range(100, 201):
#     if num > 100:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
            # print(num, end=" ")


""" find given no is prime or not """
def prime_(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f'{num} is a prime number')


prime_(10)

# ---------------------------------------------------------------------------------------------------------------------
""" Decorators,one program"""
"example 1: "
# def sub_deco(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
#
# @sub_deco
# def sub(a, b):
#     return a - b
#
# print(sub(2, 5))

# main function o/p before using decorator => -3
# main function o/p after using decorator => 3

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
#         if isinstance(res, (int, float)):
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



"""example 2: WADF that calculates time of execution of a function """

import time


def p_outer(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(n)                       # here I'm taking just 2 seconds delay so that we'll get execution time
            func(*args, **kwargs)               # it is normal program that's why execution time is zero
            end = time.time()
            print(f'Time of execution is: {end - start}')
        return wrapper
    return delay


@p_outer(2)
def sub(a, b):
    print(f'Output of a-b is {a - b}')


sub(10, 20)

"""example 3: WADF to print "hello world" message if the user has not given input """

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
# print(display1())            # hello world,   # Python world

""" Apply multiple decorator on a single function """


# def add_deco(func):
#     def wrapper(*args, **kwargs):
#         print("Hello Everyone!!")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def decorate_intro(func):
#     def wrapper(*args, **kwargs):
#         print("Welcome to Python World")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @add_deco
# @decorate_intro
# def intro():
#     print("Python is very simple programming language")
#
#
# intro()


"""" Function,one program ,that to reverse the string """

# using slicing
# def add(string):
#     print(string[::-1])
#
# add("Python")
#
# # using reversed()
# def add(string):
#     for char in reversed(string):
#         print(char, end="")
#
# add("Language")

# ---------------------------------------------------------------------------------------------------------------------
""" program to print only even numbers from a list """

# a = [1,2,3,4,5,6,7,8,9,10]
# Method 1:
# for num in a:
#     if num % 2 == 0:
        # print(num, end=' ')
# 2 4 6 8 10

# Method 2: using list
# res = [num for num in a if num % 2 == 0]
# print(res)
# [2, 4, 6, 8, 10]

""" o/p = [10,7,4,1] """
# a = [1,2,3,4,5,6,7,8,9,10]

# method 1 using slicing
# s = a[::3]
# print(s[::-1])
# [10, 7, 4, 1]

# ---------------------------------------------------------------------------------------------------------------------
""" 
a,b,c,d = 1,2,3,4,5
a=1,b=2,c=[3,4],d=5
a = ? ,b = ?, c= ?, d= ?
"""
a, b, *c, d = 1, 2, 3, 4, 5
# print(a, b, c, d, sep=',')
# 1, 2, [3, 4], 5

# ---------------------------------------------------------------------------------------------------------------------
""" Take one string(using slicing method) he told to extract some characters in string """
s1 = "python is simple language"

"python"
# print(s1[:6])
# print(s1[-25:6:])

# print(s1[-25:-19:])
# print(s1[:-19])


"is"
# print(s1[7:9])
# print(s1[-18:-16])
# print(s1[7:-16])
# print(s1[-18:9])

"simple"
# print(s1[])
# print(s1[])
# print(s1[])
# print(s1[])

"language"
# print(s1[])
# print(s1[]
# print(s1[])# print(s1[])
# # print(s1[]
# # print(s1[])