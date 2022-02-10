""" WAP to return even values in the below list """

# l = [ 1, 2, 3, 4, 5, 6, 7, 8]
# even = lambda num: num % 2 == 0
#
# res = filter(even, l)
# print(list(res))


""" WAP that returns a list of strings with odd length"""

l = ["gmail", "flipkart", "google", "yahoo", "rediff"]

odd_length = lambda item: len(item) % 2 != 0

res = filter(odd_length, l)
print(tuple(res))

