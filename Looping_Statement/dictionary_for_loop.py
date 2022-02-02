""" WAP to print the keys from the dictionary """

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# # Method 1: Traversing through dictionary directly
# for key in d:
#     print(key, end=" ")
# print()
#
# # Method 2: by using built-in-function d.keys()
# for key in d.keys():
#     print(key, end=" ")
# print()
#
# # Method 3: by using built-in-function d.items()
# for key, value in d.items():
#     print(key, end=" ")

""" WAP to print the values from the dictionary """

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# # Method 1: Traversing through dictionary directly d[key]
# for key in d:
#     print(d[key], end=" ")
# print()
#
# # Method 2: by using built-in-function d.values()
# for value in d.values():
#     print(value, end=" ")
# print()
#
# # Method 3: by using built-in-function d.items()
# for key, value in d.items():
#     print(value, end=" ")
# print()
#
# # Method 4: by using built-in-function d.get()
# for key in d:
#     print(d.get(key), end=" ")

""" print items along with their indices"""
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# # Method 1: by using enumerate() class
# for item in enumerate(d):
#     print(item, end=" ")
#
# print()
#
# # Method 2: by using enumerate() class
# for index, item in enumerate(d):
#     print((index, item), end=" ")
#
# print()
#
# # Method 3: by using enumerate(d.items())
# for index, (key, value) in enumerate(d.items()):
#     # print(index, key, value, end=", ", sep=" - ")
#     print((index, key, value), end=" ")

""" WAP to create a dictionary of character and its count pair in a string """

# string = "hello world"
#
# # Method 1: (3rd preference)
# d = {}
# for char in set(string):
#     d[char] = string.count(char)
# print(d)
#
# print()
#
# # Method 2: without built-in-method    # Try to avoid this method (4th preference)
# d1 = {}
#
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     d1[i] = count
# print(d1)
#
# print()
#
# # Method 3: if - else statement (2nd preference)
# d2 = {}
#
# for char in string:
#     if char not in d2:
#         d2[char] = 1
#     else:
#         d2[char] += 1
# print(d2)
#
# print()
#
# # Method 4: (1st preference)
# from collections import defaultdict
# dd = defaultdict(int)
#
# for char in string:
#     dd[char] += 1
# print(dd)

""" WAP to create a dictionary with word and its count pair """

# string = "python is a language, python programming is easy"
#
# l = string.split()
#
# # Method 1: by using defaultdict
# from collections import defaultdict
#
# dd = defaultdict(int)
# for word in l:
#     dd[word] += 1
# print(dd)
#
# print()
#
# # Method 2: by using if-else statement
# d = {}
#
# for word in l:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
#
# print()
#
# # Method 3: by using count() built-in-method
# d1 = {}
# for word in l:
#     d1[word] = l.count(word)
# print(d1)
#
# print()
#
# # Method 3: (4th preference)
# d4 = {}
# for word in l:
#     count = 0
#     for j in l:
#         if word == j:
#             count += 1
#     d4[word] = count
# print(d4)

""" WAP to create a dictionary with word and its length pair """

# string = "python is a language, python programming is easy"
# list_ = string.split()
# d = {}
#
# for word in list_:
#     d[word] = len(word)
# print(d)

""" WAP to create a dictionary with word and its length pair only if the word is of even length """

# string = "python is a language, python programming is easy"
# list_ = string.split()
# d1 = {}
#
# for word in list_:
#     if len(word) % 2 == 0:
#         d1[word] = len(word)
# print(d1)

""" WAP to create a dictionary with word and length pair only if the word is starting with vowel """

# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
# for word in list_:
#     if word[0].lower() in "aeiou":
#         d[word] = len(word)
# print(d)


""" WAP to create a dictionary with word and its count pair if the word is not repeated """ ## word is not repeated

# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
# print(d)

""" WAP to reverse the values in the dictionary if the value is of type string """  ###

# d = {"a": "hello", "b": 100, "c": 10.2, "d": "world"}

# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)
#
# print()

# Method 2: (but keep in mind above mentioned method we are going to chage original dictionary then the result of below mentioned method double reversed that why we get same output as input dictionary
# d1 = {}
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)

""" WAP to get all duplicate items and its count pair in the list """

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# d = {}
#
# for word in names:
#     if names.count(word) > 1 :
#         d[word] = names.count(word)
# print(d)

""" WAP to get the following outputs """

# sentence = "hello world welcome to python programming hi there"
# output = {"h": ["hello", "hi"], "w": ["world", "welcome"], "t": ["to", "there"], "p": ["python", "programming"]}
#
# l = sentence.split()
#
# # Method 1: using normal method
#
# d = {}
#
# for word in l:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         # d[word[0]] += [word]
#         d[word[0]].append(word)
#
# print(d)
#
# print()
#
# # Method 2: by using defaultdict()
#
# from collections import defaultdict
# dd = defaultdict(list)
#
# for word in l:
#     # dd[word[0]] += [word]
#     dd[word[0]].append(word)
# print(dd)

""" WAP to create a dictionary with element and its indices pair in the given list """

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# # Method 1: by using normal method
# d = {}
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)
#
# print()
#
# # Method 2: by using defultdict
# from collections import defaultdict
# dd = defaultdict(list)
#
# for index, item in enumerate(names):
#     dd[item] += [index]
# print(dd)

""" WAP to flip key and value """

# d = {"a": 1, "b": 2, "c": 3}
# d1 = {}
# # Method 1:
# for key, value in d.items():
#     d1[value] = key
# print(d1)
#
# print()
#
# # Method 2:
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)
