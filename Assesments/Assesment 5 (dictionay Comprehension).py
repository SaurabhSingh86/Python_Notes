""" 1. WAP to get the indexes of each item in the below list. """

# names = ["apple", "google", "apple", "yahoo", "yahoo", 'google', 'gmail', 'gmail', 'gmail']
# output should be: {'apple': [0, 2], 'google':[1, 5], 'yahoo':[3, 4], 'gmail': [6, 7, 8]}

# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
# print(dd)


""" 2. Reverse the values in the dictionary if the value is of type string """
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# dd = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(dd)


""" 3. WAP to get all the duplicate items & the number of time the item is repeated in the list """

# names = ["apple", "google", "apple", "yahoo", "yahoo", 'google', 'gmail', 'gmail', 'gmail']
#
# dd = {item: names.count(item) for item in names if names.count(item) > 1}
# print(dd)


""" 4. Creating dictionary of city & population pairs using dictionary comprehension """

# cities = ["Tokyo", "Delhi", "Shanghai", "Sao-Paulo", "Mumbai"]
# population = ["38,001,00", '25,703,168', '23,740,778', '21,066,245', '21,042,538']
#
# d2 = {city: populations for city, populations in zip(cities, population)}
# print(d2)


""" 5. WAP to flip key & value """
# d= {"a": "hello", "b": 100, "c": 10.1, "d": "world"}
# d1 = {v: k for k, v in d.items()}
# print(d1)

""" 6. Group even & odd index values with comprehension """
l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 88, 99, 100]

# Method 1:
# e_index = [l[index] for index in range(0, len(l), 2)]
# o_index = [l[index] for index in range(1, len(l), 2)]
# list_ = [e_index, o_index]
# a = ["even", "odd"]
# d = {i: j for i, j in zip(a, list_)}
# print(d)

# Method 2: not working
e_index = {"even": l[index] for index in range(0, len(l), 2)}
o_index = {"odd": l[index] for index in range(0, len(l), 2)}

dd = {i: e_index[i] if i == "even" else o_index[j] for i, j in zip(e_index, o_index)}
print(dd)

""" 7. Grouping both of the dictionary items in a single dictionary using comprehension """
# D = {"names": "apple", "ID": 152778}
# d = {"names": "apple", "ID": 657678}
# dd = {k1: [D[k1], d[k2]] for k1, k2 in zip(D, d)}
# print(dd)


""" 8. Create a dictionary with the items in tuple as key & its unicode as value using comprehension """
# T = (9, 56, 78, 123, 456)
# dd = {item: chr(item) for item in T}
# print(dd)


""" 9. Create a dictionary taking keys & values using items in the list, take key before special character & value after special character, using comprehension """

# list_ = ["food@table", "lilly@flower", "human@walk", "being@work"]
# d = {element.split("@")[0]: element.split("@")[-1] for element in list_}
# print(d)


""" 10. Create dictionary with key as string items & value as integer using the item in the given list, using comprehension """
s = [(4, 56, 78), ("one", "Two", "Three")]

# a, b = s
# dd = {i: j for i, j in zip(b, a)}
# print(dd)
