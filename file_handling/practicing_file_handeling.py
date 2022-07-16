# <<<~~~~~~~~~~~~~~~~~~~~~~~~~~~  OS Module  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>

# Methods related to directory:
# 1. getcwd()           :   get current working directory
# 2. mkdir(dir_name)    :   creating a new directory
# 3. chdir(dir_name)    :   changing the directory
# 4. rmdir(dir_name)    :   removing directory
# 5. listdir()          :   used to.


# Methods related to files:

# 1. popen(file_name, mode)     :
# 2. rename(old_name, new_name) :
# 3. remove()                   :

# Path related methods:

# os.path.exists()
# os.path.getsize()

# Files:
# File operation takes place in the following order:
# 1. open a file
# 2. Read & write (perform operation)
# 3. Close the file

# ----------------------------------------------------------------------------------------------------------------------
# ~~~~~~~~~~>>>>>>> Opening files in Python

# in Python, files can be opened in two ways-
# 1. without context manager    =>  file_obj = open(file_name, mode)
# 2. with context manager       =>  with open(file_name, mode) as file_obj:
#                                           pass
# Note:


# Modes:
# 1. r => read      =>
# 2. a => append    =>
# 3. w => write     =>
# 4. x => create    =>


# f = open("file1.txt", "r")
# print(f)
# print(f.closed)         # False
# print(f.close)
# print(f.closed)         # True


import os

# path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.txt'

# os.chdir(path)
# print(os.getcwd())

# with open(path, "r") as file:
#     print(file)                         # <_io.TextIOWrapper name='C:\\Users\\Saurabh\\PycharmProjects\\Python_Notes\\files_directory\\txt_log_files\\sample.txt' mode='r' encoding='cp1252'>
#     print(file.closed)                  # False
#     print(file.mode)                    # r
#     print(file.name)                    # C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.txt
#     print(file.readable())              # True
#     print(file.writeable())             # False

# Read from files


# function to perform read operations
# read()
# readline()
# readlines()

import os

path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.txt'

""" WAP to read all the lines in a file without loading the file into memory"""
# with open(path, "r") as file:
#     for line in file:
#         print(line)


""" count"""

# with open(path, "r") as file:
#     count = 0
#     for _ in file:
#         count += 1
#     print(count)


""" line no & line """

# Method 1:
# with open(path, "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)

# Method 2:
# with open(path, "r") as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)

""" count the no of words in a given file """

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             count += 1
#     print(count)


# with open(path) as file:
#     count = 0
#     for line in file:
#         count += len(line.split())
#     print(count)


""" print lines from the last """

# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

# with open(path, "r") as file:
#     res = ""
#     for line in file:
#         res = line + res
#     print(res)


""" coutn the no of space """

# with open(path) as file:
#     spaces = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 spaces += 1
#     print(spaces)

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += line.count(" ")
#     print(count)

""" Count no of words starting with vowels """

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#     print(count)


""" create a dictionary of word & its count pair in the given file """

# with open(path) as file:
#     d = {}
#     for line in file:
#         l = line.split()
#         for word in l:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)


# from collections import defaultdict
#
# with open(path, "r") as file:
#     dd = defaultdict(int)
#     for line in file:
#         l = line.split()
#         for word in l:
#             dd[word] += 1
#     print(dd)


import os

ip_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\access-log.txt'

# with open(ip_path) as file:
#     res = []
#     for line in file:
#         if line.strip():
#             l = line.split()
#             res.append(l[0])
    # print(res)


""" dictionary of ip address & its count pair """

# Method 1:
# from collections import defaultdict
# dd = defaultdict(int)
# for word in res:
#     dd[word] += 1
# print(dd)


# Method 2:
# from collections import Counter
# ip_ = Counter(res)
# print(ip_)
# print(ip_.most_common(1))

""" nth line """
# n = 5
# with open(ip_path, "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line_no, line)

# n = 5
# with open(ip_path) as file:
#     line_c = 0
#     for line in file:
#         line_c += 1
#         if line_c == n:
#             print(line_c, line)

# n= 4
# from itertools import islice
# with open(ip_path) as file:
#     res = list(islice(file, n-1, n))
#     print(res)

# with open(ip_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no <= n:
#             print(line_no, line)

""" WAP to print line from 5 to 10 """
# n1 = 5
# n2 = 8
# from itertools import islice
# with open(ip_path) as file:
#     res = list(islice(file, n1-1, n2))
#     print(res)

""" last n line """

# from collections import deque
# with open(ip_path) as file:
#     lines = list(deque(file, 5))
#     print(lines)




# import os
#
# ip_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\access-log.txt'
# c_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\File_Handeling\copy_the_content.py'
#
# with open (ip_path, "r") as r_file, open(c_path, "w") as w_file:
#     for line in r_file:
#         w_file.write(line)


# Assignment~~~~~~~~~~~~~~~~~>>>>>>>>>

d_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\data.txt'
s_log_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.log'


""" 1. finding the length of each line in the text file """
# with open(d_path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)


""" 2. extracting message from sample.log """
# with open(s_log_path) as file:
#     r_list = []
#     for line in file:
#         if line.strip():
#             l = line.split()
#             r_list.append(l[2])
#     print(r_list)


""" 3. Counting no of Info, Warn, Trace message """

# with open(s_log_path) as file:
#     l1 = []
#     for line in file:
#         if line.strip():
#             l = line.split()
#             l1.append(l[2])
# from collections import defaultdict
# dd = defaultdict(int)
# for word in l1:
#     dd[word] += 1
# print(dd)



""" 4. Reading countries from football.txt """

# f_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\football.txt'

# with open(f_path) as file:
#     for line in file:
#         if line.strip():
#             country = line.split("\t")
#             print(country[1])



""" 5. least & most occurrences of the country name"""

f_path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\football.txt'
path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.txt'

from collections import defaultdict, Counter
dd = defaultdict(int)

with open(path) as file:
    for line in file:
        if line.strip():
            l1 = line.split()
            for word in l1:
                dd[word] += 1
# print(dd)
c = Counter(dd)
most, *rest, least = c.most_common()
print(most, least)
