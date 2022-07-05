"""
Brillio first round Interview Questions
1. about yourself
2. how many years of experience in Selenium
3. Write a login page?
(there was a "live coding board" we had to write our codes on that board)
4. How to automate a login page interacting with an excel file or Html file, in the login page there was a username, password & login button
5. how many years of experience in Java & Python
6. how comfortable in SQL?
7. Do you have any knowledge of SQL (again asked)?
8. Difference between Implicit wait & Explicit wait?
9.  How to handle alerts

10. Rating yourself in java & python
string_ = 'selenium'
10.1 WAP to find the no. of occurrence of each character
10.2 WAP to sort the list on the basis of occurrence
Both the code is written in "live coding board" & run in "online complier"
explain the logic.

11. Again she asked regarding SQL

Final round Interview Questions in Brillo
1. About yourself
2. Python Programming Questions
2.1 Array = [12, 3, 1, 2, -6, 5, -8, 6]
	targetSum = 0
	Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

2.2 Array = [5, 1, 22, 25, 6, -1, 8, 10]
	Sequence = [1, 6, -1, 10]
	Output: True
	Sequence = [1, 1]
	Output: False

3. Decorator
4. Generator & its benefits
5. Framework
6. how to take screenshots (write code)
7. How to handle popups
8. How to communicate with developers?
9. What is your daily working procedure?
10. What type of framework do you have to use in your project, and how to create test cases?
11. What are the benefits of the folder/packages in the framework
12. What is POM(in detail)?
13. Where did you use Decorator in your project?
14. What are soft assertion and hard assertion?
15. can you give the priority after discussing with the developer?
16. What are the benefits of severity & priority?
17. what is time complexity?
18. where did you use Explicit wait & Implicit wait in your projects?
19. Asked many more questions from agile, selenium, projects, pythons
"""



"""
string_ = 'selenium'
1. WAP to print the no. of occurrence of each character
2. WAP to sort the list on the basis of occurrence
"""
# string_ = 'selenium'
#
# from collections import defaultdict
# dd = defaultdict(int)
#
# for char in string_:
#     dd[char] = string_.count(char)
#
# print(dd)
# defaultdict(<class 'int'>, {'s': 1, 'e': 2, 'l': 1, 'n': 1, 'i': 1, 'u': 1, 'm': 1})

# Now I want to sort the above dictionary based on occurrence
# res = sorted(dd.items(), key=lambda item: item[-1])
# print(res)
# [('s', 1), ('l', 1), ('n', 1), ('i', 1), ('u', 1), ('m', 1), ('e', 2)]

# if we want the output in dictionary
# print(dict(res))
# {'s': 1, 'l': 1, 'n': 1, 'i': 1, 'u': 1, 'm': 1, 'e': 2}

# ---------------------------------------------------------------------------------------------------------------------
""" 
Write a login page? 
How to automate a login page interacting with an excel file or Html file, in the login page there was a username, 
password & login button
"""

# class Login:
#     testbox_username_id = "Email"
#     testbox_password_id = "password123"
#     login_button_xpath = "//input[@class='button-login']"
#     logout_linktext = "Logout"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def SetUserName(self, username):
#         self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)

#     def SetPassword(self, password):
#         self.driver.find_element_by_id(self.testbox_password_id).send_keys(password)

#    def clk_login(self):
#         self.driver.find_element_by_xpath(self.login_button_xpath).click()

#    def clk_logout(self):
#         self.driver.find_element_by_linktext(self.logout_linktext).click()

# ---------------------------------------------------------------------------------------------------------------------
""" remove duplicate elements from the list"""
# ---------------------------------------------------------------------------------------------------------------------
""" reverse a list """
# l = ['Baby', 'Dragon', 26, 1996, 'India']

# Method 1: by using reversed()
# res = []
# for word in reversed(l):
#     res.append(word)
#
# print(res)                                          # ['India', 1996, 26, 'Dragon', 'Baby']

# Method 2: using comprehension
# print([word for word in reversed(l)])               # ['India', 1996, 26, 'Dragon', 'Baby']

# print([word for word in l[::-1]])                   # ['India', 1996, 26, 'Dragon', 'Baby']

# ---------------------------------------------------------------------------------------------------------------------
""" find the second highest no from set """
s = {10, 20, 30, 4}

# Method 1 using sorted (first preference)
# res = sorted(s)
# print(res[-2])          # 20


# Method 2 type cast (2nd preference)
# l = list(s)
# l.sort()
# print(l[-2])            # 20

# Method 3:this method not work in all the conditions like l = [100, 20, 10, 5, 2, 1, 0] or s = [1000, 999, 2000,
# 10, 5000, 0, 5000, 20, 10, 0] to avoid this problem we use one more condition that is inside a elif statement

# s = [100, 20, 10, 5, 2, 1, 0]
# s = [1000, 999, 2000, 10, 5000, 0, 5000, 20, 10, 0]

# max_ = 0            # highest value
# max2_ = 0           # second-highest value
# for item in set(s):
#     if item > max_:
#         max2_ = max_
#         max_ = item
#     elif item > max2_:
#         max2_ = item
#
#
# print(f'Maximum value {max_}')
# print(f'Second highest value {max2_}')
# Maximum value 30
# Second highest value 20

# print(max(s))           # 30

# print(set("hai"))
# {'i', 'a', 'h'}

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# Array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
#
# # Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
# # sum_ = 0
# l = []
# for num1 in Array:
#     for num2 in Array:
#         for num3 in Array:
#             if num1 + num2 + num3 == targetSum:
#                 l.append([num1, num2, num3])
#
# print(l)

# Array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
#
# Array.sort()
# for i in range(len(Array)-2):
#     right = i
#     left = i+1


# Validate Subsequence:
# Array = [5, 1, 22, 25, 6, -1, 8, 10]
# Sequence = [1, 6, -1, 10]
# Output: True
# Sequence = [1, 1]
# Output: False

# def sequence(Array, Sequence):
#     for num in Sequence:
#         if num not in Array:
#             return False
#         else:
#             Array.remove(num)
#
#     else:
#         return True

# print(sequence(Array, Sequence))

# Array = [5, 1, 22, 25, 6, -1, 8, 10]
# # Sequence = [1, 6, -1, 10]
# Sequence = [1, 22, 1, 2]


# Output: True

# def sequence(Array, Sequence):
#     for num in Sequence:
#         if num not in Array:
#             return False
#         else:
#             Array.remove(num)
#
#     else:
#         return True
#
#
# print(sequence(Array, Sequence))

# Array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
#
# # Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
# # sum_ = 0
# l = []
# array = Array
# for num1 in Array:
#     array.remove(num1)
#     for num2 in array:
#         array.remove(num2)
#         for num3 in array:
#             if num1 + num2 + num3 == targetSum:
#                 l.append([num1, num2, num3])
#                 array.append(num1)
#                 array.append(num2)
#
# print(l)


#
# ---------------------------------------------------------------------------------------------------------------------
# Array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
# Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
# res = []
# Array.sort()
#
# for num1 in Array:
#     for num2 in Array:
#         if num1 == num2:
#             continue
#         else:
#             for num3 in Array:
#                 if num1 == num3 or num2 == num3:
#                     continue
#                 else:
#                     if targetSum == num1 + num2 + num3:
#                         res.append([num1, num2, num3])
#
# print(res)
# print(len(res))


# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
