""" 1. WAP to remove all the duplicate elements in the list """

# names = ['apple', "google", "apple", "yahoo", "google"]
# l = []

# Method 1:
# for element in names:
#     if element not in l:
#         l.append(element)
#
# print(l)            # ['apple', 'google', 'yahoo']

# Method 2:
# for element in names:
#     if names.count(element) == 1:
#         l.append(element)
#
# print(l)            # ['yahoo']

# Method 3: by using set()

# print(set(names))            # {'apple', 'google', 'yahoo'}



""" 2. WAP to print all numeric values in a list """

# items = ['apple', 1.2, "google", "12.6", 26, "734"]

# Method 1: by using comprehension
# list_ = [item for item in items if isinstance(item, (int, float, complex))]
# print(list_)

# Method 2:
# l = []
# for element in items:
#     if isinstance(element, (int, float, complex)):
#         l.append(element)
#
# print(l)

""" 3. WAP to sum all even numbers in the given string """

# sentence = "hello 123 world 567 welcome to 9724 python"
# sum_ = 0
# # Method 1:
# for char in sentence:
#     if char.isdigit() and int(char) % 2 == 0:
#         sum_ += int(char)
#
# print(f"Sum of all even numbers are {sum_}")


""" 4. WAP to create a list with all the languages which starts with "p" or "P" """

# languages = ["Python", "Java", "Perl", "PHP", "python", "JS", "c++", "JS", "python", "ruby"]
#
# # by using list comprehension:
# l = [element for element in languages if element[0] in "pP"]
# print(l)


""" 4.1 WAP to create a set with all the languages which starts with "p" or "P" """

# languages = ["Python", "Java", "Perl", "PHP", "python", "JS", "c++", "JS", "python", "ruby"]
#
# # Method 1: by using set comprehension:
# set_ = {element for element in languages if element[0] in "pP"}
# print(set_)
#
# # Method 2:
# set_ = set()
#
# for item in languages:
#     if item[0] in "pP":             # if item[0].lower() in "p":
#         set_.add(item)
#
# print(set_)


""" 5. Build a list with only even length string """

# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
#
# # method 1: using list comprehension
# print([item for item in names if len(item) % 2 == 0])


""" 6. Reverse the item of a list if the item is of odd length string otherwise keep the item as it is """

# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
# # Method 1: by using comprehension
# print([word[::-1] if len(word) % 2 != 0 else word for word in names])
# print([word if len(word) % 2 == 0 else word[::-1] for word in names])
#
# # Method 2:
# l = []
# for word in names:
#     if len(word) % 2 == 0:
#         l.append(word)
#     else:
#         l.append(word[::-1])
#
# print(l)


""" 7. WAP to print the sum of entire list and sum of only internal list """

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# entire_sum = 0
#
# for item in l:      # [1, 2, 3], [4, 5, 6], [7, 8, 9]
#     internal_sum = 0
#     for i in item:          # (1, 2, 3), (4, 5, 6)
#         internal_sum += i
#         entire_sum += i     # 0+1= 1, 1+2= 3, 3+3=6, 6+4=10, 10+5=15, 15+6= 21
#     print(f'Sum of internal list {internal_sum}')
# print(f'Sum of entire list --> {entire_sum}')   # 6 + 15 + 24 = 45


""" 8. WAP to print list of Prime numbers between 1 - 100 """

# # Method 1:
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")
# print()
#
# # Method 2: Store inside a list
# l = []
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             l.append(num)
#
# print(l)


""" 9. WAP to reverse the list as below """

# words = ["hi", "hello", "pytho"]
# # output = ['nohtyp', 'olleh', 'ih']
#
# # Method 1: by using reversed()
# print([word[::-1] for word in reversed(words)])
#
# # Method 2: by using range()
# print([words[index][::-1] for index in range(len(words)-1, -1, -1)])
#
# # Method 3: by using slicing
# print([word[::-1] for word in words[::-1]])


""" 10. WAP to rotate item of the list """
item = ['apple', 1.2, 'google', "12.6", 26, '100']
k = 2
# output = [26, '100', 'apple', 1.2, 'google', '12.6']

# Method 1: by using while loop

# i = 1
#
# while i <= k:
#     *n1, n2 = item
#     item = n2, *n1
#     i += 1

# print(item)                 # (26, '100', 'apple', 1.2, 'google', '12.6') i.e. tuple

# Method 2:  **********************************************************
# for i in range(k):
#     remove_element = item.pop()
#     item.insert(0, remove_element)
#
# print(item)