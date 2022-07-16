from collections import defaultdict, Counter
# path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
#
# # with open(path) as f:
# #     data = f.read()
# #     print(data)
# #     print(f.tell())
# #     f.seek(0)
# #     print(f.read(10))
#
# # with open(path) as file:
# #     print(file.readline(10))    # reads 10 characters from the first line
# #     print(file.readline(5))     # reads 5 characters after the previous output
# #     print(file.readline())      # reads the left out characters in the line
#
#
# # with open(path) as file:
# #     print(file.readlines())
#
# """ Reading the file without loading the same into memory"""
# # with open(path) as file:
# #     for line in file:
# #         print(line)
#
# """ count the number of lines in the file """
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     # print(count)
#
# """ line number and line in the file """
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         # print(count, line)
#
# # using enumerate()
# # with open(path) as file:
# #     for line_no, line in enumerate(file, start=1):
# #         print(line_no, line)
#
# """ count number of words in the file """
# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             count += 1
#     # print(count)
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         count += len(words)
#     # print(count)
#
# """ reading a file in reversed order """
# # with open(path) as file:
# #     for line in reversed(list(file)):
# #         print(line)
#
# """ count number of whitespaces """
# with open(path) as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count += 1
#     # print(count)
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         spaces = line.count(" ")
#         count += spaces
#     # print(count)
#
# """ count the number of words starting with vowels """
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#     # print(count)
#
# """ word and its count pair """
# with open(path) as file:
#     d = {}
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     # print(d)
#
# with open(path) as file:
#     dd = defaultdict(int)
#     for line in file:
#         for word in line.split():
#             dd[word] += 1
#     # print(dd)
#
# """ list of ip address from access-log.txt file """
# f_path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt"
# #
# with open(f_path) as file:
#     l = []
#     for line in file:
#         if line.strip():    # checks for the blank line in the file
#             list_ = line.split()
#             l.append(list_[0])
#     print(l)
# ip_ = Counter(l)
# print(ip_)
# print(ip_.most_common())
#
#
# """ create a dictionary of ip addresses and their count"""
# with open(f_path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split()
#             if words[0] not in d:
#                 d[words[0]] = 1
#             else:
#                 d[words[0]] += 1
#     # print(d)
#
# """ print nth line from the file """
# n = 3
#
# # using enumerate()
# # with open(path) as file:
# #     for line_no, line in enumerate(file, start=1):
# #         if line_no == n:
# #             print(line)
#
# # using count
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count == n:
#             # print(line)
#             break
#
# # islice(iterable, [start], stop, [step])
#
# from itertools import islice
# n = 3
# with open(path) as file:
#     res = islice(file, n-1, n)
#     # print(list(res))
#
# """ to print first n lines """
# n = 3
#
# # using islice
# with open(path) as file:
#     res = list(islice(file, n))
#     # print(res)
#
# # using enumerate
# # with open(path) as file:
# #     for line_no, line in enumerate(file, start=1):
# #         if line_no <= n:
# #             print(line)
#
#
# """ last n lines """
# n = 3
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#
#     file.seek(0)
#     res = islice(file, count-n, count)
#     # print(list(res))
#
# # using deque(iterable, [number])
# from collections import deque
# with open(path) as file:
#     lines = deque(file, n)
#     # print(list(lines))

file_path = r"C:\Users\Vidya\PycharmProjects\Alpha_3_batch\files_directory\txt_log_files\football.txt"

with open(file_path, encoding="UTF-8") as file:
    for line in file:
        if line.strip():
            country = line.split("\t")
            # print(country[1])

path = r"C:\Users\Vidya\PycharmProjects\Alpha_3_batch\files_directory\txt_log_files\sample.txt"
from collections import defaultdict, Counter

d = defaultdict(int)
with open(path) as file:
    for line in file:
        if line.strip():
            words = line.split()
            for word in words:
                d[word] += 1
print(d)
c = Counter(d)
most, *rest, least = c.most_common()
print(most, least)








































































