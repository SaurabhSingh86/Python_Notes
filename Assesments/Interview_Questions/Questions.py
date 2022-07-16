""" 1. Write a program to find the length of the string without using inbuilt function (len)"""

# s = "marshmello"
# count_ = 0
# for _ in s:
#     count_ += 1
# print(count_)

# Method 2: by using function

# def count_(traverse):
#     _count = 0
#     for _ in traverse:
#         _count += 1
#     return _count


# print(count_("marshmello"))                         # 10
# print(count_([1, 2, "hai", 9]))                     # 4
# print(count_((1, 2, 9, 66)))                        # 4
# print(count_({1, 9, 8}))                            # 3
# print(count_({"a": 1, "b": 2, "c": 3}))             # 3


""" 2. Write a program to reverse a string without using any inbuilt functions """
# s = "dream big"
# s = "unicorn"

# ==> without using built-in-function

# Method 1: by using concatenation
# output = ""
# for char in s:
#     output = char + output
#
# print(output)

# ==> by using built-in-function
# Method 1: by using range
# res = ""
# for index in range(len(s)-1, -1, -1):
#     res += s[index]
#
# print(res)                                # gib maerd

# Method 3: by using reversed
# for char in reversed(s):
#     print(char,end="")


""" 3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe". """
# s = "Hello World"

# Method 1:
# res = s.replace("World", "Universe")
# print(res)


""" 4. How to convert a string to a list and vice-versa. """
# => convert a string into a list       =====>>> by using split() built-in-function


# def convert_into_list(any_string):
#     return any_string.split()
#
#
# print(convert_into_list("love me like you do"))         # ['love', 'me', 'like', 'you', 'do']

# => convert list into a string     ====>>>>  by using join() built-in-function


# def convert_into_string(any_list):
#     res = " ".join(any_list)
#     return res
#
#
# print(convert_into_string(["I", "am", "a", "foodie", "Person."]))    # I am a foodie Person.
# l = ["I", "am", "a", "foodie", "Person."]
# print(" ".join(l))


""" 5. Convert the string "Hello welcome to Python" to a comma separated string. """

# given_string = "Hello welcome to Python"
# list_ = given_string.split()
# res = ",".join(list_)
# print(res)                                      # Hello,welcome,to,Python


""" 6. Write a program to print alternate characters in a string. """

# Method 1: by using slicing
# sentence = "Money Heist"
# print(sentence[::2])                        # MnyHit


# Method 2: by using range
# for i in range(0, len(sentence), 2):
#     print(sentence[i], end="")              # MnyHit


""" 7. Write a Program to print ascii values of the characters present in a string. """
# Method 1: using function


# def ascii_value(character):
#     return ord(character)
#
#
# print(ascii_value("P"))                 # 80
# print(ascii_value("PS"))

# def ascii_value(character):
#     for char in character:
#         print(ord(char), end=" ")
#
#
# ascii_value("Sea")
# print()
# ascii_value("p")
# print()
# ascii_value(input("Enter a character: "))

# Method 2:
# user_input = input("Enter a character: ")
# print(ord(user_input))                  # p = 112


""" 8. Write program to convert upper case to lower case and vice-versa without using inbuilt method. """
# sentence = "Ocean Of The Blue Sea"
# res = ""
# for char in sentence:
#     if 'a' <= char <= 'z':
#         res += chr(ord(char) - 32)
#     elif "A" <= char <= "Z":
#         res += chr(ord(char) + 32)
#     else:
#         res += char
# print(res)


# Method 2: **************************************************************************************************

# def convert(any_string):
#     l = []
#     for char in any_string:
#         temp = ord(char)
#         if temp >= 97 and temp <= 122:
#             l.append(chr(temp - 32))
#         elif temp >= 65 and temp <= 90:
#             l.append(chr(temp + 32))
#         else:
#             l.append(char)
#     return "".join(l)
#
# print(convert("Ramta Jogi"))


""" 9. Write program to swap two numbers without using 3rd variable. """
# Method 1: using function


# def swap_num(a, b):
#     a, b = b, a
#     return a, b
#
#
# print(swap_num(11, 21))                   # (21, 11)


""" 10. Write program to merge two different lists. """

# a = [1, 2, 3]
# b = [4, 5, 6]

# Method 1: using unpacking
# merge_list = [*a, *b]
# print(merge_list)                       # [1, 2, 3, 4, 5, 6]

# Method 2: using concatenation
# c = a + b
# print(c)                                # [1, 2, 3, 4, 5, 6]


# Method 3: Using chain
# from itertools import chain
# s = chain(a, b)                         # Returns an Iterators
# print(list(s))


""" 11. Write program to read a random line in a file. (ex. 50, 65, 78th line) """
# n = int(input("Enter your required line number: "))


# Method 1: using enumerate
# with open(path) as file:
#     for line_number, line in enumerate(file, start=1):
#         if line_number == n:
#             print(line_number, line)


# Method 2:
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count == n:
#             print(count, line)
#             break


# Method 3: using islice
# from itertools import islice
# with open(path) as file:
#     res = islice(file, n-1, n)
#     print(list(res))


""" 12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line) """
# # Method 1: using islice
# with open(path) as file:
#     res = islice(file, )

""" 13 Program to print last "N" lines of a file. """
# path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\my_file1.txt'
#
# from collections import deque
# n = int(input("Enter required number of lines: "))
# with open(path) as file:
#     lines = deque(file, n)
#     print(list(lines))


""" 14. Write a program to check if the given string is Palindrome or not without using reversed method. """

# Method1: by using slicing

# def is_palindrome(any_string):
#     res = any_string[::-1]
#     if res == any_string:
#         return f'{any_string} is palindrome'
#     return f'{any_string} is not palindrome'
#
#
# print(is_palindrome("radar"))           # radar is palindrome
# print(is_palindrome("india"))           # india is not palindrome

""" 15 Write a program to search for a character in a given string and return the corresponding index. """
# Method 1: normal method

# string_ = input("Enter your string: ")
# find_char = input("Enter your character that you find: ")
#
# for index, char in enumerate(string_):
#     if char == find_char:
#         print(f'Indexing position of {char} is {index}')

# Method 2: by using function


# def search_char(string, find_string):
#     for index, char in enumerate(string):
#         if char == find_string:
#             print(f'Indexing position of {char} is {index}')
#
#
# search_char("La ca sa da Papel", "P")           # Indexing position of P is 12
# search_char("the vampire diary", " ")
# Indexing position of   is 3
# Indexing position of   is 11

""" 16 Write a program to get the below output """
# sentence = "hello world welcome to python programming hi there"
# result: d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# from collections import defaultdict
# dd = defaultdict(list)
# l = sentence.split()
# for word in l:
#     dd[word[0]] += [word]
# print(dd)


""" 17 Write a program to replace all the characters with - if the character occurs more than once in a string """
# s = "google"
# res = ""
# for char in s:
#     if s.count(char) > 1:
#         res += "-"
#     else:
#         res += char
#
# print(res)


""" 18 write a decorator that returns only positive values of subtraction """

# def positive_values(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
#
# @positive_values
# def sub(a, b):
#     return a - b
#
#
# print(sub(3, 7))
# print(sub(196, 1996))

""" 19 How to get the count of number of instances of a class that is being created. """

""" 20 Write a function which takes a list of strings and integers. If the item is a string it should print as is and 
if the item is integer or float it should reverse it. """
# list_ = ['apple', 'yahoo', '1234', 100, 123.76, '26.23']
#
#
# def func(items):
#     l = []
#     for item in items:
#         if isinstance(item, (int, float)):
#             l.append(str(item)[::-1])
#         else:
#             l.append(item)
#     return l
#
#
# print(func(list_))


""" 21 Write a class named Simple and it should have iteration capability. """

""" 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a """

""" 23 Write a python program to get the below output """

# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
#
# # Method 1:
# l = sentence.split()
# for word in l:
#     print(word[::-1], end=" ")


""" 24 Write a python program to get the below output """
# sentence = "Hi How are you"
# o/p should be "uoy era woH iH"

# Method 1: by using reversed function
# l = sentence.split()
# for word in reversed(l):
#     print(word[::-1], end=" ")


# Method 2: by using range:


""" 25 Write a lambda function to add two numbers (a, b) """
# res = lambda a, b: a + b
# print(res(2, 7))
# print(res(2+5j, 10))


""" 26 What is the output of the following """
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])           # [[1, 2, 3], [4, 5, 6]]    i.e. list of list
# print((a, b))           # ([1, 2, 3], [4, 5, 6])    i.e Tuple of lists
# print([*a, *b])         # [1, 2, 3, 4, 5, 6]        i.e. Concatenate it or merge into single list


""" 27 How to remove duplicates from the list without using inbuilt functions """

# Method 1:
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# l = []
# for item in items:
#     if item not in l:
#         l.append(item)
# print(l)


# Method 2:
# print(set(items))           # {1, 2, 3, 4, 5} but we get the output in set collection => to avoid this => type cast
# print(list(set(items)))  # [1, 2, 3, 4, 5]

""" 28 Find the longest word in the sentence """
# sentence = "Hello world. Welcome to Python"
# l = sentence.split()
#
# # by using sorted function
# res = sorted(l, key=len)
# print(res[-1])                                              # Welcome
#
# # dictionary
# d = {word: len(word) for word in l}
# print(max(d.items(), key=lambda item: item[-1]))            # ('Welcome', 7)


""" 29 write a program to reverse the values in the dictionary if the value is of type String """
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# dictionary = {key: value[::-1] for key, value in d.items() if isinstance(value, str)}
# print(dictionary)

""" 30 write a program to get 1234 """
t = ('1', '2', '3', '4')
# by using join function
res = "".join(t)
print(res)
print(type(res))
rest = int(res)
print(rest)
print(type(rest))

# by using for loop
# output = ""
# for i in t:
#     output += i
# print(output)

""" 31 How to get the elements that are in list b but not in list a """
# a = [1, 2, 3]
# b = [1, 2, 3, 4]

# Method 1:
# for element in b:
#     if element not in a:
#         print(element, end="")            # 4

# Method 2:
# a1 = set(a)
# b1 = set(b)
# print(b1.difference(a1))                  # {4}


""" 32 A function takes variable number of positional arguments as input. How to check if the arguments that are 
passed are more than 5 """

# def count_arguments(*args):
#     if len(args) > 5:
#         print("Length of positional arguments are more than 5")
#     else:
#         print("Length of positional arguments are less than 5")
#
#
# count_arguments(1, 2)                       # Length of positional arguments are less than 5
# count_arguments(9, 8, 5, 26, 11, 31)        # Length of positional arguments are more than 5


""" 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file. """  # ****************
lines = """
CRITICAL: Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL: Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""

# from collections import defaultdict
# res = defaultdict(int)
# for line in lines.split('\n'):
#     if line.strip():
#         l = line.split(":")
#         res[l[0]] += 1
#
# print(res)

""" 34 Write a function to reverse any iterable without using reverse function. """
# a_ = [1, 2, 3, 4, 5]

# Method 1: by using range


# def reverse_(a):
#     l = []
#     for index in range(len(a)-1, -1, -1):
#         l.append(a[index])
#     print(l)
#
#
# reverse_(a_)


""" 35 Write a function to print the below output. """
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX


# def func(string_, initial):
#     if initial:
#         return string_[::2]
#     return string_[1::2]
#
#
# print(func("TRACXN", 0))            # RCN
# print(func("TRACXN", 1))            # TAX


""" 36 Sum all the numbers in the below string. """
# s = "Sony12India567Pvt2ltd"        # 1+2+5+6+7+2
# sum_ = 0
# for char in s:
#     if char.isdigit():
#         sum_ += int(char)
#
#
# print(sum_)

""" 37 Write a program to sum all the numbers in below string. """
# *********************************************
# s = "Sony12India567Pvt2ltd"        # 12+567+2
# import re
# rr = re.findall(r'[\d]+', s)                # ['12', '567', '2']
# print(rr)
# total = 0
# for num in rr:
#     total += int(num)
#
# print(total)

""" 38 Print all the numbers in the below list """
# a = ['abc', '123', 'hello', '23']
# for element in a:
#     if element.isdigit():
#         print(element, end=" ")


""" 39 Program to print the number of occurrences of characters in a String without using inbuilt functions. """
# s = 'helloworld'

# Method 1: by using dictionary comprehension
# d = {char: s.count(char) for char in s}
# print(d)                        # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Method 2: by using defaultdict
# from collections import defaultdict
# dd = defaultdict(int)
# for char in s:
#     dd[char] += s.count(char)
#
# print(dd)                       # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 9, 'o': 4, 'w': 1, 'r': 1, 'd': 1})


""" 40 Program to print only the repeated characters and count of the same. """
# s = 'helloworld'
# # Method 1: by using dictionary comprehension
# d = {char: s.count(char) for char in s if s.count(char) > 1}
# print(d)                            # {'l': 3, 'o': 2}
#
# # Method 2: by using defaultdict
# from collections import defaultdict
# dd = defaultdict(int)
# for char in s:
#     if s.count(char) > 1:
#         dd[char] = s.count(char)
#
# print(dd)                           # defaultdict(<class 'int'>, {'l': 3, 'o': 2})


""" 41 Write a program to get alternate characters of a string in list format. """
# s = 'hello world welcome to python'
# l = [s[index] for index in range(0, len(s), 2)]
# print(l)


""" 42 Write a program to get square of list of number's using lambda function . """
# a = [1, 2, 3, 4, 5]
# square = lambda num: num ** 2
# l = [square(element) for element in a]
# print(l)


""" 43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other. """

# def anagram(string1, string2):
#     if sorted(string1) == sorted(string2):
#         return f'Given string is Anagram.'
#     return f'Given string is Not Anagram.'
#
#
# print(anagram("heart", 'earth'))                # Given string is Anagram.
# print(anagram("way", 'away'))                   # Given string is Not Anagram.


""" 44 Write a program to iterate through list and build a new list, only if the items of the list has even number of 
characters."""
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# res = [item for item in names if len(item) % 2 == 0]
# print(res)


""" 45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even 
number of characters. """

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d_ = {element: len(element) for element in names if len(element) % 2 == 0}
# print(d_)


""" 46 Write a program which squares the numbers in a list using map object """
# a = [1, 2, 3, 4, 5]
# square = map(lambda num: num**2, a)
# print(list(square))           # [1, 4, 9, 16, 25]


""" 47 Count number of lines in a file without loading the file to the memory """
# path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\file1.txt'
#
# with open(path) as file:
#     count_ = 0
#     for _ in file:
#         count_ += 1
# print(f'Total number of lines are: {count_}')


""" 48 Printing line and line no's """

# with open(path) as file:
#     for line_number, line in enumerate(list(file), start=1):
#         print(line_number, line)


""" 49 Write a Program to print the sum of entire list and sum of only internal list """
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Method 1:
# entire_sum = 0
# for element in l:
#     internal_sum = 0
#     for num in element:
#         internal_sum += num
#         entire_sum += num
#     print(f'Sum of internal list: {internal_sum}')
# print()
# print(f'Sum of entire list: {entire_sum}')

# Method 2:
# internal_sum = [sum(element) for element in l]
# print(f'Sum of internal list: {internal_sum}')                          # Sum of internal list: [6, 15, 24]
#
# print(f'Sum of Entire list: {sum(internal_sum)}')                       # 45

""" 50 Write a program to reverse the list as below """
# words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']

# Method 1: by using list comprehension (reversed() function)

# result = [element[::-1] for element in reversed(words)]
# print(result)

# Method 2: by using list comprehension(slicing)

# result = [element[::-1] for element in words[::-1]]
# print(result)

""" 51 Write a program to update the tuple """
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
#
# # Method 1:
# output = (*t1, *t2)
# print(output)
#
# # Method 2:
# result = t1 + t2
# print(result)

""" 52 Write a program to replace value present in nested dictionary. """
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
# # Method 1
# for key, value in d.items():
#     if isinstance(value, dict):
#             d[key]['n'] = "net"
# print(d)


""" 53 Write a program to count the number of white spaces in a file. """
# path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\file1.txt'

# Method 1
# count_space = 0
# with open(path) as file:
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count_space += 1
# print(count_space)
#
# # Method 2:
# import re
# white_spaces = 0
# with open('data/sample.txt') as f:
#     for line in f:
#         match = re.findall(r'\s', line)
#         if match:
#             white_spaces += len(match)
# print(white_spaces)


""" 54 Grouping anagrams. """
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# from collections import defaultdict
# dd = defaultdict(list)
# for word in words:
#     # s = "".join(sorted(word))
#     print(s, end=" ")
#     dd[s].append(word)
#
# print(dd)

""" 55 What is the difference between defaultdict and normal dictionary. """

"""
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
"""

""" 56 Explain property decorator in python. """

""" 57 What is Mutable and Immutable datatypes. """
"""
1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
"""

""" 58 Explain get() method in dictionaries. """

"""
point =  {'a': 1, 'b': 2}
1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
           e.g. profile.get('c', 'Sorry the key does not exist')
"""

""" 59 Write a list comprehension to get a list of even numbers from 1-50 """
# even_num = [num for num in range(1, 51) if num % 2 == 0]
# print(even_num)


""" 60 Find the longest non-repeated substring in the below string """
# s = "This is a Programming language and Programming is fun"
# l = s.split()
#
# # Method 1: by using list comprehension
# list_ = [word for word in l if l.count(word) == 1]
# arrange = sorted(list_, key=len)
# print(arrange[-1])                      # language
#
# # Method 2: by using dictionary comprehension
# dictionary_ = {word: len(word) for word in l if l.count(word) == 1}
# arrange = sorted(dictionary_.items(), key=lambda item: item[-1])
# print(arrange[-1])                      # ('language', 8)


""" 61 Write a program to find the duplicate elements in the list without using inbuilt functions """
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# for item in set(names):
#     count_ = 0
#     for word in names:
#         if word == item:
#             count_ += 1
#             if count_ > 1:
#                 print(item, end=" ")


""" 62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions """
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
#
# from collections import defaultdict
# occurrence_ = defaultdict(int)
# for element in names:
#     occurrence_[element] += 1
# print(occurrence_)
#
#
# # Method 2:
# # Get the unique elements present in the list
# unique_items = set(names)
#
# # declare an empty dictionary
# d = {}
#
# for item in unique_items:
#     _count = 0
#     for name in names:
#         if item == name:
#             _count += 1
#     d[item] = _count
#
# print(d)

""" 63 Write a function to check if the number is Prime """

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(f'{num} is not prime number')
#                 break
#             return f'{num} is prime number'
#
#
# print(is_prime(111))             # 111 is prime number
# print(is_prime(97))              # 97 is prime number


""" 64 How to create a tuple using range function """
# res = tuple(range(11))
# print(res)              # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

""" 65 Write a program to find the largest number in the list without using any inbuilt functions """
# numbers = [10, 20, 30, 40, 50]
# largest_number = 0
# for num in numbers:
#     if num > largest_number:
#         largest_number = num
#
#
# print(largest_number)

""" 66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) 
should return 2."""

# def last_digit(num):
#     s = str(num)
#     return int(s[-1])
#
#
# print(last_digit(198766542))


""" 67 Write a program to find most common words in a given list. """
# words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
# 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the','eyes', 'look', 'into', 'my', 'eyes', "you're",
# 'under']

# # Method 1:
# d = {word: words.count(word) for word in words}
# sorted_d = sorted(d.items(), key=lambda item: item[-1])
# print(sorted_d[-1])
#
# # Method 2: using Counter
# from collections import Counter
# res = Counter(words)
# print(res.most_common(1))


""" 68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns 
the last n elements from the given sequence, as a list."""

# def tail(sequence, n):
#     return sequence[-n:]
#
#
# print(tail("Women", 3))                                             # men
# print(tail(["M.P.", "U.P.", "Delhi", "Goa"], 2))                    # ['Delhi', 'Goa']
# print(tail(("Mango", "banana", "apple", "Grapes", "Papaya"), 2))    # ('Grapes', 'Papaya')


""" 69 Write a function named is_perfect_square that accepts a number and returns True if it's a perfect square and 
False if it's not. """

# Method 1: using import math
# from math import sqrt
#
#
# def is_perfect_square(num):
#     return num == sqrt(num) ** 2
#
#
# print(is_perfect_square(5))         # False
# print(is_perfect_square(36))        # True


# Method 2:


# def is_perfect_square(num):
#     sq = int(num ** 0.5)
#     if sq * sq == num:
#         return True
#     return False
#
#
# print(is_perfect_square(9))             # True
# print(is_perfect_square(10))            # False


# # Method 3: using range   ????????????????????????????????????????????????????? not working check
#
#
# def is_perfect_square(num):
#     for i in range(num):
#         if i ** 2 == num:
#             return True
#         return False
#
#
# print(is_perfect_square(9))
# print(is_perfect_square(121))


""" 70 Write a program to get all the duplicate items and the number of times the item is repeated in the list. """
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

# Method 1: using comprehension
# d = {element: names.count(element) for element in names if names.count(element) > 1}
# print(d)

""" 71 Write a program to count the number of occurrences of each word in a file. """

""" 72 Write a program to count the number of occurrences of vowels in a file. """

""" 73 Write a program to print all numeric values in a list """
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# res = [item for item in items if isinstance(item, (int, float, complex))]
# print(res)

""" 74 Triangle Patterns """

# Left Justified Triangle
# for i in range(1, 6):
#     print(f"{'* '*i:<5}")

"""
*         
* *       
* * *     
* * * *   
* * * * * 
"""

# Right Justified Triangle
# for i in range(1, 6):
#     print(f"{' *'*i:>10}")

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# Equilateral Triangle
# for i in range(1, 6):
#     print(f"{'* ' * i : ^10}")

"""
    *     
   * *    
  * * *   
 * * * *  
* * * * * 
"""

# for i in range(1, 6):
#     print(f"{' *' * i : ^10}")

"""
*    
    * *   
   * * *  
  * * * * 
 * * * * *
"""

# Inverted Triangles (Left Justified)
# for i in range(6, 0, -1):
#     print(f"{'* ' * i: <6}")
"""
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*   
"""

# Inverted Triangles (Right Justified)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:>12}")
"""
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
"""

# Inverted Triangles (Centre)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:^12}")

"""
 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 
"""

# ------------------------------------------------------------------------------------------------------------------

# Number Pattern in triangle (Left Justified)

# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:<5}')

"""
1    
1 2  
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

# Number Pattern in triangle (Right Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:>10}')

"""
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5

"""
# Number Pattern in triangle (Centre)
# pat = ''
# for i in range(1, 6):
#     pat = pat + ' ' + str(i)
#     print(f'{pat:^10}')

"""
     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5

"""
# ------------------------------------------------------------------------------------------------------------------
# Alphabet Pattern

# Left justification
# pat = ""
# for i in range(ord("a"), ord('d') + 1):
#     pat += chr(i) + " "
#     print(pat)

"""
a 
a b 
a b c 
a b c d 
"""

# Right Justification
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:>8}')

"""
      a 
    a b 
  a b c 
a b c d  
"""

# Central
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:^8}')

"""
   a    
  a b   
 a b c  
a b c d 
"""

""" 75 Write a program count the occurrence of a particular word in the file """

""" 76 Write a program to map a product to a company and build a dictionary with company and list of products pair """

""" 77 Write a program to rotate items of the list """
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# n = int(input("Number of rotation: "))
#
# # Method 1:
# i = 1
# while i <= n:
#     *a, b = names
#     names = [b, *a]
#     i += 1
#
# print(names)


# Method 2:
# for item in range(n):
#     remove_item = names.pop()
#     add_remove_item = names.insert(0, remove_item)
#
# print(names)


""" 78 Write a program to rotate characters in a string """
# string = "helloworld"
# n = int(input("Enter your number of rotations: "))

# Method 1: using while loop
# i = 1
# res = ""
# while i <= n:
#     last_char = string[-1]
#     res = last_char + string[:len(string)-1]
#     string = res
#     i += 1
#
# print(res)


# Method 2:


# def rotate_string(string_, n):
#     string_ = list(string_)
#     for _ in range(n):
#         last_item = string_.pop()
#         string_.insert(0, last_item)
#     return ''.join(string_)
#
#
# print(rotate_string("helloworld", 2))               # ldhellowor
# print(rotate_string("karnataka", 4))                # takakarna


""" 79 Write a program to count the number of white spaces in a given string """
# sentence = """Hello world welcome to Python Hi  How are you. Hi how are you"""
#
# # Method 1 using for loop
# count = 0
# for char in sentence:
#     if char == " ":
#         count += 1
#
# print(f'Total number of white spaces are: {count}')
#
#
# # Method 2: using built-in-function
# count_white_space = sentence.count(" ")
# print(f'Total number of white spaces are: {count_white_space}')

# Method 3: using Regular Expression
# import re
# spaces = re.findall(r'\s', sentence)        # \s  =>  Matches only whitespace
# print(f'Total number of white spaces are: {len(spaces)}')


""" 80 Write a program to print only non-repeated characters in a string """
# s = 'helloworld'
#
# # Method 1: using comprehension
# non_repeated_char = [char for char in s if s.count(char) == 1]
# print(non_repeated_char)


""" 81 What is the difference between a list and a tuple """

"""
1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation. 
Where as in tuples, memory is not over allocated, as tuples does not support append operation. 
(Since tuples are immutable, it does not support append operation). 
3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
4. Tuples are negligibly faster than lists. 
"""

""" 82 Write a program to print all the consonants in a given string """
# s = 'helloworld'
# for char in s:
#     if char.isalpha() and char not in "aeiouAEIOU":
#         print(char, end=" ")


""" 83 Write a program to count the number of commented lines in a text file """
# with open(path) as file:
#     count_commented_line = 0
#     for line in file:
#         if line.strip():
#             if line.startswith("#"):
#                 count_commented_line += 1
#
# print(f'Total number of commented lines are: {count_commented_line}')


""" 84 Write a program to check if the year is leap year or not """  # ****************************************
# import calendar
# print(calendar.isleap(2012))            # True
# print(calendar.isleap(1816))            # True
# print(calendar.isleap(2022))            # False

""" 85 Liner Search """

""" 86 Difference between xrange and range """
"""
python2- xrange
python3- range

1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
  Python-3
  r = range(0, 10)
  r.start
  r.stop
  r.step

  r = xrange(0, 10)
  In Python-2 The above attributes are not supported.

2. range Object supports slicing! But xrange does not support slicing

3. range object has __contains__ method implemented. So it supports membership testing. 
   But xrange does not implement __contains__ method. 
   So Python will iterate over each and every item in the range xrange object until it finds a match. 
   (So if you are searching for a number in range is faster than xrange)

4. range will accept integer of any size. But xrange objects accepts integer size equivalent to C long!
"""

""" 87 Write a program to count no of capital letters in a string """
# sentence = "Hi How are You WelCome to PytHon"

# Method 1: using buil-in-method
# count_uppercase = 0
# for char in sentence:
#     if char.isupper():
#         count_uppercase += 1
#
#
# print(f'Total number of Capital letters are: {count_uppercase}')

# Method 2: without using built-in-method
# count_uppercase = 0
# for char in sentence:
#     if 65 <= ord(char) <= 90:
#         count_uppercase += 1
#
# print(f'Total number of Capital letters are: {count_uppercase}')


""" 88 Write a program to get the below output """
"""
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 
"""

# for i in range(1, 5):
#     print("* " * 1)
#     print("* " * (i+1))

""" 89 Write a program to get the below output """
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
[1, 2]
[3, 4]
[5, 6]
[7, 8]
[9]
"""

# for item in range(0, len(a), 2):
#     print(a[item: item+2])


""" 90 Write a program to check if the elements in the second list is series of continuation of the items in the 
first list """

# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# s = [0, 5, 10, 15]
# p = [20, 25, 30, 35, 40]
#
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]


""" 91 What is the difference between append() and extend() method in list """

"""
1. append() method appends one item at the end of the list.
2. extend() method appends all the items of the iterable to the end of the list.
3. Both append() and extend() method's mutates the existing list.

e.g. 
>>> a = [1, 2, 3]
>>> b = (4, 5, 6)
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]

>>> c = {7, 8, 9}
>>> a.extend(c)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7]

>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> a.extend(d)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7, 'a', 'b', 'c']

The list "a" is getting mutated each time when it is extended.
"""

""" 92 Write a program to find the first repeating character in a string """
# s = 'helloworld'
# for char in s:
#     if s.count(char) > 1:
#         print(f'first repeated character is: {char}')
#         break

""" 93 Write a program to find the index of nth occurrence of a sub-string in a string """  # ???????????????????
# sentence = "hello world welcome to python hello hi how are you hello there"


# def index_position(char):
#     return sentence.rindex(char)
#
#
# print(index_position("r"))
# print(len(sentence))


# Method 2:
"""import re

>>> def index_nth_occurance(sentence, pat, n):
      matches = re.finditer(pat, sentence)
      _count = 0
      for match in matches:
         _count +=1
         if _count == n:
            return f"Start Index: {match.start()}, End Index: {match.end()}"

>>> index_nth_occurance(sentence, 'hello', 3)
>>> Start Index: 51, End Index: 56
>>> index_nth_occurance(sentence, 'hello', 2)
>>> Start Index: 30, End Index: 35
>>> index_nth_occurance(sentence, 'hello', 2)
>>> Start Index: 0, End Index: 5"""

""" 94 Write a program to print prime numbers from 1 to 50 """
# prime_numbers = []
# for num in range(1, 51):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             prime_numbers.append(num)
#
# print(prime_numbers)


""" 95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd 
numbers first and then even numbers in sorted order"""
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# # o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]
#
# odd_numbers = [num for num in a if num % 2 != 0]
# even_numbers = [num for num in a if num % 2 == 0]
#
# odd_numbers.sort()
# even_numbers.sort()
#
# print([*odd_numbers, *even_numbers])
# print(odd_numbers + even_numbers)


""" 96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers 
should be in ascending order and even numbers should be in descending order"""
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
#
# odd_numbers = [num for num in a if num % 2 != 0]
# even_numbers = [num for num in a if num % 2 == 0]
#
# odd_numbers.sort()
# even_numbers.sort(reverse=True)
#
# print([*odd_numbers, *even_numbers])  # or
# print(odd_numbers + even_numbers)


""" 97 Write a program to count the number of occurrences of non-special characters in a given string """
# string = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

# # Method 1: 2nd preferable
# non_special_chr = ""
# for char in string:
#     if char.isalnum():              # char.isdigit() or char.isalpha()
#         non_special_chr += char
#
# from collections import defaultdict
# res = defaultdict(int)
# for char in set(non_special_chr):
#     res[char] += non_special_chr.count(char)
#
# print(res)

# Method 2: first preferable
# from collections import defaultdict
# d = defaultdict(int)
# for char in string:
#     if char.isalnum():
#         d[char] += 1
#
# print(d)

# Method 3: using Regular_Expression (1st preferable)
# import re
# characters = re.findall(r'\w', string)                      # \w  =>  word character. Same as [a-zA-Z0-9].
# res = {char: characters.count(char) for char in characters}
# print(res)


""" 98 Grouping Flowers and Animals in the below list """
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# from collections import defaultdict
# grouping = defaultdict(list)
# for item in items:
#     l = item.split("-")
#     grouping[l[-1]] += [l[0]]
#
# print(grouping)


""" 99 Grouping files with same extensions """
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# from collections import defaultdict
# res = defaultdict(list)
# for element in files:
#     l = element.split(".")
#     res[l[-1]] += [l[0]]
#
# print(res)


""" 100 Filter only those characters except digits """
# s = '@hello12world34welcome!123'
#
# # Method 1:
# res = ""
# for char in s:
#     if not char.isdigit():
#         res += char
#
# print(res)
#
# # Method 2: using Regular Expression
# import re
# l = re.findall(r'\D', s) #['@', 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'w', 'e', 'l', 'c', 'o', 'm', 'e', '!']
# res = "".join(l)
# print(res)                  # @helloworldwelcome!


""" 101 Count number of words in a sentence. ignore special characters. """
# sentence = "Hi there! How are you:) How are you doing today!"
# l = sentence.split()
# print(f'Total number of words are: {len(l)}')

# Method 2: using Regular_Expression
import re

# l = re.findall(r'\b\w+', sentence.lower())
# print(f'Total number of words are: {len(l)}')


# count the no. of occurrence
# Method 1:
# from collections import Counter
# c = Counter(l)
# print(c)

# Method 2:
# l = sentence.split()
# d = {item: l.count(item) for item in l}
# print(d)                # {'Hi': 1, 'there!': 1, 'How': 2, 'are': 2, 'you:)': 1, 'you': 1, 'doing': 1, 'today!': 1}

# above method is not work properly so
# l1 = re.findall(r'\b\w+', sentence.lower())
# d1 = {item: l1.count(item) for item in l1}
# print(d1)


""" 102 Grouping even and odd numbers """
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
# from collections import defaultdict
# res = defaultdict(list)
# for num in numbers:
#     if num % 2 == 0:
#         res[0] += [num]     # res[0].append(num)
#     else:
#         res[1] += [num]     # res[1].append(num)
#
# print(res)


""" 103 Find all max numbers from the below list """
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# # Output should be [4, 4, 4]
# max_ = max(numbers)
# all_max_num = [num for num in numbers if num == max_]
# print(all_max_num)


""" 104 Find all max length words from the below sentence """
# sentence = "hello world hi apple you yahoo to you"
# # Output should be ['hello', 'world', 'apple', 'yahoo']
# res = sorted(sentence.split(), key=len)
# max_ = len(res[-1])
# max_length = [item for item in res if len(item) == max_]
# print(max_length)


""" 105 Find the range from the following string """  # ************************************************************
# sentence = '0-0, 4-8, 20-20, 43-45'
# # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
# l = sentence.split(",")
# res = []
# for ranges in l:
#     start, end = ranges.split("-")
#     for num in range(int(start), int(end)+1):
#         res.append(num)
#
# print(res)


""" 106 Can we override a static method in python? """

# class Parent:
#     @staticmethod
#     def demo():
#         print("Running Parent's demo method")
#
#
# class Child:
#     @staticmethod
#     def demo():
#         print("Running Child's demo method")
#
#
# c = Child()
# c.demo()
# Running Child's demo method
# Yes, we can override a static method in Python


""" 107 Write a function which returns the sum of lengths of all the iterables """

# def sum_of_length(*iterables):
#     print(iterables)
#     total = 0
#     for iterable in iterables:
#         total += len(iterable)
#     print(f'Total length of the iterables are: {total}')
#
#
# sum_of_length([1, 2, 3])                                                            # 3
# sum_of_length([1, 2, 3], [9, 10])                                                   # 5
# sum_of_length(["hai", 2, "Hello"], (20, 30), {"Python", "VS"})                      # 7
# sum_of_length((1, 2, 3), (2, 3, 5, 8), {"a": "apple", "b": 2, "c": "Camel"})        # 10
# sum_of_length({1, "rainbow", 3}, (20, 30, 89), {"a": "apple", "b": 2, "c": "Camel"}, [2.5, 5+6j, "True", False]) # 13


""" 108 Replace whitespaces with newline character in the below string """
# sentence = "Hello world welcome to python"

# Method 1:
# res = sentence.replace(" ", "\n")
# print(res)

# Method 2: use Regular Expression
import re

# res = re.sub(r'\s', '\n', sentence)         # \s => matches only whitespace, \n => next line
# print(res)
# Hello
# world
# welcome
# to
# python

# Method 3: using for loop
# l = sentence.split()
# for item in l:
#     print(item)


""" 109 Replace all vowels with "*" """
# sentence = "hello world welcome to python"

# Method 1
# res = ""
# for char in sentence:
#     if char.lower() in "aeiou":
#         res += "*"
#     else:
#         res += char
#
# print(res)          # h*ll* w*rld w*lc*m* t* pyth*n

# Method 2:
# import re
# res = re.sub(r'[aeiouAEIOU]', '*', sentence)      # [abcd]=>any character which matches either 'a' or 'b' or 'c' or 'd'
# print(res)              # h*ll* w*rld w*lc*m* t* pyth*n


""" 110 Replace all occurrences of "Java" with "Python" in a file """

# import re
# with open('java.txt', 'r') as java_file:
#     with open('python.py', 'a') as python_file:
#         for line in java_file:
#             new_line = re.sub("Java", "Python", line)
#             python_file.write(new_line)


""" 111 Maximum sum of 3 numbers and Minimum sum of 3 numbers"""
# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]

# Method 1: using sorted built-in-function
# sorted_list = sorted(numbers)
#
# sum_max_3 = sum(numbers[-3:])
# sum_min_3 = sum(numbers[:3])
#
# print(f'Sum of maximum 3 numbers are: {sum_max_3}')
# print(f'Sum of minimum 3 numbers are: {sum_min_3}')


""" 112 Write a program to get the output as below """
# input = "python@#$%pool"
# # o/p should be ['PYTHON', 'POOL']
# import re
# words = re.findall(r'\w+', input)       # \w =>word character. Same as [a-zA-Z0-9].Matches alphanumeric and underscore
# res = [word.upper() for word in words]
# print(res)                              # ['PYTHON', 'POOL']


""" 113 Write a program to print all the number which are ending with 5 """
# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
#
# # Method 1: using comprehension
# res = [num for num in numbers if num[-1] == '5']
# print(res)
#
# # Method 2: using Regular expression
# import re
# for num in numbers:
#     match = re.findall("5$", num)
#     if match:
#         print(num, end=" ")


""" 114 Write a program to get the indexes of each item in the below list """
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# # output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
#
#
# from collections import defaultdict
# res = defaultdict(list)
# for index, item in enumerate(names):
#     res[item] += [index]
# print(res)


""" 115 Write a program to print "Bangalore" 10 times without using "for" loop """
# Method 1:
# print("bangalore\n" * 10)


""" 116 Write a program to print all the words which starts with letter 'h' in the given string """
# string = 'hello world hi hello universe how are you happy birthday'
# # l1= string.split()
#
# # Method 1:
# l = [word for word in string.split() if word[0] in "hH"]
# print(l)
#
# # Method 2: using regular expression  *****************************************************************************
# import re
# matches = re.findall(r'\bh\w+', 'hello world hi hello universe how are you happy birthday')
# print(matches)


""" 117 Write a program to sum all even numbers in the given string """
# sentence = 'hello 123 world 567 welcome to 9724 python'
#
# # Method 1:
# sum_ = 0
# for char in sentence:
#     if char.isdigit() and int(char) % 2 == 0:
#         sum_ += int(char)
#
# print(sum_)

# Method 2: using regular expression  ***************************************************************************
# import re
# numbers = re.findall()


""" 118 Write a program to add each number in word1 to number in word2 """
# e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9
# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
#
# # Method 1: using regular expression method
# import re
# number1 = re.findall(r'\d', word1)
# number2 = re.findall(r'\d', word2)
# add = []
# for num1, num2 in zip(number1, number2):
#     add.append(int(num1) + int(num2))
#
# print(add)

# Method 2: using comprehension
# number1 = [num for num in word1.split() if num.isdigit()]
# number2 = [num for num in word2.split() if num.isnumeric()]
#
# res = []
# for num1, num2 in zip(number1, number2):
#     res.append(int(num1) + int(num2))
#
#
# print(res)


""" 119 Write a program to filter out even and odd numbers in the given string """
# sentence = 'hello 123 world 456 welcome to python498675634'

# even_ = [char for char in sentence if char.isdigit() and int(char) % 2 == 0]
# odd_ = [char for char in sentence if char.isnumeric() and int(char)%2 != 0]
#
# print(f'Even numbers are: {even_} \n Odd numbers are: {odd_}')


# Method 2: using Regular_expression *******************************************************************************
# import re
# numbers = re.findall(r'\d', sentence)   # ['1', '2', '3', '4', '5', '6', '4', '9', '8', '6', '7', '5', '6', '3', '4']
#
# even_ = [num for num in numbers if int(num) % 2 == 0]
# odd_ = [num for num in numbers if int(num) % 2 != 0]
# print(f'Even numbers are: {even_} \n Odd numbers are: {odd_}')


""" 120 Write a program to print all the number which are starting with 8 """
# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']

# Method 1: using regular expression ****************************************************************************
# import re
# for number in numbers:
#     matches = re.findall(r'^8', number)
#     if matches:
#         print(number, end=" ")

# Method 2: using com
# res = [num for num in numbers if num[0] == '8']
# print(res)


""" 121 Write a program to remove duplicates from the list without using set or empty list """  # *******************
# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1[::]          # or l2 = l1.copy()
# for item in l2:
#     if l1.count(item) > 1:
#         l1.remove(item)
#
# print(l1)


""" 122 Print all the missing numbers from 1 to 10 in the below list """
# numbers = [1, 3, 6, 8, 10]
# for num in range(1, 11):
#     if num not in numbers:
#         print(f'Missing Number is {num}')


""" 123 Write a python program to get the below output """
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# # o/p1 ['1a', '2b', '3c']
# # o/p2 ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
#
# # Output1:
# res = [str(i) + j for i, j in zip(l1, l2)]
# print(res)
#
# # Output2
# l = []
# for i in l1:
#     for j in l2:
#         l.append(str(i) + j)
# print(l)

# Method 2:
# res = [''.join((str(i), j)) for i in l1 for j in l2]
# print(res)

""" 124 Write a python program to get the below output """  # *****************************************
# word = "AAAAaaccYYY"
# o/p : ['Y3', 'c2', 'A4', 'a2']


""" 125 What is the output of the below function call """

# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")
#
#
# d = Demo()
# d.greet()


# => "hello universe"  because Method overloading

""" 126 In the list below, find all the number pairs which results in 10 either when added or subtracted """
# a = [3, 5, -4, 8, 11, 1, -1, 6]
# for num1 in a:
#     for num2 in a:
#         if num1 != num2:
#             if num1 + num2 == 10 or num1 - num2 == 10:
#                 print(num1, num2)


""" 127 Write a decorator to prefix +91 to the original phone numbers """
# numbers = [1234567890, 913456790, 9234567890, 911234567890]


# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         number_, = args
#         add_country_code = ["+91" + str(num) for num in number_]
#         return func(add_country_code)
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(p_numbers):
#     for number in p_numbers:
#         print(number)
#
#
# print_numbers(numbers)


# Method 2:

# numbers = [1234567890, 9876543210, 911234567890, 111234567890, 912345678]
#
#
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:]
#         return str_number
#     else:
#         return str_number
#
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(number) for number in temp]
#         return func(processed_numbers)
#
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(numbers):
#     for item in numbers:
#         print(item)
#
#
# print_numbers(numbers)

""" 128 Write a program to get the below output """
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# o/p should be ['b', 'd']
# # Method 1:
# l = [key for key, value in d.items() if value % 2 == 0]
# print(l)                    # ['b', 'd']
#
# # Method 2:
# keys = list(d.keys())
# l1 = [key for key in keys[1::2]]
# print(l1)


""" 129 Can we have multiple init methods in a class """

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c


# p = Point(1, 2)                 # TypeError: __init__() missing 1 required positional argument: 'c'
# print(p.a)
# print(p.b)
# Since python is dynamically typed language, it takes the latest __init__ method

# p1 = Point(10, 20, 30)
# print(p1.a)
# print(p1.b)
# print(p1.c)

# Multiple constructor is possible in a single class
# if we have multiple constructor (__init__) in a class then it will considered latest one.
# by default constructor will return None

# Multiple constructor is not possible in Python => to solve this problem by using default value => i.e.
# constructor overloading

# ___________ Constructor overloading / Overloaded constructor______________________


# class Point:
#     def __init__(self, a=0, b=0, c=0, d=0):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#
# p1 = Point()
# p2 = Point(1)
# p3 = Point(10, 20)
# p4 = Point(1, 12, 13)
# p5 = Point(100, 220, 30, 40)
#
# print(p1.a)
# print(p2.a)
# print(p3.a)
# print(p4.a)
# print(p5.a)
