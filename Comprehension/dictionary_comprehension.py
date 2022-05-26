"""WAP to create a dictionary with item & its index pair"""

# s = "python"
#
# d = {char: index for index, char in enumerate(s)}
# print(d)


"""WAP to create a dictionary with words & its length pair"""
# s = "sky is no limit"
#
# dict_ = {word: len(word) for word in s.split()}
# print(dict_)
#
""" WAP to create a dictionary with character & its count pair """
#
# string = "hello world"

# # comprehension

# d = {item: string.count(item) for item in string}
# print(d)

"""WAP to create a dictionary of words & its count pair only if the words in of even length """

# s = "python is a language, python programming is easy"

# d = {word: list_.count(word) for word in list_ if len(word) % 2 == 0}
# print(d)

""" WAP to create a dictionary with index & word pair if the word is of odd length reverse it else keep it as it is """

# string = "python is a language, python programming is easy"
# l = string.split()
# dd = {index: word[::-1] if len(word) % 2 != 0 else word for index, word in enumerate(l)}
# print(dd)


""" WAP to create a dictionary with word & its length pair only if the word starting with vowels """

# string = "python is a language, python programming is easy"
# l = string.split()
# dd = {word: len(word) for word in l if word[0] in "aeiouAEIOU"}
# print(dd)

""" WAP to create a dictionary of index & item pair if the item is of string data type reverse it & rest as it is """
# l = ["python", 1, 2.5, "ruby", "vS code", 99, 3+0j]
# d = {index: item if not isinstance(item, str) else str(item)[::-1] for index, item in enumerate(l)}
# print(d)

# d1 = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(l)}
# print(d1)

""" WAP to create a dictionary of index & item pair if the item is of string data type keep it as it is else reverse it """
# l = ["python", 1, 2.5, "ruby", "vS code", 99, 3+0j]
# d = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(l)}
# print(d)
#
# d1 = {index: str(item)[::-1] if not isinstance(item, str) else item for index, item in enumerate(l)}
# print(d1)

""" WA dictionary comprehension to flip or swap key & values in a dictionary """
# d = {"a": 1, "b": 2, "c": 3, "d":4, "e": 5}
#
# dd = {value: key for key, value in d.items()}
# print(dd)
#
# print()
#
# d2 = {d[key]: key for key in d}
# print(d2)


"""WAP to create a dict of character & its ascii value pair"""
# s = "rainbow"
# d = {char: ord(char) for char in s}
# print(d)


"""WAP to create a dict of character as value & its ascii as key"""

# d1 = {ord(char): char for char in s}
# print(d1)
