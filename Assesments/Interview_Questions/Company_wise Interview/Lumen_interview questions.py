"""
Lumen first round Interview questions
1. about yourself
2. about project
3. Roles & Responisbilties
4. Current company name & position

5. if you get the new features in between then 
5.1 what are the procedures to follow
5.2 what was your first expression when you get a new features
5.3 How to resolve this type of problem
5.4 Meetings

6. what type of challenges you have faced in your previous projects?
7. How to prioties the defects?
8. What types of defects you get in your projects?
9. if you didn't get the confirmation messages how to reproduce it?
10. Give me some example of priority (what is priority or types)
11. What are negative test scenario & where did you used in preious projects?
12. Minor defects in your projects

13. Python:
13.1 How to check the current version of Python
13.2 How to get the current time 
13.3 How to generate random number
Take one string s = "Saurabh Singh"
13.4 remove the duplicate items
13.5 remove the spaces in between
13.6 reversed the item i.e o/p should be Singh Saurabh

14. How to read excel file
15. what are Git & Jenkins & after this ask git command
16. Why do you want to leave your company?
17. What is the notice period?
18. Are you only static on python or you can learn any other languages
19. what is your current location?
20. you are not from Karnataka, what is the reason behind staying here?
21. What are the defects you get in previous projects? (Explain anyone)
22. Explicit wait & implicit wait
23. If a web element is present in the DOM but it is not going to click but you can see the element easily.
24. robot framework

Lumen interview questions asked in the final round
1. Where are you from?
2. Speciality of your hometown
3. Current location
4. Current company
5. self-introduction
6. Roles & responsibilities
7. Details about the previous company
8. Previous project name & explain
9. Ask so many questions which are related to the project
10. What is a framework, pytest in detail.
11. mainly focus on POM and why it is needed
12. what is qtp/uft & page object class
13. in the initial stage why did you do it manually before Automation
14. Are you part of writing the test script or modifying the test scripts?
15. How to write the test case?
16. how to write scratch if your framework is ready?
17. Almost all test cases can be Automatable why do manually in the initial stage.
18. There is a website it could to tested by another tool but my requirement is it will be automated by the python-selenium tool what will you do & what procedure you follow?
19. How the python helps in the selenium?
20. Why do you want to leave your company?
21. What is the notice period?
22. Are you willing to learn new things or languages?
23. If you want you can ask me any question (then i asked 2 questions)
24. If the framework is ready & you need to install other packages how can you do this?

They are mainly focused on projects & asked why need this (pom etc) is there any alternative & asked a question which is related to real-time scenarios & told every test cases can be automatable just you have to use another tool for that.
They are looking for candidates who have knowledge of how to create a framework, write test scripts, scratch, qtp, and uft.

"""

""" 
1) Introduce Yourself

---------------------------------------------------------------------------------------------------------------------
2) Explain about Project and Roles and Responsibilities

------------------------------------------------------------------------------------------------------------------------------------
Thanks for A2A. It's very real time question and in this situation what you can do is first verify that defect/bug is valid or not ? If it is valid then try to reproduce in different system and send screenshot, proper defect report to developer. Now even after this developer is not accepting then you can send email to respective developer regarding issue and cc to you test lead.

If Test lead is also not taking it seriously or not accepting then you can escalate this issue to Test Manager. Even though if they are not accepting then take final call with Business Analyst or Product Owner. B.A/P.O is the person who closely interact with client/business, so you can check with him. If B.A is telling this is not a bug then you can write a B.A comment in JIRA/Test Case and close it.

If B.A is accepting this as a defect/bug then send email and inform why this is a bug to respective developer, cc to development lead, test lead, test manager, B.A/P.O
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
""" remove spaces in between the sentence """
s = "Python is Programming Language"
# Method 1: using built-in-method
# res = s.replace(" ", "")
# print(res)
# print(s.replace(" ", ""))

# Method 2 using for loop
# res = ""
# for char in s:
#     if char == " ":
#         continue
#     else:
#         res += char
# print(res)
# print()
# # Method 3: using join built in
# res = "".join(s.split())
# print(res)
# ---------------------------------------------------------------------------------------------------------------------
""" count the no of characters in a string without using len """
# s = "langauge"
# count = 0
# for _ in s:
#     count += 1
# print(count)

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
# def prime_(num):
#     for i in range(2, num//2 + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f'{num} is a prime number')
#
#
# prime_(10)

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

# import time
#
#
# def p_outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             time.sleep(n)                       # here I'm taking just 2 seconds delay so that we'll get execution time
#             func(*args, **kwargs)               # it is normal program that's why execution time is zero
#             end = time.time()
#             print(f'Time of execution is: {end - start}')
#         return wrapper
#     return delay
#
#
# @p_outer(2)
# def sub(a, b):
#     print(f'Output of a-b is {a - b}')
#
#
# sub(10, 20)

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
# a, b, *c, d = 1, 2, 3, 4, 5
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



import time

# current_time = time.localtime(time.time())
# print(f"Current time is {current_time}")

import random
print(random.randint(1,101))
