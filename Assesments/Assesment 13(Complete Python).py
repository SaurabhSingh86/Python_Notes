""" 1. Convert the string "Hello Welcome to Python" to comma separated string """

# string_ = "Hello Welcome to Python"

# Method 1
# l = string_.split()
# res = ",".join(l)
# print(res)

# Method2:
# res = string_.replace(" ", ",")
# print(res)

# Method 3:
# res = ""
# for char in string_:
#     if char == " ":
#         res += ","
#     else:
#         res += char
# print(res)


""" 2. Reverse item of list if the item is of odd length sting otherwise keep the item as it is by using list 
comprehension"""

# names = ["apple", "google", 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#
# l = [item for item in names if len(item) % 2 != 0]
# print(l)


""" 3. Creating dictionary of city and population pairs using dict comprehension """

# cities = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai"]
# population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']
#
# res = {city: populations for city, populations in zip(cities, population)}
# print(res)


""" 4. WAP to print the following pattern 
*
*
*
**
*
***
*
*****
*
*****

"""

# for num in range(1, 11):
#     if num % 2 == 0:
#         r = num / 2
#         print("*" * int(r))
#
#     else:
#         print("*")


""" 5. WAP to reverse a string without using any in built function """

# Method 1:
# s = "Hello Everyone"
# res = ""
# i = len(s) - 1
# while i >= 0:
#     res += s[i]
#     i = i - 1
#
# print(res)


""" 6. WAP to check if the given string is Palindrome or not without using reversed function """

# string_ = "radar"
# a = string_
#
# i = 0
# res = ""
# while i < len(string_):
#     res = string_[i] + res
#     i += 1
#
# if res == a:
#     print(f'{a} is Palindrome')
# else:
#     print(f'{a} is not Palindrome')


""" 7. Write a Python Program to get the below output """
# sentence = "Hi How are you"
# # output should be: "uoy era woH iH"
# l = sentence.split()
# res = [item[::-1] for item in reversed(l)]
# output = " ".join(res)
# print(output)


""" 8.Find the longest word in the sentence """
# sentence = "Hello world. Welcome to Python"
# l = sentence.split()
# res = sorted(l, key=len)
# print(f' Longest word in the give string is {res[-1]}')


""" 9. WAP to reverse the values in the dictionary if the value is of type sting """

# d = {"a": "Hello", "b": 100, "c": 10.1, "d": "world"}
# res = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(res)


""" 10. WAP to sum all the numbers in the string below """

# s = "Sony12India567Pvtltd"
# sum_ = 0
# for num in s:
#     if num.isdigit():
#         sum_ += int(num)
#
# print(sum_)


""" 11. WAP to iterate through list and built a new dictionary of word and its length pair, only if the item of the 
list has even number of characters by using dictionary comprehension """
# names = ["apple", 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# d = {item: len(item) for item in names if len(item) % 2 == 0}
# print(d)


""" 12. create a dictionary by grouping Flowers & animals in the below list"""

# from collections import defaultdict
# dd = defaultdict(list)
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# for element in items:
#     l = element.split("-")
#     dd[l[1]] += [l[0]]
#
# print(dd)


""" 13. WADF to delay the execution of a function for n seconds """

