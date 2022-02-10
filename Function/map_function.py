# map applies a function to all the items in an input_list
# syntax:        map(function_name, list of inputs)
# map can be applied to more than one list but the lists should have the same length

""" WAP to check weather the string that is present inside a list is Palindrome or not """

# list_ = ["man", "mom", "dad", "arrow", "ocean", "civic"]
#
# palindrome = lambda item: item == item[::-1]
# res = map(palindrome, list_)
# print(list(res))                        # [False, True, True, False, False, True]


""" WAP that checks if the given list of numbers are even or odd """

#error#######

# l1 = ["Tom", "Jerry", 26, 15, 31.5, 3+5j, 7]


# def even_odd(num):
#     if num % 2 == 0:
#         return f'{num} is even'
#     return f'{num} is odd'
#
#
# output = map(even_odd, l1)
# print(list(output))


"""" WAP to return the string which are starting with vowels """
# l = ["apple", "gmail", "yahoo", "flipkart", "instagram"]
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


""" WAP to add the followinng list elements simultaneously """

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

