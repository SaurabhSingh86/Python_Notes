# import os
# print(os.getcwd())
#
path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\file1'
#
# print(os.getcwd())

""" WAP to read all the lines in a file without loading the file into memory"""

# with open(path) as file:
#     for line in file:
        # print(line)


""" WAP to count the number of lines present in the file """

# with open(path) as file:
#     count = 0
#     for _ in file:
#         count += 1
#     print(count)


""" WAP to print line number & line in the file """

# Method 1:
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)

# Method 2: by using enumerate()
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)

""" WAP to count the number of words in a given file """

# Method 1:

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             count += 1
#     print(count)                                  # 34

# Method 2:

# with open(path) as file:
#     count = 0
#     for line in file:
#         l = line.split()
#         count += len(l)
#     print(count)

""" WAP to print the lines from the last line"""

# Method 1: using concatenate               ##############last two lines not working properly
# with open(path) as file:
#     res = ""
#     for line in file:
#         res = line + res
#     print(res)

# print()

# with open (path) as file:
#     for line in reversed(list(file)):
#         print(line)

""" WAP to count the number of spaces in the given file """

# Method 1: without using buil-in-method
# with open(path) as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":             ## don't use char.isspace() because it count next line as a single space
#                 count += 1
#     print(count)                          # 27

# Method 2: by using buil-in-method
# with open(path) as file:
#     count = 0
#     for line in file:
#         space = line.count(" ")
#         count += space
#     print(count)


""" WAP to count the number of words that is starting with vowels """

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#
#     print(count)                              # 7


""" WAP to create a dictionary of word & its count pair in the given file """

# Method 1: by using if-else statement
# with open(path) as file:
#     d = {}
#     for line in file:
#         # l = line.split()
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)
# {'hello': 8, 'world': 6, 'universe': 2, 'welcome': 2, 'to': 2, 'python': 5, 'programming': 1, 'in': 1, 'is': 3, 'fun': 2, 'java': 1, 'easy': 1}


# Method 2: by using defaultdict()
# from collections import defaultdict

# with open(path) as file:
#     dd = defaultdict(int)
#     for line in file:
#         for word in line.split():
#             dd[word] += 1
#     print(dd)


# Method 3: by using count() function
from collections import defaultdict

# with open(path) as file:
#     dd = defaultdict(int)
#     for line in file:
#         l = line.split()
#         for word in set(l):                 ########## to avoid duplicates from the l
#             dd[word] += l.count(word)
#     print(dd)


""" WAP to extract all the ip address from acces_log.txt file """

path1 = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\File_directory\access-log.txt'

# Method 1:
# with open(path1) as file:
#     for line in file:
#         l = line.split()
#         for word in l:
#             print(l[0])

# Method 2:
# with open(path1) as file:
#     l = []
#     for line in file:
#         list_ = line.split()
#         l.append(list_[0])
#     print(l)

""" WAP to create a dictionary of ip address & their count """


