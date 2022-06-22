"""
Lumen first round Interview questions
1. about yourself
2. about project
3. Roles & Responisbilties
4. Current company name & position"""

"""5. if you get the new features in between then """

"5.1 what are the procedures to follow"
# you know changes are the part of the work. When I was working on previous company, we were working on Agile Environment
# In Agile Environment, Where the objects & the application scenario flows are constantly changing.
# you know if requirement changes => corresponding design changes => if the design changes the code has to be changed => because of which Testing approach will change because there will be lot of defects while testing.


" 5.2 what was your first expression when you get a new features"
# when I was new on that then I was worried later on I was familier with it.

"5.3 How to resolve this type of problem"
# As Automation Test Engineer first I've to understand the updated requirement if there is a problem to understand the requirement then discuss with Manual test engineer, Test lead, Project Manager even though I still have problem then discussed with BA.

# If we get any changes then we discussed on meetings, in this meeting scrum master tells what are the procedures we have to follow.


"5.4 Meetings"
# Meetings coducted in Agile Enviroment
# 1. Sprint planning meeting: Assign the task to each engg. & keep a track of it.
#
# 2. Stand-up meeting: here entire scrum team meets, this meeting is completely done by scrum master. In this meeting
# each engg. Should tell
# 2.1 What they have done yesterday
# 2.2 What are the hurdles/problems they have faced yesterday’s task
# 2.3 What activities are planning to do today?
#
# 3. Sprint review meeting: Demo of the product
#
# 4. Retrospect meeting:  discuss achievements & drawbacks or we can say that summary of the product.


"""6. what type of challenges you have faced in your previous projects? 7. How to prioties the defects?"""
# We are Test Engineer & we have good knowledge on the s/w & we know how each features work so on the basic of knowledge we identify the severity & priority.

# Note: Severity & Priority both are given by Test Engineers. (Test lead, Development lead also give the priority)
# Developer will always fix the defect based on the priority given & not an severity.

"""10. Give me some example of priority (what is priority or types)"""
# P1  => high       => resolve immediately
# P2  => Medium     => within 2-3 days
# P3  => Low        => within a week

"""
8. What types of defects you get in your projects?
9. if you didn't get the confirmation messages how to reproduce it?

11. What are negative test scenario & where did you used in preious projects?
12. Minor defects in your projects

"""

# 13. Python:
""" 13.1 How to check the current version of Python """
# There are two ways:
# 1. in Pycharm in terminal we write    =>  python --version
# 2. in Command prompt                  =>  python --version
# 3. in Pycharm                         =>  if we observe carefully right-bottom it is showing version of the Python

""" 13.2 How to get the current time """
# first we have to import some module

# Method 1:
# from datetime import datetime
# print(datetime.now())
# 2022-06-21 20:31:49.569863

# from datetime import date
# print(date.today())
# 2022-06-21

# Method 2:
# import time
# print(time.localtime(time.time()))
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=21, tm_hour=20, tm_min=30, tm_sec=29, tm_wday=1, tm_yday=172, tm_isdst=0)


""" 13.3 How to generate random number """
# first we have to import
# import random
# print(random.randint(1, 101))

""" 
Take one string s = "Saurabh Singh"
13.4 remove the duplicate items
13.5 remove the spaces in between
13.6 reversed the item i.e o/p should be Singh Saurabh
"""
s = "Saurabh Singh"

# 13.4 remove the duplicate items


# 13.5 remove the spaces in between


# 13.6 reversed the item i.e o/p should be Singh Saurabh


""" 14. How to read excel file"""
# Step 1: First we have to import xlrd
# Step 2: opening the excel file / workbook
# Step 3: Opening the spreadsheet & getting its handle
# Step 4: get the data in entire sheet
# skip the headers
# get each row

# Step 1: First we have to import xlrd
# import xlrd
#
# excel_file_path = r"C:\Users\Saurabh\Desktop\Mark_sheet.xlsx"
#
# # Step 2: opening the excel file / workbook
# book = xlrd.open_workbook(excel_file_path)
#
# # Step 3: Opening the spreadsheet & getting its handle
# sheet = book.sheet_by_name("Marks_Sheet1")
#
# # Step 4: get the data in entire sheet
# data = sheet.get_rows()
#
# # skip the headers
# header = next(data)
#
# # get each row
# mark_sheets = {}
# for row in data:
#     mark_sheets[row[0].value] = (row[1].value, row[2].value)
#
# print(mark_sheets)


""" 15. what are Git & Jenkins & after this ask git command """

# Git & Git Commands
# In previous project for version control we were using "Github" tool. I was working on Pycharm in this platform
# there is an option commit, push, update-project, clone, merge etc. We used directly.

# Jenkins
# Jenkins is an open source continuous integration/continuous delivery and deployment (CI/CD) automation software
# DevOps tool written in the Java programming language. It is used to implement CI/CD workflows, called pipelines.
# Programming languages used: Java

""" 16. Why do you want to leave your company? """
# Currently, I'm in bench & looking for good projects. Test Yantra also provides me opportuninty that's why I'm here.

"""17. What is the notice period?"""
# Immediate join

"""18. Are you only static on python or you can learn any other languages"""
# I'm always willing to learn new language/skills. If I get an opportunity to work with any other languagae then I'll
#  definitely learn & work on it.

"""19. what is your current location?"""
# Srinivas nagar, 9th main road, near Venkateshwara temple, Banashankari

"""20. you are not from Karnataka, what is the reason behind staying here?"""
# There are many reason
# 1. Career wise => it is one of the best place for me where I can build my career
# 2. Weather suits me (not too hot)
# 3. People are very kind & helping in nature
# 4. There are lots of place where I want to visit like Iskan temple etc

# Suppose if they asked what types of difficulties you are facing here then
# 1. food issues
# 2. sometimes we face language problem
# 3. sometime weather can't be predicted


"""21. What are the defects you get in previous projects? (Explain anyone)"""
#

"""22. Explicit wait & implicit wait"""


"""23. If a web element is present in the DOM but it is not going to click but you can see the element easily."""


"""24. robot framework"""


""" Do you have any questions """
# Yes, I would like to know about if I get selected what will be my roles & responsibilities?



""" Lumen interview questions asked in the final round
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


---------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------------------
Thanks for A2A. It's very real time question and in this situation what you can do is first verify that defect/bug is 
valid or not ? If it is valid then try to reproduce in different system and send screenshot, proper defect report to 
developer. Now even after this developer is not accepting then you can send email to respective developer regarding 
issue and cc to you test lead.

If Test lead is also not taking it seriously or not accepting then you can escalate this issue to Test Manager. 
Even though if they are not accepting then take final call with Business Analyst or Product Owner. B.A/P.O is the 
person who closely interact with client/business, so you can check with him. If B.A is telling this is not a bug then 
you can write a B.A comment in JIRA/Test Case and close it.

If B.A is accepting this as a defect/bug then send email and inform why this is a bug to respective developer, 
cc to development lead, test lead, test manager, B.A/P.O
---------------------------------------------------------------------------------------------------------------------
3) Explain Framework And oops concept

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
"""
# ---------------------------------------------------------------------------------------------------------------------

""" 5) Where did you use list and tuple in your Project """
# When I was working on my project I used list & tuple so many times
# for Shopping cart system ~~~~~~~~>>>>
# list was used         =>  [name of all categories]     # Men, Women, Kids
# tuple was used        =>  (stores the multiple data like categories, total no of clothes)
#                           ('men', 500), ('women', 1000), ('Kids', 600)
# dictionary was used   =>  {
#                             'men': [colors, types, brands, pattern],
#                            'women': (colors, types, brands, pattern),
#                            'kids' : [colors, types, brands, pattern]
#                           }

# for online ticket booking system ~~~~~~~~>>
# list was used         => [airlines names]         # Air Asia, Air India, Go First, IndiGo, SpiceJet, Vistara
# tuple was used        => (stores the multiple data like airlines name, stopage)
# dictionary was used   => {"airlines_name1":[no_of_stopage, durations, checkin_weight, meal],
#                           "airlines_name2":[no_of_stopage, durations, checkin_weight, meal]
#                            }
# ---------------------------------------------------------------------------------------------------------------------
""" 8. difference between list and dict """
# Both are built-in (collection value) data types in Python but there are some differences in between

# 1. list is mutable data type & dictionary is also mutable data type but in dictionary key must be Immutable data type
# value can be mutable.
#
# 2. List contains duplicates value whereas, in dictionary value can be duplicates but key must be unique or not be
# duplicated otherwise it can be a data loss.

# 3. Syntax wise: list collection is enclosed by Square braces [] & all the elements seperated by comma (,) operators,
# while, dictionary collection is enclosed by curly braces {} & each pair is seperated by comma(,) operators & key &
# value is seperated by colon (:).

# 4. Indexing & slicing both are possible in List but in dictionary can't be supported. Dictionaries are indexed by keys

# 5. some built-in-methods of list are => .append(), .insert(), .remove(), .index(), .count(), .clear(), .sort(), .reverse() etc
# some buit-in-methods of Dictionary are => .keys(), .values(), .items(), .get(), .pop(), .popitem(), .clear(), .update({key: value})
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
a, b, *c, d = 1, 2, 3, 4, 5
# print(a, b, c, d, sep=',')                    # 1, 2, [3, 4], 5
# print([a, b, c, d])                           # [1, 2, [3, 4], 5]


# ---------------------------------------------------------------------------------------------------------------------
""" 10.Explain slicing """
# Slicing is a process of extracting multiple data at a time.
# Syntax: variable_name = [Start_index: End_index: Step_value]

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
1. self introduction 
2. Tell me about your frame work which you used in your project 
6. Can you tell about Defect life cycle 

7. i have 50 test cases , you are doing Regression testing , SO you have only 2 days of time to complete the 
  regression testing . the scenario is , you has to complete the regression testing with in end of day(today).
  Tomorrow is the release and you only the QA in your team , and you have 50 test cases . So how you can complete
  regression testing with in the day 
  
9. difference between .py and .pyc

12.How to combine data frames ?

15.Explain OOP 

24.how you can going to sink the code from local repository to global repository ?
25.How can you revert the codes ?

27.what is sql ?
28.Find the 2nd highest sal and details of the employee from employee dynamic table 




"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 4. Difference between smoke and sanity testing """
# “Testing the basic or critical features before we do through testing, is called as Smoke Testing.
# Smoke Testing is also known as Sanity testing but there are some difference in between
#
# 1. Smoke Testing is done to check the basic & critical features of an application
# It is done to check for the fixed defect & again defects for basic features.
#
# 2. Smoke Testing is documented
# Sanity testing is not documented
#
# 3. Smoke can be done by developer & Test engineer
# only Test Engineer
#
# 4. It is done on new builds
# It is done on old build

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 3. what is API testing ? how you used  20.Explain about Postman. 21.How you test in Postman ? """
# in previous project we were mainly focus on Python-Selenium, I didn't get any opportunity to work on Application
# Programming Interface i.e. API, but I'm willing to work on that so I'm trying to learn myself till now I've some basic
#  knowledge on API. Postman, RestAssured are some API tools, where we can perform "CRUD" operations on the given URL
#  (URL is provided by Developer) C stands for Create (but in API Post), R => Read (Get), U => Update (Put/Fetch) and
#  D => Delete (Delete).
#  We use API when the frontend is not ready.
#  There are two types of website 1. Normal website 2. Secured website
#  While doing on Secured website we need authentication so here we use "Bearer Token", "OAuth 2.0".
#  let us take one e.g.
#  Suppose I want to perform API on Github. We can't perform directly because it is secured website so what can I do.
#  here I've an account on Github so I can create "Barer Token" or "OAuth 2.0" then we can perform the operations.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 22.What you know about GIT ? 23.For what purpose we use GIT ? """
# In previous project for version control we were using "Github" tool. I was working on Pycharm in this platform
# there is an option commit, push, update-project, clone, merge etc. We used directly.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 13.What is python path ?  """
# It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is
# also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to
# determine which module to load.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 29.how can you verify the log ? """
# in my project I was using Assert: The assert statement in Python is meant to debug your code, not to handle run
# time errors.
# I used assertion condition inside the class:
# if assertion condition is True => Program continue to run it means doesn't do anything & continue the normal flow
# of execution.
# if assertion conditon is False => Assertion stops programs & give the AssertionError along with optional msg

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 5. Difference between Load testing and Stress testing """
# These types of testing are done under performance testing:
# In performance testing, testing the stability & response time an application by applying load.
# Stability       => it is the ability to withstand the load.
# Response time   => It is the total time taken to send the request to the server, time taken to run the program & also
#                     the time taken to response-back to the user i.e. T = T1 + T2 + T3
# Load            => load is nothing but the number of users.
#
# Types of performance testing:
# testing the stability & response time of an application
# 1. Load testing     => by applying the load which is equal to or less than the number of users
# 2. Stress testing   => by applying the load which is more than the number of users
# 3. Volume testing   => by transferring huge volume of data
# 4. Soak testing     => for a particular period of time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 14.what is local and global variables in the python? """
# Global variable: Variables declared outside a function or in global space are called global variables. These variables
# can be accessed by any function in the program.

# Local Variable: Any variable declared inside a function is known as a local variable. This variable is present in the
#  local space and not in the global space.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" 30.Define agile methodology """
# It is a model where we develop the software is an incremental & iterative manner.
# In order to overcome the drawback which was there in all previous models we have come up with Agile model
# Here we build larger product in a shorter cycles called as sprint.

# Incremental       => because we are giving the software in incremental order to the customer.
# Iterative model   => bcz in all the cycle we are repeating the same process/stages
#                       i.e Requirement collection, Feasibility study, Design, code, test

# Meeting conducted in Agile Methodlogy
# Sprint planning meeting: Assign the task to each engg. & keep a track of it.
# Stand-up meeting: here entire scrum team meets, this meeting is completely done by scrum master. In this meeting each engg. Should tell
# What they have done yesterday
# What are the hurdles/problems they have faced yesterday’s task
# What activities are planning to do today?
# Sprint review meeting: Demo of the product
# Retrospect meeting:  discuss achievements & drawbacks or we can say that summary of the product.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""16.what is polymorphism ?"""
# Poly means 		=> 	Many
# Morphs means 	    => 	forms
# Polymorphism contains the topic like:
#
# 1) Overloading:
# 	1) Operator Overloading
# 	2) Method Overloading
# 	3) Constructor Overloading

# 2) Overriding:
# 	1) Method Overriding
# 	2) Constructor Overriding

""" Method overloading VS method overriding,explain with example"""

# Method Overloading
# If two methods have the same name but different type of arguments then those methods are said to be overloaded methods.
#
# In Python, method overloading is not possible.
#
# If we are trying to declare multiple methods with same name and different number of arguments then python will always
# consider only last method.

# class demo:
#     def m1(self):
#         print("no argument method")
#
#     def m1(self,x):
#         print("one argument method")
#
#     def m1(self,x,y):
#         print("two argument method")
#
#
# s=demo()
# s.m1(2,7)


# Method Overriding
# Whatever members available in the parent class are by default available to the child class through inheritance.
#
# If the child class is not satisfied with parent class implementation, then, the  child class is allowed to redefine
# that method in the child class based on its requirement. This concept is called overriding.


# class Parent:
#     def greet(self):
#         print("Good Morning")
#
#
# class Child(Parent):
#     def greet(self):
#         print("Hello Everyone, Have a great day")
#
#
# s = Child()
# s.greet()			# Hello Everyone, Have a great day

""" Constructor Overloading VS Constructor Overriding"""
# Constructor Overloading:
# Constructor overloading is not possible in Python. If we define multiple constructors then the last constructor will
# be considered.

# class demo:
#     def __init__(self):
#         print("no argument method")
#     def __init__(self,x):
#         print("one argument method")
#     def __init__(self,x,y):
#         print("two argument method")
# s = demo(2,3)


# Constructor Overriding:
# overriding concept is applicable for constructor overriding

# class Parent:
#     def __init__(self):
#         print("parent constructor")
# class Child(Parent):
#     def __init__(self):
#         print("child constructor")
#
# s = Child()


""" Operator Overloading """
# •	We can use the same operator for multiple purposes, which is nothing but operator overloading.
# •	Python supports operator overloading.
# •	java won't support operator overloading
#
# e.g 1: same + operator can be used for Arithmetic addition and String concatenation
#  print(10 + 20)
#  print('hello' + 'world')
#
# e.g 2: same * operator can be used for multiplication and string repetition purposes.
#  print(10 * 20)
#  print("hai" * 3)
#
# e.g 3: operator overloading can also be used in the object that is created from class:--->
#
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#
# b1 = Book(200)
# b2 = Book(300)
#
# print(b1 + b2)
#
# #TypeError: unsupported operand type(s) for +: 'book' and 'book'
#
# # How to overcome it
#
# Note:->
# •	Python provides support for operator overloading using a Magic method
# •	For every operator Magic Methods are available
# •	Here in this example whenever the controller/interpreter sees print(b1+b2), automatically it calls ma agic method, here we have use magic method   __add__(self, other)
#
#
# S.N.	Symbols	Syntax
# 1.		+	object.__add__(self, other)
# 2.		-	object.__sub__(self, other)
# 3.		*	object.__mul__(self, other)
# 4.		/	object.__div__(self, other)
# 5.		//	object.__ floordiv __(self, other)
# 6.		%	object.__ mod __(self, other)
# 7.		**	object.__pow__(self, other)
# 8.		+=	object.__iadd__(self, other)
# 9.		-=	object.__isub__(self, other)
# 10.		*=	object.__imul__(self, other)
# 11.		/=	object.__idiv__(self, other)
# 12.		//=	object.__ ifloordiv__(self, other)
# 13.		%=	object.__ imod__(self, other)
# 14.		**=	object.__ipow__(self, other)
# 15.		<	object.__lt__(self, other)
# 16.		<=	object.__le__(self, other)
# 17.		>	object.__gt__(self, other)
# 18.		>=	object.__ge__(self, other)
# 19.		==	object.__eq__(self, other)
# 20.		!=	object.__ne__(self, other)
#
#
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):             # __add__ is a magic method to add two object that is created from class
#         return self.pages + other.pages   # here self is nothing but b1 object & other is  nothing but b2 object
#
#
# b1 = Book(200)
# b2 = Book(300)
#
# print(b1+b2)            # 500
#
#
# # employee Class Objects:---->
#
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __ge__(self,other):
#         return self.salary >= other.salary
#
#
# e1=employee("Elon", 20000)
# e2=employee("Steve", 20000)
#
# print(e1 >= e2)
#
#
# # Overloading <= employee Class Objects:---->
#
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __le__(self,other):
#         return self.salary<=other.salary
#
#
# e1=employee("Elon",20000)
# e2=employee("Steve",30000)
# print(e1<=e2)
#
# # Note:--> <= can also manage >= and vice versa
#
# Program to Overload Multiplication Operator to Work on employee salary Objects:
#
# class employee:
#     def __init__(self,name,salary_per_day):
#         self.name=name
#         self.salary_per_day=salary_per_day
#
#
#
# class working_day:
#     def __init__(self,no_of_working_days):
#         self.no_of_working_days=no_of_working_days
#
#     def __mul__(self,other):
#         return self.no_of_working_days * other.salary_per_day
#
#
# e=employee("Mark",750)
# s=working_day(27)
# print(s*e)

"""Que. What are magic methods?"""
#
# Magic methods are special methods which starts and ends with double underscores. It is internally called by python. We can customise the behaviour of an object or class using magic methods. They are also called as protocols.
#
# e.g. when you ask for the length of the list len(names) internally python will call _len_ method on list object.
#
# E.g. when you check for membership "apple" in names python internally triggers _contains_("apple")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""17.What is data Abstraction ? """
""" 4) Where did you use Abstract class in your Project """


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""18.What is data Encapsulation ?"""
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""19.Explain Inheritance """
# What ever variables, methods and constructors available in the parent class by default available to the child classes
# & we are not required to rewrite.

#__________Advantages_of_inheritance______________:
#    1.  Code reusability
#    2.  Code extensibility

#________________Types_of_Inheritance______________:
#    1.  Single inheritance
#    2.  Multi-level inheritance
#    3.  Hierarchical inheritance
#    4.  Multiple inheritance
#    5.  Hybrid inheritance
#    6.  Cyclic inheritance
# Python as well as Java won't support cyclic inheritance.

# Constructor overloading
# Multiple constructor is possible in a single class
# if we have multiple constructor (__init__) in a class then it will considered latest one.
# by default constructor will return None
# Multiple constructor is not possible in Python => to solve this problem by using default value => i.e. constructor overloading

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" 11. what are the keywords available in Python ? """
# Keywords are reserved words that have a specific meaning associated with them, we can't modify the meaning of
# Keywords, we can only utilize the meaning as per our requirement in the program.
#
# Keywords are case-sensitive
#
# Total no of keywords, depends on Version of the software
# e.g 33 keywords => before Python 3.7
#     35 keywords =>  after Python 3.7
#
# Some keywords are:
# import, True, False, is, in, not, if, else, elif, def, for, while, lambda, global, nonlocal, break, continue, pass,
# None, class, return, yield, try, raise, with, except, finally, and, or, as, assert, await, from
#
# Que. How to get all keyword
# 1. help("keywords)
# 2. import keyword
# keyword.kwlist
#
# To check whether a string is Keyword or not
# keyword.iskeyword('string')
#
# Word in orange color    => Keywords
# word in purple colour   => Built-in-function