# sorted(iterable, *, key=None, reverse=False):-       => output in the form of "list"
#       1> Returns a new sorted list from the items in return iterable
#       2> Has two optional arguments which must be specified as keyword arguments.
#       3> sorted only Homogeneous data type (it means we can't sort iterable that contain Heterogeneous data type)

# key => specifies a function of one argument that is used to extract a comparison key from each element in iterable
#          e.g key=str.lower
#          The default value is None (compare the element directly)
#
# reverse => is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
#            sorted by default ascending order
#            if we want descending order then use => reverse=True
#            strings are sorted => alphabetically  (based on ASCII value)
#            Numbers are sorted => numerically


""" default sorting the collection datatype"""

# => String :-
# s = "PythOn"
# print(sorted(s))                      # ['O', 'P', 'h', 'n', 't', 'y']  => sorted by their ascii value
# print(sorted(s, reverse=True))        # ['y', 't', 'n', 'h', 'P', 'O']

# => List :-
# l = [5, 4, 2, 3, 1, 9, 11, 7]
# print(sorted(l))                                       # [1, 2, 3, 4, 5, 7, 9, 11]  output in the form of List
# print(sorted(l, reverse=True))                         # [11, 9, 7, 5, 4, 3, 2, 1]

# list_ = ["python", "java", "c", "ruby", "perl"]
# print(sorted(list_))                                   # ['c', 'java', 'perl', 'python', 'ruby']
# print(sorted(list_, reverse=True))                     # ['ruby', 'python', 'perl', 'java', 'c']

# => Tuple :-
# t = (5, 4, 2, 3, 1, 9, 11, 7)
# print(sorted(t))                                        # [1, 2, 3, 4, 5, 7, 9, 11]    output in the form of List
# print(sorted(t, reverse=True))                          # [11, 9, 7, 5, 4, 3, 2, 1]

# => Set :-
# set_ = {"python", "java", "c", "ruby", "perl"}
# print(sorted(set_))                                     # ['c', 'java', 'perl', 'python', 'ruby']
# print(sorted(set_, reverse=True))                       # ['ruby', 'python', 'perl', 'java', 'c']

# => Dictionary :-
# d = {"gmail": 5, "apple": 3, "walmart": 7, "flipkart": 8}
# print(sorted(d))                                        # ['apple', 'flipkart', 'gmail', 'walmart']  visible layer
# print(sorted(d, reverse=True))                          # ['walmart', 'gmail', 'flipkart', 'apple']


# <<==~~~~~~~~~~~~~~~~ Custom Sorting  ~~~~~~~~~~~~~~~==>>

""" WAP to sort the element present in the list based on their length """

l = ["python", "java", "c", "ruby", "perl"]
#
# print(sorted(l, key=len))                           # ['c', 'java', 'ruby', 'perl', 'python']
# print(sorted(l, key=len, reverse=True))             # ['python', 'java', 'ruby', 'perl', 'c']
#                                                     # if the number of length are same then their order get preference


""" WAP to find the longest & the shortest word in the following string """

# sentence = "Python is programming language"

# Method 1:
# l = sentence.split()
# res = sorted(l, key=len)
# print(f'Longest word is: {res[-1]}, shortest word is: {res[0]}')     # Longest word is: programming, shortest word: is
#
# # Method 2: by using packing
# shortest, *rest, longest = sorted(sentence.split(), key=len)
# print(f'Longest word is: ', longest)                                 # Longest word is:  programming
# print(f'Shortest word is: ', shortest)                               # Shortest word is:  is


""" WAP to find the longest & the shortest word along with their length in the following string """

# sentence = "Python is programming language"

# Method 1:
# l = sorted(sentence.split(), key=len)
# print(f'Longest word {l[-1]}, contain {len(l[-1])} characters')
# print(f'Shortest word {l[0]}, contain {len(l[0])} characters')

# Method 2:
# shortest, *rest, longest = sorted(sentence.split(), key=len)
# print((shortest, len(shortest)), (longest, len(longest)))           # ('is', 2) ('programming', 11)



""" WAP to short the below list element based on the last character of each string """

# l = ["python", "java", "c", "ruby", "perl"]
#
# Method 1: by using normal function
#
# def last_item(item):
#     return item[-1]
#
#
# print(sorted(l, key=last_item))                 # ['java', 'c', 'perl', 'python', 'ruby']

# Method 2: by using lambda function
#
# last_chr = lambda element: element[-1]
# print(sorted(l, key=last_chr))                  # ['java', 'c', 'perl', 'python', 'ruby']


""" WAP to short the below list based on middle character of each element """

# l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key=lambda item: item[len(item) // 2]))         # ['ruby', 'c', 'python', 'perl', 'java']

# ==>> Sorting dictionary
# shorting a dictionary based on its keys

# d = {"gmail": 5, "walmart": 7, "apple": 3, "flipkart": 8}

# print(sorted(d))                                    # ['apple', 'flipkart', 'gmail', 'walmart']
# print(sorted(d.keys()))                             # ['apple', 'flipkart', 'gmail', 'walmart']
# print(sorted(d.items()))        # *Prefer           # [('apple', 3), ('flipkart', 8), ('gmail', 5), ('walmart', 7)]


""" Based on length of keys """

# print(sorted(d, key=len))                                # ['gmail', 'apple', 'walmart', 'flipkart']
# print(sorted(d.keys(), key=len))                         # ['gmail', 'apple', 'walmart', 'flipkart']
# print(sorted(d.items(), key=lambda item: len(item[0])))  # [('gmail', 5), ('apple', 3), ('walmart', 7), ('flipkart', 8)]
# print(dict(sorted(d.items(), key=lambda item:len(item[0]))))

""" WAP to short a dictionary based on values """

# d = {"gmail": 5, "walmart": 7, "apple": 3, "flipkart": 8}
# print(sorted(d, key=lambda item: d[item]))                  # ['apple', 'gmail', 'walmart', 'flipkart']
# print(sorted(d.values()))                                   # [3, 5, 7, 8]
# print(sorted(d.items(), key=lambda item: item[-1]))         # [('apple', 3), ('gmail', 5), ('walmart', 7), ('flipkart', 8)]
# print(dict(sorted(d.items(), key=lambda item: item[-1])))   # {'apple': 3, 'gmail': 5, 'walmart': 7, 'flipkart': 8}

""" WAP to short the dictionary based on keys last item """

# d = {"gmail": 5, "walmart": 7, "apple": 3, "flipkart": 8}
# print(dict(sorted(d.items(), key=lambda item: item[0][-1])))


""" WAP to short the above list based on the temperature """

# temperatures = [("Delhi", 32), ("Mumbai", 27), ("Kolkata", 30), ("Chennai", 35)]
# print(sorted(temperatures, key=lambda item: item[-1]))
## [('Mumbai', 27), ('Kolkata', 30), ('Delhi', 32), ('Chennai', 35)]


""" WAP to get the most repeated word """

# sentence = "hi how are you how is your health"
# l = sentence.split()
# d = {item: l.count(item) for item in l}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])                                              # ('how', 2)


""" WAP to print the longest word with its length """
# sentence = "python is a programming language and programming is fun"
# l = sentence.split()
# d = {key: len(key) for key in l}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])                                          # ('programming', 11)


""" WAP to find longest non-repeated word """
# sentence = "python is a programming language and programming is fun"
# l = sentence.split()
# d = {item: len(item) for item in l if l.count(item) == 1}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])                                              # ('language', 8)

""" WAP to find shortest & longest non-repeated word """
# sentence = "python is a programming language and programming is fun"
# l = sentence.split()
# d = {item: len(item) for item in l if l.count(item) == 1}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[0], res[-1])

""" Sort the below list based on the names """
# l = [{"name": "Ram", "class": 6, "age": 12},
#      {"name": "Shyam", "class": 12, "age": 18},
#      {"name": "John", "class": 8, "age": 13}]
#
# # Ascending order:
#
# print(sorted(l, key=lambda item: item["name"]))
# print(sorted(l, key=lambda item: item["class"]))
# print(sorted(l, key=lambda item: item["age"]))
#
# # Descending order:
#
# print(sorted(l, key=lambda item: item["name"], reverse=True))
# print(sorted(l, key=lambda item: item["class"], reverse=True))
# print(sorted(l, key=lambda item: item["age"], reverse=True))
