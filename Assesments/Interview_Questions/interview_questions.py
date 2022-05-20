""" find the second highest value in the given dictionary"""
# d = {"a": 20, "b": 10, "c": 30, "d": 30}
# l = []
# for key, value in d.items():
#     if value not in l:
#         l.append(value)
#
# res = sorted(l)
# print(res[-2])


from collections import defaultdict

# d1 = {}
# for key, value in d.items():
#     if d[key] not in d1.values():
#         d1[key] = value
#
# res = sorted(d1.items(), key=lambda item: item[-1])
# print(res[-2])


""" """
# input = 25
# output = 425

# Method 1: using concatenation
# i = str(input)
# res = ""
# for num in i:
#     res = res + str(int(num)**2)
# print(res)

# Mwthod 2:
# l = "623"
# res = []
# for i in l:
#     res.append(str(int(i)**2))
# output = "".join(res)
# print(output)


""" How to remove special character by using re"""
# items = ['$123.53', '$177.75', '$7784.58']

import re

# Method 1
# for item in items:
#     # replace "$" with an empty string. (need to escape $)
#     match = re.sub(r"\$", "", item)
#     print(match)

# Method 2:
# for item in items:
#     match = "".join(re.findall(r"[\d\.]", item))
#     print(match)

# Method 3:
# for item in items:
#     match = "".join(re.findall(r"[\d\.d]+", item))
#     print(match)


""" """
# s1 = "([{([{}])}])"
# s2 = "([{([{})})"
#
#
# def equal_(s):
#     open_ = 0
#     close_ = 0
#     for char in s:
#         if char in "({[":
#             open_ += 1
#         else:
#             close_ += 1
#     if open_ == close_:
#         print("Equal")
#     else:
#         print("Not Equal")
#
#
# equal_(s1)
# equal_(s2)

""" """
#
# d = {"a": 1, "b": 2, "c": 3}
# user_input = input("Enter your string: ")
# sum_ = 0
# for char in user_input:
#     sum_ += d[char]
#
# print(sum_)


# l = "ac"
# sum_ = 0
# for i in l:
#     if i in d:
#         sum_ += d[i]
#
# print(sum_)


""" find the missing item in the list"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]


# Method 1:
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# for i in range(1, len(list1)):
#     if i not in list1:
#         print(i, end=" ")


# # Method 2:
# sum_list1 = sum(list1)
# expected_sum = 0
# for num in range(11):
#     expected_sum += num
# find_missing_term = expected_sum - sum_list1
# print(find_missing_term)
