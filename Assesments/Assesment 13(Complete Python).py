""" 1. Convert the string "Hello Welcome to Python" to comma separated string """

string_ = "Hello Welcome to Python"

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

names = ["apple", "google", 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

