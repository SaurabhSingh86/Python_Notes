""" WAP to check weather a given element that is present inside a list is Palindrome or not """

# l = ["hai", "madam", "malayalam", "dad", "python", "mom"]
# list_ = [item for item in l if item == item[::-1]]
# print(list_)


# s = "radar"
# if s == s[::-1]:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')


"""WAP to remove all the vowels present inside the string """
# s = "she sells sea, shells on the sea shores"

# # Method 1:
# res = ""
# for char in s:
#     if char in "aeiouAEIOU":
#         pass
#     else:
#         res += char
#
# print(res)
#
# # Method 2:
# res = ""
# for char in s:
#     if char not in "aeiouAEIOU":
#         res += char
#
# print(res)

# Method 3: by using replace() method   ###################################
# for char in s:
#     if char in "aeiouAEIOU":
#         res = s.replace(char, "")
#         s = res
#
# print(res)

"""WAP to separate each elements then combine by "*" """

# s = "she sells sea, shells on the sea shores"
# l = s.split()
# print(l)
#
# res = "*".join(l)
# print(res)


""" WAP to print all the elements that have total no. of length less than 4 """
# l = ["hai", "hello", 'welcome', 'numbers', 'dictionary', 'set']
#
# # Method 1: by using list comprehension
# list_ = [element for element in l if len(element) <= 4]
# print(list_)
#
# # Method 2: by using if-else statement
# l1 = []
# for char in l:
#     if len(char) <= 4:
#         l1.append(char)
#
# print(l1)


"""WAP to convert all the characters into their ascii value"""
# l = ["hai", "hello", 'welcome', 'numbers', 'dictionary', 'set']
#
# l1 = []
# for item in l:
#     res = ""
#     for i in item:
#         res += str(ord(i))
#     l1.append(res)
#
# print(l1)

"""WAP to print each item that present inside the string if their length is more than 2"""
# s = "she sells sea, shells on the sea shores"

# Method 1
# l = s.split()
# res = []
# for item in l:
#     if len(item) >= 2:
#         res.append(item)
#
# print(res)
#
# # Method 2: by using comprehension
# l1 = s.split()
# list_ = [element for element in l1 if len(element) >= 2]
# print(list_)

'''WAP to print each element that is ending index of the element is 2 '''
# l = ['she', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shores']
#
# # Method 1:
# l1 = []
# for element in l:
#     if element.index(element[-1]) == 2:
#         l1.append(element)
#
# print(l1)
#
# # Method 2:
# list_ = [item for item in l if item.index(item[-1]) == 2]
# print(list_)

"""WAP to print numbers and other characters grouping same the same """

# s = "saurabhsingh8602@gmail.com"
#
# # Method 1: by using list comprehension (result in the form of list)
#
# l1 = [char for char in s if char.isdigit()]
# l2 = [char for char in s if not char.isdigit()]
# print(l1, l2)
#
# # Method 2: if-else statement (result in the form of string)
# rdigit = ""
# ralpha = ""
# for char in s:
#     if char.isdigit():
#         rdigit += char
#     else:
#         ralpha += char
#
# print(rdigit, ralpha)

""""""
# s = "he@l@lo@worl@d@"
# # output should be : "" if count of @ is odd
#
# for char in s:
#     if s.count("@") % 2 != 0:
#         res1 = ""
#         for i in s:
#             if i.isalpha():
#                 res1 += i
#         res = "@"+res1
#     else:
#         res = "none"
#
# print(res)


# s = "he@l@lo@worl@d@"
# output should be : "" if count of @ is odd

# l = s.split("@")
# print(l)
# res = []
# for index, item in enumerate(l):
#     if index % 2 == 0:
#         res.append(item)
#
# print(res)
#
# output = " ".join(res)
# print(output)


"""WAP to print even and odd number separately by using while loop from 1 to 20 """
#
# start = 1
# end = 20
# e_num = []
# o_num = []
# while start <= end:
#     if start % 2 == 0:
#         e_num.append(start)
#     else:
#         o_num.append(start)
#
#     start += 1
#
# print("Even numbers are: ", e_num)
# print("Odd numbers are: ", o_num)

"""WAP to print index & their count pair from 1 to 20 """
# start = 1
# end = 20
# l = []
# while start <= end:
#     l.append(start)
#     start += 1
#
# # res = [(index, l.count(num)) for index, num in enumerate(l)]
# res1 = [str((index, 1)) for index, num in enumerate(l)]
# # print(res)
# print(res1)

# l = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]
#
# res = [(str(index), str(value)) for index, value in l]
# print(res)

"""WAP to reverse the entire list as well as reverse their elements also """

# l = ["pytho", "VS Code", "Java", "Selenium"]

# Method 1: by using comprehension

# list_ = [word[::-1] for word in reversed(l)]
# print(list_)
#
# # Method 2: by using slicing
# list1 = [word[::-1] for word in l[::-1]]
# print(list1)

"""WAP to find which character has maximum number of occurrence """
# l1 = ["hy", "hello", 'hai', 'hello', 'python', 'hai', 'hello', 'vs', 'python', 'hai', 'hai', 'hello', 'python', "hello"]

# res = []
# for item in set(l1):
#     if item not in res:
#         res.append((item, l1.count(item)))
#
# print(res)
# #
# item_ = []
# count_ = []
# for item, count in res:
#     item_.append(item)
#     count_.append(count)
#
# print(item_)
# print(count_)
# max_ = max(count_)
# for i, j in res:
#     if max_ == j:
#         print(i)

# l1 = ["NS", "hello", 'hai', 'hello', 'python', 'hai', 'hello', 'vs', "zi", 'python', 'hai', 'hai', 'hello', 'python', "hello"]
#
#
# max1 = 0
# item = l1[0]
# for i in l1:
#     if l1.count(i) > max1:
#         max1 = l1.count(i)
#         item = i
# print(item)

"""find number of cube present inside the given from 1 - 30"""

# # Method 1:
# l1 = [n for n in range(1, 31)]
# for i in l1:
#     if i**3 in l1:
#         print(i, i**3, sep="->", end=", ")
#
# print()
# # Method: 2 by using comprehension:
#
# list_ = [(num, num**3) for num in l1 if num**3 in l1]
# print(list_)


""""""

# l2 = [1, 2, 3, 3, 5, 5, 9, 9, 5, 1.1]
# res = [num**2 if l2.count(num) > 1 else num**index for index, num in enumerate(set(l2))]
# print(res)

# a = 22
# b = 7
# pi = a/b
# print([str(pi)*10])


# from math import pi
# a = 10
# e = a*pi
# print(e)


# l = [f'{3.142}'* 10]

""" create a list"""

# s = "she sells sea shells on the sea shores"
# l = s.split()
# list_ = [item for item in l if len(item) % 2 == 0]
# print(list_)
#
# """ASCII value"""
# # list2 = [ord(item) for item in l]
#
# """ indexing is even = print index number else reverse it"""
# list3 = [item[::-1] if not len(item) % 2 == 0 else index for index, item in enumerate(l)]
# print(list3)
""""""

""" Tuple"""

# t = (1, 2, 3, 4, 5)
# l = [n*n for n in t]
# print(tuple(l))
#
#
# """Multiplied by pi"""
# from math import pi
# t = (1, 2, 3, 4, 5)
# l = [n*pi for n in t]
# print(tuple(l))


"""SET"""

l = ["a", "b", "c", "d"]
# list_ = [(item, index) for index, item in enumerate(l)]
# print(list_)
# d = {item: index for item, index in list_}
# print(d)


# d = {}
# s = {(j, i) for i, j in enumerate(l)}
# d = dict(s)
# print(d)


""""""

# s = input("Enter your sentence: ")
# f = input("Enter your character that you want to find: ")
# if f in s:
#     print(f'{f} is present given sentence')
# else:
#     print(f'{f} is not present given sentence')


# s = input("Enter your sentence: ")
# f = input("Enter your character that you want to find: ")
# if f in s:
#     print(ord(f))
# else:
#     print(s)
#     f1 = input("Enter your valid character that is show in above sequence: ")
#     if f1 in s:
#         print(ord(f1))


# s = input("Enter your sentence: ")
# f = input("Enter your character that you want to find: ")
# if f in s:
#     print(f'{f} is present inside the sentence')
# else:
#     print(f'{f} is not present inside the sentence')
#     print()
#     print("Sentence is ==>>: ", s)
#     f1 = input("Enter your valid word that is shown above sentence: ")
#     if f1 in s:
#         print(f'{f1} is present inside the the sentence')


"""Function"""
# python is general purpose, object-oriented, high level programming language


# def user_input(sequence):
#     find_ = input("Enter your character that you want to find: ")
#     if find_ in sequence:
#         return f'{find_} is present inside the sentence'
#     else:
#         print(f'{find_} is not present inside the sentence')
#         print("Sentence is ==>>: ", s)
#         return user_input(sequence)
#
#
# s = input("Enter your sentence: ")
# print(user_input(s))


# l = lambda word: word == word[::-1]
# print(l("madam"))
#
# l2 = lambda word: f'{word} is Palindrome' if word == word[::-1] else f'{word} is not a palindrome'
# print(l2("madam"))
# print(l2("saurabh "))

# l1 = lambda num: num % 2 == 0
# print(l1(4))


""""""
# list_ = ["hai", "mom", 'dad', 'hello']
# palindrome = lambda string: string == string[::-1]
# res = map(palindrome, list_)
# print(list(res))

# list_ = ['hai', 1, 3.5, 7+5j, 73, 8, 6]
# # numbers = lambda num: num % 2 == 0
# l = [item for item in list_ if isinstance(item, int)]
# res = map(l, list_)
# print(list(res))


l = ["apple", "gmail", "yahoo", "flipkart", "instagram"]
# vowels = lambda string: string[0] in 'aeiouAEIOU'
# res = map(vowels, l)
# print(list(res))


# def vowels(item):
#     if item[0] in "aeiouAEIOU":
#         return item
#
#
# res = filter(vowels, l)
# print(list(res))

# print(help("keywords"))

# import keyword
# print(keyword.kwlist)


# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# entire_sum = 0
# for l in list_:
#     internal_sum = 0
#     for n in l:
#         internal_sum += n
#         entire_sum += n
#     print(f'Sum of internal list {internal_sum}')
#
# print(f'Sum of entire list --> {entire_sum}')




# D = {"name": "apple", "id": 23456}
# d = {"name": "apple", "id": 78945}
#
# dd = {k1: [D[k1], d[k2]] for k1, k2 in zip(D, d)}
# print(dd)



# l = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 12, 13, 13, 14, 16, 16, 96, 96, 100]
#
# even = {"even": [l[i]] for i in }
# print(even)
# odd = {"odd": [l[j]] for j in enumetate()}
# print(odd)
