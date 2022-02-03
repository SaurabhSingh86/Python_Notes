"""WAP to square all the elements that is present inside the list"""

# l = [1, 2, 3, 4, 5]
# res = []

#by using normal method
# for item in l:
#     res.append(item*item)
#
# print(res)

# # by using list comprehension

# square_list = [i*i for i in l]
# print(square_list)

"""WAP to create a list of tuples which is having index & the corresponding items"""

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# #by using normal method
#
# res = []
# for item in enumerate(l):
#     res.append(item)
#
# print(res)
#
# # by using list comprehension
# res = [item for item in enumerate(l)]
# print(res)
#
# # or
# res = [(index, item) for index, item in enumerate(l)]
# print(res)
#
# #by using range()
# res = [(index, l[index]) for index in range(len(l))]
# print(res)

""" WAP to create a list of even number from the below list """
# l = [2, 9, 98, 100, 201, 36, 25, 41]
#
# # Normal method
# list_ =[]
# for enum in l:
#     if enum % 2 == 0:
#         list_.append(enum)
# print(list_)
#
# # list comprehension
# enum = [num for num in l if num % 2 == 0]
# print(enum)

"""WAP to print even number from 0 to 10"""

# enum = [n for n in range(11) if n % 2 == 0]
# print(enum)
#
# enum = [n for n in range(0, 11, 2)]
# print(enum)

"""WAP to print even & odd number separately between 0 to 10"""

# even_num = []
# odd_num = []
#
# for num in range(10):
#     if num % 2 == 0:
#         even_num.append(num)
#     else:
#         odd_num.append(num)
# print("Even numbers are: ", even_num)
# print("Odd numbers are: ", odd_num)

# by using list comprehension

# even_num = [num for num in range(0, 11, 2)]
# odd_num = [num for num in range(1, 11, 2)]
#
# print(even_num, odd_num)
#
# even_num = [num for num in range(11) if num % 2 == 0]
# odd_num = [num for num in range(11) if num % 2 != 0]
#
# print(even_num, odd_num)

"""WAP to create a list using the following list if the word is of even length store the word as it is & if it is of odd length reversed the word & store it"""

# l = ["python", "Node Js", "selenium", "Java", "c++", "SQL"]
#
# # normal method
# res = []
# for item in l:
#     if len(item) % 2 == 0:
#         res.append(item)
#     else:
#         res.append(item[::-1])
#
# print(res)
#
# # by using comprehension
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)


"""WAP to create a list from the following list if the elements are of type string keep them as it is else reversed it"""

# l = ["python", 12, "selenium", 73.4, True, "SQL"]
#
# res = [item if isinstance(item, str) else str(item)[::-1] for item in l]
# print(res)
#
# res = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
# print(res)

"""WA list comprehension to create a list with the string starting with vowels"""
# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo", "inox"]
#
# res = [item for item in files if item[0] in "aeiouAEIOU"]
# print(res)


""" traversing through a list in reversed order """

# l = ["python", 10, 3.2, "selenium", "Java"]
# # # by using range()
# # res = [l[item] for item in range(len(l)-1, -1, -1)]
# # print(res)
#
# # # by using reversed class
#
# res = [item for item in reversed(l)]
# print(res)
#
# #by using slicing
#
# res = [item for item in l[::-1]]
# print(res)

""" print even indexed elements in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# list_ = [l[index]for index in range(len(l)) if index % 2 == 0]
# print(list_)
#
# l1 = [l[index] for index, item in enumerate(l) if index % 2 == 0]
# print(l1)

""" print integers in a list """

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# list_ = [item for item in l if isinstance(item, int)]
# print(list_)

""" print only numeric datatypes"""

# l = ["python", 10, 3.2, "selenium", "Java", 5+7j]
#
# list_ = [element for element in l if isinstance(element, (int, float, complex))]
# print(list_)

""" print length of each string in the list """

# l = ["python", "Node JS", "selenium", "Java"]
#
# list_ = [len(element) for element in l]
# print(list_)

""" print the strings with even length """

# l = ["python", "Node JS", "selenium", "Java"]
#
# list_ = [(element, len(element)) for element in l if len(element) % 2 == 0]
# print(list_)

""" reverse string elements or else keep it as it is"""

# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby", 3+5j]
# l = [element[::-1] if isinstance(element, str) else element for element in list_]
# print(l)

""" print if the element is starting with vowel """

# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo", "intex"]
# l = [item for item in files if item[0].lower() in "aeiou"]
# print(l)

""" print the elements other than the given element"""
# numbers = [10, 40, 20, 80, 20, 40, 30]
# n = 20
# l = [element for element in numbers if element != n]
# print(l)

""" print the palindromes in the given list """
# l = ["python", "dad", "hai", "malayalam", "madam", "mom"]
#
# list_ = [element for element in l if element == element[::-1]]
# print(list_)

""" print all the extensions in the following list """

files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]


# l = [char.split(".")[-1] for char in files]
# print(l)


""" printing file name with odd length """

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
#
# l = [char.split(".")[0] for char in files if len(char) % 2 != 0]
# print(l)

###############################################################################
# """ index of first occurrence of the given element in the list"""
#
numbers = [10, 40, 20, 80, 20, 40, 30, 20]
num = 20
# not possible through comprehension


""" check if the number is a prime number """
# not possible by list comprehension

""" to generate prime number series"""

# not possible by list comprehension



"""find prime no from the given list"""

l =[2, 4, 11, 15, 86, 98, 99]

for num in l:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")


