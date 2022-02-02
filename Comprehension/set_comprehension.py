
"""Write a set comprehension to create a set of squares from 1 to 10"""
#
# res = {i ** 2 for i in range(1,11)}
# print(res)

# list_ = ["java", "python", True, 10, 1.4, "c++"]
#
# # res = {i, list_[i] for i in range(len(list_))}
# # print(res)
#
# res = { item for item in enumerate(list_)}
# print(res)

# list_ = ["python", "selenium", "Node JS", "Java", "SQL"]
#
# res = {(element, len(element)) for element in list_}
# print(res)

""" print index and its corresponding item in the set"""
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# res = {(index, item) for index, item in enumerate(l)}
# print(res)

"""WA set comprehension traversing through a set in reversed order """

# it'll not work

# l = ["python", 10, 3.2, "selenium", "Java"]

# res = {item for item in l[::-1]}
# print(res)

""" WA set comprehension print even indexed elements in the list """

# list_ = ["python", 10, 3.2, "selenium", "Java"]

#by using range

# res = {list_[index] for index in range(len(list_)) if index % 2 ==0 }
# print(res)

# by using enumerate()

# res = {for }

