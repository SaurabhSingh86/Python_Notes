""" 1. WAP to print the number of occurrence of characters in a string without using built-in-functions """
# s = "helloworld"

# Method 1: by using dict comprehension (with built-in-function)
# d = {char: s.count(char) for char in s}
# print(d)

# Method 2: by using default dict
# from collections import defaultdict
# dd = defaultdict(int)
# for char in s:
#     dd[char] += 1
#
# print(dd)


""" 2. WAP to get the indexes of each item in the below list """

# names = ["apple", "google", "apple", "yahoo", "yahoo", "google", 'gmail', 'gmail', 'gmail']
# # output  = {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
#
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
#
# print(dd)


""" 3. Grouping files with same extensions """
# files = ["apple.txt", 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
#
# from collections import defaultdict
# dd = defaultdict(list)
# for element in files:
#     l = element.split(".")
#     dd[l[-1]] += [element]
#
# print(dd)
# {'txt': ['apple.txt', 'google.txt', 'facebook.txt'], 'pdf': ['yahoo.pdf', 'gmail.pdf', 'amazon.pdf', 'flipkart.pdf']})
#
# d = defaultdict(list)
# for item in files:
#     l = item.split(".")
#     d[l[-1]] += [l[0]]
#
# print(d)        # {'txt': ['apple', 'google', 'facebook'], 'pdf': ['yahoo', 'gmail', 'amazon', 'flipkart']})

# Method 2: by using if-else statement *******(check this method it is not working

# d1 = {}
# for element in files:
#     l = element.split(".")
#     if element not in d1:
#         d1[l[-1]] = [l[0]]
#     else:
#         d1[l[-1]] += [l[0]]
#
# print(d1)


""" 4. WAP to create a dictionary with only the repeated characters & count of the same """

# s = "hello world"
# d = {}
# for char in s:
#     if s.count(char) > 1:
#         d[char] = s.count(char)
#
# print(d)
#
# # Method 2: using comprehension
# print({char: s.count(char) for char in s if s.count(char) > 1})


""" 5. WAP to reverse the values in the dictionary if the value is of type string """
# d = {"a": 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# Method 1: using dict comprehension

# print({item: values[::-1] if isinstance(values, str) else values for item, values in d.items()})

# Method 2:

""" 6. WAP to get all the duplicate items & the number of times the item is repeated in the list """
# names = ["apple", "google", "apple", "yahoo", "google", "gmail", 'gmail', 'gmail', 'gmail']

# using comprehension
# print({item: names.count(item) for item in names if names.count(item) > 1})

# Method 2

# d = {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
#
# print(d)


""" 7. Grouping flowers & animals in the below list """

# items = ['lotus-flower', 'lily-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
#
# from collections import defaultdict
# dd = defaultdict(list)
# for item in items:
#     l = item.split("-")
#     dd[l[-1]] += [l[0]]
#
# print(dd)


""" 8. Grouping even & odd numbers """

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # output = {1:[1, 3, 5, 7, 9], 0:[2, 4, 6, 8, 10]}
#
# # Method 1:
# from collections import defaultdict
# d = defaultdict(list)
# for n in numbers:
#     if n % 2 != 0:
#         d[1] += [n]
#     else:
#         d[0] += [n]
#
# print(d)

# Method 2: by using if-else statement

# d = {}

""" 9. WAP to crating dictionary of city & population pairs using dictionary comprehension """

# cities = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai"]
# population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']
#
# print({city: populations for city, populations in zip(cities, population)})


""" 10. WAP to flip keys & values """
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
#
# print({value: key for key, value in d.items()})
