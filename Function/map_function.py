# map applies a function to all the items in an input_list
# syntax:        map(function_name, list of inputs)
# map can be applied to more than one list but the lists should have the same length

""" WAP to check weather the string that is present inside a list is Palindrome or not """

# list_ = ["man", "mom", "dad", "arrow", "ocean", "civic"]
#
# palindrome = lambda item: item == item[::-1]
# res = map(palindrome, list_)
# print(list(res))                        # [False, True, True, False, False, True]

# res1 = filter(palindrome, list_)
# print(list(res1))                       # ['mom', 'dad', 'civic']


""" WAP that checks if the given list of numbers are even or odd """

# l1 = ["Tom", "Jerry", 26, 15, 31.5, 3+5j, 7]
# l = [element for element in l1 if isinstance(element, int)]
# l = [1, 2, 3, 4, 56, 6]
# def even_odd(num):
#     if num % 2 == 0:
#         return f'{num} is even'
#     return f'{num} is odd'
#
#
# output = map(even_odd, l)
# print(list(output))


"""" WAP to return the string which are starting with vowels """
l = ["apple", "gmail", "yahoo", "flipkart", "instagram"]
#
# # Method 1: by using def function:
#
#
# def vowel(item):
#     if item[0] in "aeiouAEIOU":
#         return item
#
#
# res = map(vowel, l)
# print(list(res))                    # ['apple', None, None, None, 'instagram']
#
#
# # Method 2: using lambda function
#
# vowels = lambda item: item[0] in 'aeiouAEIOU'
# output = map(vowels, l)
# print(list(output))                 # [True, False, False, False, True]


""" WAP to add the following list elements simultaneously """

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
#
# def add_(item1, item2):
#     return item1 + item2
#
#
# res = map(add_, a, b)
# print(list(res))


# Method 2: without using map (by using list comprehension)

# l = [i+j for i, j in zip(a, b)]
# print(l)



""" words into uppercase """

# sentence = "hello World"
#
# def upper_(word):
#     return word.upper()
#
# upper_lambda = lambda word: word.upper()
# print(list(map(upper_lambda, sentence.split())))          # ['HELLO', 'WORLD']
#
# res = map(str.upper, sentence.split())
# print(list(res))


""" words into lowercase """

# sentence = "HELLO VS"
#
# def lower_(word):
#     return word.lower()
#
# lower_lambda = lambda word: word.lower()
# print(list(map(lower_lambda, sentence.split())))        # ['hello', 'vs']
#
# res = map(str.lower, sentence.split())
# print(list(res))


""" all negative into positive numbers """

# l = [1, 6, -3, 9, -3.9, -4, 1, -1]
#
# print(list(map(abs, l)))
#
# print(list(map(lambda word: abs(word), l)))
#
#
# def convert_(num):
#     return abs(num)
#
# print(list(map(convert_, l)))


""" WAP to get list of length of each word """
#
s = "python is easy language"

# print(list(map(len, s.split())))
#

"""" word and its length inside a tuple """
# sentence = "Python is easy language"
# l = sentence.split()
# def word_len(word):
#     return word, len(word)
#
# res = map(word_len, l)
# print(list(res))            # [('Python', 6), ('is', 2), ('easy', 4), ('language', 8)]
                            # if we have miltiple value output then output will get autmatically in tuple form.

""" to get list of tuple of character & its ascii value """
# word = "VS Code"
# #
# def char_ascii(char):
#     return char, ord(char)
#
# res = map(char_ascii, word)
# print(list(res))


""" item to the power of its index"""

# l = [10, 20, 30, 40]

# def func(item):
#     index, value = item
#     return value ** index
#
# print(list(map(func, enumerate(l))))
#
#
# def func1(item):
#     return item[-1] ** item[0]
# print(list(map(func1, enumerate(l))))
#
# print(list(map(lambda item: item[1] ** item[0], enumerate(l))))

""" WAP to add the following list elements simultaneously """


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# Method 1: normal function
# def add_(item1, item2):
#     return item1 + item2
#
# res = map(add_, a, b)
# print(list(res))


# Method 2: by using lambda
print(list(map(lambda n1, n2: n1+n2, a, b)))