# def greet():
#     yield "Hello world"
#     yield "hai"
#     yield "hello"
#
#
# msg = greet()
# for sentence in msg:
#     print(sentence)

# l = [1, 2, 3, 4, 5]
# using list comprehension:
# list_ = [num ** 2 for num in l]
# print(list_)

# by using generators:


# def squares():
#     for item in l:
#         yield item ** 2
#
#
# res = (item ** 2 for item in l)
# print(next(res))        # 1
# print(next(res))        # 4
# print(next(res))        # 9
# print(next(res))        # 16
# print(next(res))        # 25
# print(next(res))        # StopIteration

""" WAG function to yield even numbers in the range 1 - 50 """
#
#
# def evens():
#     for item in range(1, 51):
#         if item % 2 == 0:
#             yield item
#
#
# even_num = evens()
# print(even_num)             # Generator object address  <generator object even at 0x00000204B4AD8748>
# print(list(even_num))
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
#
#
# # above are Generator function
#
# # Generator expression
# evens_ = (item for item in range(1, 51) if item % 2 == 0)
# print(evens_)           # <generator object <genexpr> at 0x000002958ACC8848>
# print(list(evens_))
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


""" WAGF & expression to yield the name starting with vowels in the given list"""
# names = ['john', 'eve', 'bob', 'emmo', 'ano']
#
#
# def vowels(names_):
#     for name in names_:
#         if name[0] in 'aeiouAEIOU':
#             yield name
#
#
# # Generator expressions:
# vowels_ = vowels(names)
# print(list(vowels_))


# vowels_ = (name for name in names if name[0] in "aeiouAEIOU")
# print(vowels_)              # <generator object <genexpr> at 0x00000169E88487C8>
# print(list(vowels_))        # ['eve', 'emmo', 'ano']


""" WAGF & expression to yield length of each line in a file, only if the line is not empty """

# path = r'C:\Users\Saurabh\PycharmProjects\Python_Notes\files_directory\txt_log_files\sample.txt'

#
# def l_file():
#     with open(path) as file:
#         for line in file:
#             if line.strip():
#                 l = line.split()
#                 c = len(l)
#                 yield c
#
#
# print(list(l_file()))               # [2, 9, 9, 3, 5, 3, 3]


""" WAGF to yield each line in a file, only if the line is not empty """

# def line_length():
#     with open(path) as file:
#         for line in file:
#             if line.strip():
#                 yield line
#
#
# lines = line_length()
# print(list(lines))


""" dictionary """
# names = ['john', 'eve', 'bob', 'emmo', 'ano']
# d = {}
# for name in names:
#     if name not in d:
#         d[name[0]] = [name]
#     else:
#         d[name[0]] += [name]
# print(d)                            # {'j': ['john'], 'e': ['emmo'], 'b': ['bob'], 'a': ['ano']}


""" division """

# a = 10
# b = 0
# try:
#     print(a / b)
# except:
#     print("In exception block")


# ------------------------------------------------------------------------------------------------------------------
# default exception block

# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except:
#     print("In exception block")


# ------------------------------------------------------------------------------------------------------------------
# specific exception block

# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except ZeroDivisionError:
#     print("In exception block")
#
# print("hello")

# ------------------------------------------------------------------------------------------------------------------
# Multiple exception block : we can handle n number of exception block

# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except ZeroDivisionError:
#     print("Zero divison handled")
#
# except NameError:
#     print("Name Error Handled")
#
# print("Hello")

# or

# try:
#     print(a / b)
# except(ZeroDivisionError, NameError):
#     print("In except block")
#
# # or
# except(ZeroDivisionError, NameError) as error_msg:
#     print("In Except block")
#     print(error_msg)



# ------------------------------------------------------------------------------------------------------------------
# Generic Exception block