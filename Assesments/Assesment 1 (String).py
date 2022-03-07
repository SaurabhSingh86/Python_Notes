""" 1. WAP to print "Bangalore" 10 times without using loop """

# print("Bangalore"*10)
# print("Bangalore\n"*10)


""" 2. WAP to count the number of digits & alphabets in the string """

# string = "hai1234python23"

# alp_count = 0
# dig_count = 0

# Method 1:
# for char in string:
#     if char.isalpha():
#         alp_count += 1
#     elif char.isdigit():
#         dig_count += 1

# print(f'Total number of alphabets are: {alp_count}')
# print(f'Total number of digits are: {dig_count}')


# Method 2:
# for char in string:
#     if 'a' <= char <= 'z' or "A" <= char <= "Z":
#         alp_count += 1
#     elif "0" <= char <= "9":
#         dig_count += 1
#
# print(f'Total number of alphabets are {alp_count}')
# print(f'Total number of digits are {dig_count}')


""" WAP to create a string by swapping the cases of the characters without using built in method """

# string = "VS PytHon"
# res = ""

# Method 1
# for char in string:
#     if 'a' <= char <= 'z':
#         res += chr(ord(char)-32)
#     elif "A" <= char <= "Z":
#         res += chr(ord(char) + 32)
#     else:
#         res += char
#
# print(res)

# (Method 2: by using built-in method)

# for char in string:
#     if char.islower():
#         res += char.upper()
#     elif char.isupper():
#         res += char.lower()
#     else:
#         res += char
#
# print(res)

""" 4. WAP to create a string with only consonants presents in the string """

# string = "Million Dollar Smile"
# res = ""
#
# # Method 1:
# for char in string:
#     if char.isalpha() and char not in "aeiouAEIOU":
#         res += char
#
# print(res)
#
# # Method 2:
#
# for char in string:
#     if char.isalpha() and char not in 'aeiouAEIOU':
#         print(char, end="")


""" 5. WAP to search for a character in the string & return its first occurrence position """

# s = "programming"
# find_ = "m"
#
# # Method 1:
# for char in s:
#     if char == find_:
#         # print(char, s.index(char))
#         print(f'{char} is present at index {s.index(char)}')
#         break                                         ## we use break keyword because we need only first occurrence
#
# # Method 2: by using range()
# for index in range(len(s)):
#     if find_ == s[index]:
#         print(f'{s[index]} is present at index {index}')
#         break
#
# # Method 3: by using enumerate()
#
# for index, char in enumerate(s):
#     if char == find_:
#         print(f'{char} is present at index {index}')
#         break


""" 6. WAP to print the character and its ascii value if the character is a vowel in the string """

# s = "she sells sea shells on the sea shore"
#
# for char in s:
#     if char.lower() in "aeiou":
#         print(f"ASCII value of {char} is {ord(char)}")


""" 7. WAP to print word & its length in string """

# s = "she sells sea shells on the sea shore"
# l = s.split()
# for word in l:
#     print(word, len(word))


""" 8. WAP to print the words that are starting with vowels in the string """

# s = "She is very good actor"
# l = s.split()
#
# for word in l:
#     if word[0] in "aeiouAEIOU":
#         print(word)


""" 9. WAP to count the number of characters in the string without using built-in-method """

# s = "She is very beautiful"
# count = 0
# for _ in s:
#     count += 1
#
# print(f'Total number of characters are: {count}')


""" 10. WAP to reverse a string without using slicing """

s = "Python is high level programming language"
#
# # Method 1: by using reversed()
# for char in reversed(s):
#     print(char, end="")
#
# print()
#
# # Method 2: by using range()
# for index in range(len(s)-1, -1, -1):
#     print(s[index], end="")
#
# print()

# Method 3: by using concatenation  **********************************************************
# res = ""
# for char in s:
#     res = char + res
#
# print(res)

