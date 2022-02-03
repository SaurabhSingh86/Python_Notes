
# s = "sky is no limit"

# list_ = s.split()
# # Normal method
# res
# # for char in list_:
# #
# # #by using comprehension
# #
# # dict_ = {word: len(word) for word in list_}
# # print(dict_)
#
#
#
# string = "hello world"
# d = {}
#
# for char in string:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)
#
# # comprehension
from collections import defaultdict
# dd = defaultdict(int)
# d = {item : string.count(item) for item in string}
# print(d)

# """wap """"

# s = "python is a language, python programming is easy"
#
# list_ = s.split()
# dict_ = {word: list_.count(word) for word in list_}
# print(dict_)

# s = "python is a language, python programming is easy"
# list_ = s.split()
# d = {}
# for word in list_:
#     if len(word) % 2 == 0:
#         d[word] = list_.count(word)
# print(d)
# print()
# # by using comprehension
#
# d = {word: list_.count(word) for word in list_ if len(word) % 2 == 0}
# print(d)


# string = "python is a language, python programming is easy"
# # l = string.split()
# # dd = {index: word[::-1] if len(word) % 2 != 0 else word for index, word in enumerate(l)}
# # print(dd)

# string = "python is a language, python programming is easy"
# l = string.split()
# dd = {word: len(word) for word in l if word[0] in "aeiouAEIOU"}
# print(dd)

#
# l = ["python", 1, 2.5, "ruby", "vS code", 99, 3+0j]
# d = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(l)}
# print(d)


# d = {"a": 1, "b": 2, "c": 3, "d":4, "e": 5}
#
# dd = {value: key for key, value in d.items()}
# print(dd)
#
# print()
#
# d2 = {d[key]: key for key in d}
# print(d2)
# """WAP to create a dict of character & its ascii value pair"""
# s = "rainbow"
# d = {char: ord(char) for char in s}
# print(d)
#
# """WAP to create a dict of character as value & its ascii as key"""
# d1 = {ord(char): char for char in s}
# print(d1)
