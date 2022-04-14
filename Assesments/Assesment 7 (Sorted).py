""" 1. sort this list from a-z."""

# l = ["hello", "ball", "zebra", "yak", "apple"]
#
# print(sorted(l))


""" 2. Sort the words based on length """
# s = "this world is not enough"
# l = s.split()
# d = {item: len(item) for item in l}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res)

""" 3. Sort based on the last character from the word """
# l = ['hello', 'ball', 'zebra', 'yak', 'apple']
# res = sorted(l, key=lambda item: item[-1])
# print(res)


""" 4. Sort based on the length of the keys """
d = {'flipkart': 10, 'walmart': 15, 'google': 20}
# res = sorted(d.items(), key=lambda item: item[0])
# print(res)

print(sorted(d, key=len))


""" 5. d = {'flipkart':10, 'walmart':15, 'google':20} 
Sort based on the values """



""" 6. WAF that accepts two strings & returns True if the two strings are Anagram of each other """

""" 7. prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.25}
Sort the dictionary based on the share prices if the prices are more than 40"""

""" 8. 

Portfolio = [
{'name':'IBM', 'shares': 100, 'price': 91.1}
{'name':'AAPL', 'shares': 50, 'price': 543.22}
{'name':'FB', 'shares': 200, 'price': 21.09}
{'name':'HPQ', 'shares': 35, 'price': 31.75}
{'name':'YHOO', 'shares': 45, 'price': 16.35}
{'name':'ACME', 'shares': 75, 'price': 115.65}
]
Sort the above list based on number of shares
"""


""" 9. Find the most repeated charcter in the below string """
# sentence = "hi hello hi hi hiiiiiiiii"


""" 10. Find the longest non-repeating sub-string in the below string"""
sentence = "This is a programming language and programming is fun"