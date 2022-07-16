""" 26 What is the output of the following """
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])           # [[1, 2, 3], [4, 5, 6]]    i.e. list of list
# print((a, b))           # ([1, 2, 3], [4, 5, 6])    i.e Tuple of lists
# print([*a, *b])         # [1, 2, 3, 4, 5, 6]        i.e. Concatenate it or merge into single list


""" 10. Write program to merge two different lists. """

# a = [1, 2, 3]
# b = [4, 5, 6]

# Method 1: using unpacking
# merge_list = [*a, *b]
# print(merge_list)                       # [1, 2, 3, 4, 5, 6]

# Method 2: using concatenation
# c = a + b
# print(c)                                # [1, 2, 3, 4, 5, 6]


# Method 3: Using chain
# from itertools import chain
# s = chain(a, b)                         # Returns an Iterators
# print(list(s))

