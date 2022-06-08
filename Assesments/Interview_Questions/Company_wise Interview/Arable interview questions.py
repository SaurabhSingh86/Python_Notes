"""
1.	Walk through your profile.
2.	Python Framework and development?
3.	What r u testing in your current company?
4.	list and tuple, which is faster
9.	how to use variable from 1.py in 2.py, is it possible?
10.	What is Global or local or import all functions
11.	how to define global variables?
12.	What is the strip keyword in python?
15.	What is heap keyword in python?
17.	difference between read line and read function
19.	JSON file, how to check if JSON file format is correct or not
20.	Postman tools - how to validate some API
21.	difference between get and put
22.	status codes of API
23.	Jenkins and simulators
24.	idea on Linux
25.	change the permission of dir in linux and give only exe permission
26.	How to search a specific word in text file , in linux
27.	what is the use of selenium?
28.	xpath of a specific element of login id
29.	Can 2 web pages have the same id
31.	SQL and HTML
32.	SQL - Print the name of employees older than 60+ yrs
33.	How to create a python project in pycharm
34.	How to create a package in python
36.	how to create a class in python
37.	how to create object in python class
38.	what keyword to use if you dont know how many parameters you are going to pass
39.	Python basics, how exceptions are handled, file handling, classes and objects, string operations.
40.	Generators, args kwargs , file handling
42.	How to import modules and packages and variables in python

"""

""" Sum of nos upto a range, string operations """

""" What is __init()__ """

""" diff bet single slash and double slash in python """

""" What is MRO with example """

""" l = [1,2,3]  and l2 = [4,5,6]  Expected Ans is l3 = [1,2,3,4,5,6]? """

""" What is the lambda keyword in python with example """

""" l = [shubhangi], print list in reverse order without using predefined function """

""" s = "abc    ef" – 1. delete first 2 spaces  from the string, 2. Delete all the spaces from the string """

""" How does memory allocation take place in the python program """

# -------------->>> Memory Management in Python  <<<---------------------

# 1. Garbage Collection:
# Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
# Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine
# has a garbage collector that automatically deletes that object from the heap memory



# 2. Reference Counting:
# Reference counting works by counting the number of times an object is referenced by other
# objects in the system. When references to an object are removed, the reference count for an object is decremented.
# When the reference count becomes zero, the object is deallocated.
#
# For example, Let’s suppose there are two or more variables that have the same value, so, what Python virtual
# machine does is, rather than creating another object of the same value in the private heap, it actually makes the
# second variable point to that originally existing value in the private heap. Therefore, in the case of classes,
# having a number of references may occupy a large amount of space in the memory, in such a case referencing counting
# is highly beneficial to preserve the memory to be available for other objects


# Python manages memory using reference counting semantics. Once an object is not referenced anymore, its memory is
# deallocated. But as long as there is a reference, the object will not be deallocated. Things like cyclical
# references can bite you pretty hard.

""" read the text file, after reading calculate the no of words in text file """

""" how to feed data into textbox """

