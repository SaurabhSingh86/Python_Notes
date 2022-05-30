# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# """ 1. given two int a & b in one step you can add 2 to any num a or b
# your have to """
#
#
# # class Solution:
# #     def solve(self, A, B):
# #         if self.A > self.B:
# #             print(B)
# #             print(B + 2 = )
#
#
# """ 3.  Max height of staircase
# Given an int A respresnting the square blocks the height of each square block is 1. the task is to create a staricase a
# the first stair would require only one block. the second stair would require two blocks and son on
#  find and return the max height of the staricase"""
#
#
# """ delete middle of each """
#
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution(ListNode):
#
#     def del_middle_element(self):
#         self.list = []
#         if len(self.val) % 2 != 0:
#             rem_index = int(len(self.val)//2)
#             for i in range(len(self.val)):
#                 if i == rem_index:
#                     pass
#                 else:
#                     self.list.append(self.val[i])
#             return self.list
#
#         else:
#             rem_index = int(len(self.val) // 2)
#             for i in range(len(self.val)):
#                 if i == rem_index:
#                     pass
#                 else:
#                     self.list.append(self.val[i])
#             return self.list
#
#
# n1 = Solution([1, 2, 3, 4])
# print(n1.del_middle_element())
#
# n2 = Solution([1, 2, 3, 4, 5])
# print(n2.del_middle_element())


s = "Python Welcome Jayashr world mediumn hi"
# l = {item: len(item) for item in s.split()}
# print(l)
# res = dict(sorted(l.items(), key=lambda item: item[-1]))
# print(res)
# max_ = dict(res[-1])
# print(max_)

# l = [item for item in s.split()]
# res = sorted(l, key=len)
# print(res)
# max_len = len(res[-1])
# for word in l:
#     if len(word) == max_len:
#         print((word, len(word)), end=" ")


""" WAP to print all the second largest word in the given list """
# l = ['hai', "hello", "Not", "a", "Google", "world", "yahooo"]
#
# l1 = [len(element) for element in l]
# print(l1)
# # l1 = [1, 3, 3, 5, 5, 6, 6]
# r_dup = list(set(l1))
# print(r_dup)
# a = sorted(r_dup)
# print(a)
# s_a = (a[-2])
# for item in l:
#     if len(item) == s_a:
#         print(item, len(item), end=" ")

# """ waf to return 3 digit numbers only """
#
#
# def func(int):
#     s = str(int)
#     return s[-3:]
#
#
# print(func(123))
# print(func(1234))


# d = {"a": 1, "b": 5, "c": 6, "d": 2}
# l1 = [5, 1, 3, 4, 2]
# l = sort(l1)
# l = [1, 2, 3, 4, 5]
# n = 1
# for i in range(n):
#     rem_e = l.pop()
#     add_e = l.insert(0, rem_e)
# print(l)


# l = [1, 1, 3, 4, 4, 4]
# # output = [1, 4, 4, 4, 4]
#
#
# def func(num, k):
#     s = str(num)
#     for i in s:
#         for i in range(4):
#             if i[0]:
#                 p = int(i)+1
#                 for i in range(6):
#                     if i[1]:
#                         q = int(i)+1
#     return (p+
# print(func(512,10))

# import time
# current_time = time.localtime(time.time())
# print(current_time)


# driver.get_window_size()
# driver.set_window_size(1000, 800)

# ---------------------------------------------------------------------------------------------------------------------
""" Square of element by using function"""

# def square_element(number):
#     print(number**2)
#
#
# square_element(10)


""" Square of element by using function"""

# def square_(sequence):
#     l = []
#     for item in sequence:
#         l.append(item ** 2)
#
#     print(l)
#
#
# square_([10, 20, 2, 5, 25])     # [100, 400, 4, 25, 625]
# square_((2, 4, 6, 10))          # [4, 16, 36, 100]
# square_({10, 20})               # [100, 400]


# Note: if I want to output in the same data type that we have to pass

# def square_(sequence):
#     l = []
#     for item in sequence:
#         l.append(item ** 2)
#     if isinstance(sequence, tuple):
#         print(tuple(l))
#     elif isinstance(sequence, set):
#         print(set(l))
#     else:
#         print(l)
#
#
# square_([10, 20, 2, 5, 25])     # [100, 400, 4, 25, 625]
# square_((2, 4, 6, 10))          # (4, 16, 36, 100)
# square_({10, 20})               # {400, 100}
# ---------------------------------------------------------------------------------------------------------------------

""" sort the list"""
# l = [100, 10, 30, 99, 101, 500, 1000]
# l.sort()        # in ascending order
# print(l)        # [10, 30, 99, 100, 101, 500, 1000]

# Method2 using sorted()
# res = sorted(l)
# print(res)      # [10, 30, 99, 100, 101, 500, 1000]

# ---------------------------------------------------------------------------------------------------------------------

""" If u get a new project are u able to create basic setups w. r. t to selenium configuration files"""

# ---------------------------------------------------------------------------------------------------------------------

"1. Create a function should accept one argument as a string and u have to fetch the data from a file and u have map "
"the words and get the count of it they asked "

# path_file = r"C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\my_file1.txt"
# from collections import defaultdict
#
# def word_count(path):
#     with open(path) as file:
#         dd = defaultdict(int)
#         count = 0
#         for line in file:
#             if line.strip():
#                 for word in line.split():
#                     dd[word] += 1
#         print(dd)
#
# word_count(path_file)


# ---------------------------------------------------------------------------------------------------------------------

" 2. Function should accept a list and and if any number divisible by 3 then modify to 33 or else keep it as it is"

# def divide(*args):
#     l = args[0]
#     res = []
#     for num in l:
#         if num % 3 == 0:
#             res.append(33)
#         else:
#             res.append(num)
#     return res
#
#
# print(divide([1, 3, 13, 30, 15, 96, 99]))

# ---------------------------------------------------------------------------------------------------------------------

""" What are Abstract method and abstract class, base class.. How it work

If new class is created how is it possible access the abstract class .. Clarify the answer """

# ---------------------------------------------------------------------------------------------------------------------
""" programs to execute on list, dictionary and regular expression """

# ---------------------------------------------------------------------------------------------------------------------

""" write a program to read excel"""

# ---------------------------------------------------------------------------------------------------------------------

""" how will u Handle partial dynamic element """

# ---------------------------------------------------------------------------------------------------------------------

""" palindrome without for loop """
# using slicing

# def palindrome(string):
#     if string == string[::-1]:
#         print(f'{string} is Palindrome')
#
#     else:
#         print(f'{string} is not Palindrome')
#
# palindrome("madam")         # madam is Palindrome
# palindrome("rainbow")       # rainbow is not Palindrome

# ---------------------------------------------------------------------------------------------------------------------

""" Write a python pgm on palindrome, without using slicing """
# using for loop & concatenation


# def palindrome(string):
#     res = ""
#     for char in string:
#         res = char + res
#     if res == string:
#         print(f'{string} is Palindrome')
#     else:
#         print(f'{string} is not Palindrome')
#
#
# palindrome("malayalam")     # malayalam is Palindrome
# palindrome("python")        # python is not Palindrome

# ---------------------------------------------------------------------------------------------------------------------


""" in string no of occurrence and ignore special characters """
s = "@python& is2 programming2 language32!$"

# Method 1: using comprehension
# res = [(char, s.count(char)) for char in set(s) if char.isalnum()]
# print(res)

# Method 2: using dictionary comprehension
# res = {char: s.count(char) for char in s if char.isalnum()}
# print(res)

# Normal method
# for char in set(s):
#     if char.isalnum():
#         print(char, s.count(char))

# ---------------------------------------------------------------------------------------------------------------------

"Python program to read string from one file n print in another file"

read_file_path = r"C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\my_file1.txt"
write_file_path = r"C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\write_file1.txt"

with open(read_file_path) as read_file, open(write_file_path, 'w') as write_file:
    for line in read_file:
        write_file.write(line)

    print("Execution done successfully")





# ---------------------------------------------------------------------------------------------------------------------

""" Reversing the list of number without inbuilt function"""
# l = [1, 9, 78, 25, 32, 1, 65, 'a']


# def reverse(list_):             # if we are taking *args instead of list then we have to unpack it
#     s = ""
#     for element in list_:
#         s = str(element) + " " + s
#     return s.split()
#
#
# print(reverse(l))

# by using reverse()  i.e which is not our requirement

# l.reverse()
# print(l)

# by using reversed()
# print([element for element in reversed(l)])         # ['a', 65, 1, 32, 25, 78, 9, 1]


# ---------------------------------------------------------------------------------------------------------------------

" What is assert Asset "
# ---------------------------------------------------------------------------------------------------------------------

" Selenium grid"

# Selenium Grid is a smart proxy server that makes it easy to run tests in parallel on multiple machines. This is
# done by routing commands to remote web browser instances, where one server acts as the hub. This hub routes test
# commands that are in JSON format to multiple registered Grid nodes.

# Hub enables simultaneous execution of tests on multiple machines, managing different browsers centrally,
# instead of conducting different tests for each of them. Selenium Grid makes cross browser testing easy as a single
# test can be carried on multiple machines and browsers, all together, making it easy to analyze and compare the
# results.
#
# The two major components of the Selenium Grid architecture are:
#
# 1. Hub is a server that accepts the access requests from the WebDriver client, routing the JSON test commands to the
# remote drives on nodes. It takes instructions from the client and executes them remotely on the various nodes in
# parallel
#
# 2. Node is a remote device that consists of a native OS and a remote WebDriver. It receives requests from the
# hub in the form of JSON test commands and executes them using WebDriver

# refer notes ==> MS office notes


# ---------------------------------------------------------------------------------------------------------------------

""" Input : [10, 20, 30, 20, 40, 30]
Output : [10, 20, 30, 40]"""
# input = [10, 20, 30, 20, 40, 30]
#
# # if order doesn't matter
# print(list(set(input)))
#
# # normal method
# l = []
# for element in input:
#     if element not in l:
#         l.append(element)
#
# print(l)                # [10, 20, 30, 40]

# ---------------------------------------------------------------------------------------------------------------------

""" Write generator program to count the number of numbers inside list ."""


# def count_(list_, _count=0):
#     for _ in list_:
#         _count += 1
#     yield _count
#
#
# res = count_([1, 2, 3, 4, 5, 10])               # <generator object count_ at 0x000002B2425A66C8>
# print(next(res))                                # 6
#
# print(next(count_([3, 4, 5, 6])))               # 4



# ---------------------------------------------------------------------------------------------------------------------

""" between web browser and api """
# ---------------------------------------------------------------------------------------------------------------------
" 2. What is A/B testing?"

# ---------------------------------------------------------------------------------------------------------------------

""" 3. Can you screen freeze in selenium , how ?
For screen freeze while inspecting

Open devTools (F12).
Select the "Sources" tab.

While the element you want is displayed, press F8 (or Ctrl+/).

 This will break script execution and "freeze" the DOM exactly as it is displayed.

From this point, use Ctrl+Shift+C to select the element.

"""
# ---------------------------------------------------------------------------------------------------------------------

"""5. What is ternary operator in Python"""
# Ternary operators are also known as conditional expressions are operators that evaluate something based on a
# condition being true or false. It was added to Python in version 2.5.
# It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.
# inline if-else statement

# syntax: "true_statement" if condition else "false_statement"
" I want to check which number is greater between two numbers "
# a, b = 30, 20
#
# print(f'{a} is greater' if (a > b) else f'{b} is greater')
# 30 is greater

# ---------------------------------------------------------------------------------------------------------------------

"""  How to convert interger into string without using string methods?"""
# number = 9876
#
# # Method 1: using while method & concatenation
# num = number
# res = ""
# while num > 0:                # or while num:
#     rem = num % 10
#     if rem == 0:
#         res += '0'
#     elif rem == 1:
#         res += '1'
#     elif rem == 2:
#         res += '2'
#     elif rem == 3:
#         res += '3'
#     elif rem == 4:
#         res += '4'
#     elif rem == 5:
#         res += '5'
#     elif rem == 6:
#         res += '6'
#     elif rem == 7:
#         res += '7'
#     elif rem == 8:
#         res += '8'
#     else:
#         res += '9'
#     num = num // 10
#
# print(res[::-1])
# print(type(res))
# without using slicing
# 6789
# <class 'str'>

# using slicing or reversed() also can be used
# 9876
# <class 'str'>

# Method2: using ASCII value of digits (The idea is to use the ASCII value of the digits from 0 to 9 start from 48 – 57)
# num = 506
# s = []
# while num:
#     s.append(chr(48 + num % 10))
#     num = num // 10
# a = "".join(reversed(s))
#
# print(a)
# print(type(a))
# 506
# <class 'str'>
# ---------------------------------------------------------------------------------------------------------------------

""" 8. S = a + '[' + b + ']' + c     

 what is this process called as ?"""

# ---------------------------------------------------------------------------------------------------------------------
""" 13. Xavier is the second brother of Mala. Mala's son finished second on the finish line with Xavier's son.

Wap to identify and store common words . Replace common words with user provided input."""

# sentence = "Xavier is the second brother of Mala. Mala's son finished second on the finish line with Xavier's son."
# l1 = sentence.split()
# l = [word for word in set(l1) if l1.count(word) > 1]
# res = ",".join(l)
# print(f'These are the common words that is present in the given string: {res}')
#
# replace_word = input("Enter your word that you want to replace: ")
# replace_with = input("Enter your word that you want to replace with: ")
#
# if replace_word in res:
#     final_res = res.replace(replace_word, replace_with)
#     print(final_res)
# else:
#     print("Kindly Enter valid word that you want to replace")

# ---------------------------------------------------------------------------------------------------------------------

""" 
reverse a string,
i/p: "hi welcome to python"
o/p: "ih emoclew ot nohtyp
"""
# input = "hi welcome to python"
#
# # Method 1: using slicing:
# l = [word[::-1] for word in input.split()]
# print(" ".join(l))                  # ih emoclew ot nohtyp


# ---------------------------------------------------------------------------------------------------------------------

""" 5.how do you handle alert
6.write a sample script for alert"""

# ---------------------------------------------------------------------------------------------------------------------

""" take 2 decorator, what is order of execution?
    @decor1
    @decor2
    def func()"""

# first execute decor1 => decor2

# ---------------------------------------------------------------------------------------------------------------------

""" what is _repr_? how you used? """

# ---------------------------------------------------------------------------------------------------------------------

""" What is dataclass? """

# ---------------------------------------------------------------------------------------------------------------------
