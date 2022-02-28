""" 1. WAP to get all the duplicate items & the no of times the item is repeated in the list using both comprehension &
 default dict """
# names = ['apple', 'google', 'apple', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

# by using dictionary comprehension
# d = {item: names.count(item) for item in names if names.count(item) > 1}
# print(d)

# by using default dict
# from collections import defaultdict
# dd = defaultdict(int)
# for item in names:
#     if names.count(item) > 1:
#         # dd[item] = names.count(item)
#         dd[item] += 1
# print(dd)


""" 2. WAP to extract both alpha numeric value from the string, without using in-built-function """

# s = "sony123@pv#td948"
# res = ""
# for char in s:
#     if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
#         res += char
# print(res)

""" 3. WAF to print a particular word in a string along with its number of occurrences """


# def occurrence(l, word):
#     for item in l:
#         if item == word:
#             print(item, l.count(item))
#             break
#
#
# s = "Johny Johny yes papa"
# a = s.split()
# b = "Johny"
# occurrence(a, b)


""" 4. WAP to print longest non-repeated word in the sentence """

# s = "See and saw went to see a sea"
# l1 = s.split()
# l = [word for word in l1 if l1.count(word) == 1]
# res = sorted(l, key=len)
# print(f'Longest non-repeated word is: {res[-1]}')


""" 5. Sort the dictionary based on the last character of the key """
# prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.25}

# print(dict(sorted(prices.items(), key=lambda item: item[0][-1])))

""" 6. Build a list with only even with even length string using filter"""

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# res = filter(lambda item: item[0] % 2 == 0 and len(item[-1]) % 2 == 0, enumerate(names))
# print(list(res))

""" 7. WAP to return a list of elements raised to the power of their indices """
numbers = [32, 65, 39, 8, 1]



""" 8. WAP to count the no of occurences of word in the string without using in-built-method """

# sentence = "hello world welcome to python hello hi hello hello"


""" 9. WA Python program to sum the square of first 20 natural numbers """

"""10. WA Dictionary comprehension to create a dictionary with word as its key and if the word is of numeric type 
reverse it else add the word as it is """

# sentence = "12 plus 18 equals to 30"

""" 11. WAF that accepts two strings & returns True if the two strings are Anagrams of each other """

""" 12. 
list_ = [2, 3, 9, 5, 8, 2, 3, 0, 4, 5, 3, 7, 1, 3, 8] 
key = 3
output = [11, 2, 12, 9] """

"""" 13. WAP to get the following output 
input: s = 'AABBCCCDAACD'
output: 2A2B3C1D2A1C1D
"""

""" 14. 
names = ["apple", "google", "apple", "yahoo", "yahoo", "yahoo", "yahoo", "yahoo", "google", "gmail", 'gmail', 'gmail']
output should be:
{'apple': [0, 2], 'google':[1,5], 'yahoo':[3, 4], 'gmail':[6, 7, 8] }"""

""" 15. Find all maximum numbers from the below list """
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]