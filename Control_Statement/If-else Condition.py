""" WAP to check given character is uppercase or lowercase """
s = "V"
#
# # Method 1: by using built-in-method
# if s.isupper():
#     print(f'{s} is uppercase character')
# else:
#     print(f'{s} is lowercase character')

## Method 2: without using built-in-method

# if 'a' <= s <= 'z':
#     print(f'{s} is lowercase character')
# else:
#     print(f'{s} is uppercase character')




# Assignment

""" 1. WAP to print greatest among three numbers """




""" 2. WAP to  check if the entered character is vowel or not if the character is an vowel crete a dictionary with 
character as key & ASCII value of the character as value"""

# char = "a"
# d = {}
# if char.lower() in "aeiou":
    # d[char] = ord(char)                             # Method 1
    # d.update({char: ord(char)})                     # Method 2
    # d.setdefault(char, ord(char))                   # Method 3
    # print({char: ord(char)})
#
# print(d)

d = {}
d.setdefault("python")
print(d)
d.setdefault("Java", 4)
print(d)
