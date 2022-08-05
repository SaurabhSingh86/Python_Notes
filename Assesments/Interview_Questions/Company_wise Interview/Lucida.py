"""
1. What is the output of this program
numbers = {}
letter = {}
numbers[0] = 'hai'
numbers[3] = 'hello'
letter[2] = 'Python'
comb = {}
comb['Numbers'] = numbers
comb["Letter"] = letter
print(comb)
"""
# Output => {'Numbers': {0: 'hai', 3: 'hello'}, 'Letter': {2: 'Python'}}

# ---------------------------------------------------------------------------------------------------------------------
# 2. What is the output of os.getlogin()


# ---------------------------------------------------------------------------------------------------------------------
"""
3. what is the output of this program
print('{a}{b}{a}'.format(a='hello', b='world'))
"""
# output => helloworldhello

# ---------------------------------------------------------------------------------------------------------------------
""" 4. What is the output of this question
print('The {} side {1} {2}'.format('bright', 'of', 'it')) 
"""
# Output => Value Error

# Correct format is
# print('The {0} side {1} {2}'.format('bright', 'of', 'it'))
# The bright side of it


# ---------------------------------------------------------------------------------------------------------------------
""" 
5. What is the output of
print([1, 2, 3] * 3)
"""
# output => [1, 2, 3, 1, 2, 3, 1, 2, 3]

# value = False
# while not value:
#     n = int(input("Enter your number: "))
#     while n % 2 == 0:
#         print("Bye")
#         value = True

# Bye(Infinite loop of print Bye)

# ---------------------------------------------------------------------------------------------------------------------
"""
6. What is the output of this code
l = [1, 5, 5, 5, 1]
max_ = l[0]
indexofmax = 0
for i in range(1, len(l)):
    if l[i] > max_:
        max_ = l[i]
        indexofmax = i
print(indexofmax)
"""

# Output => 1

# ---------------------------------------------------------------------------------------------------------------------
# 7. partition
# s = 'abcdefcdgh'
# print(list(s.partition('cd')))
# ['ab', 'cd', 'efcdgh']

# print(s.split('cd'))
# ['ab', 'ef', 'gh']

# ---------------------------------------------------------------------------------------------------------------------
"""
8. What is the output of this program
l = ['ab', 'cd']
res = []
for i in l:
    res.append(i.upper())

print(res)
"""
# ['AB', 'CD']

# ---------------------------------------------------------------------------------------------------------------------
# 9. sqrt

# ---------------------------------------------------------------------------------------------------------------------
# 10. veggies cerel
# veggies = ['tomato', 'brocoli', 'Potato']
# veggies.insert(1, 'Cerels')
# print(veggies)

# output => ['tomato', 'Cerels', 'brocoli', 'Potato']

# ---------------------------------------------------------------------------------------------------------------------
# 11. annoyymous

# ---------------------------------------------------------------------------------------------------------------------
# 12. len(['hello', 1, 2, 3])

# ---------------------------------------------------------------------------------------------------------------------
"""13. What is the output of this python code

import collections
# a = dict()
a = collections.defaultdict(int)
print(a[1])
"""
# output => 0

# ---------------------------------------------------------------------------------------------------------------------
"""
14.
a = 10
b = 20


def func():
    global b
    a = 20
    b = 56


func()
print(a, b)
"""
# output => 10 56

# ---------------------------------------------------------------------------------------------------------------------
"""
15. What is the output of this program
"""
# l = []
# print(l.append("hello"))


# ---------------------------------------------------------------------------------------------------------------------
"""
16. 
print('for'.isidentifier())
"""
# Output => True

# print('True'.isidentifier())

# ---------------------------------------------------------------------------------------------------------------------
"""
17. 

"""

# ---------------------------------------------------------------------------------------------------------------------


"""
18. 

"""

# ---------------------------------------------------------------------------------------------------------------------

"""
19. 

"""

# ---------------------------------------------------------------------------------------------------------------------

"""
20. 

"""

# ---------------------------------------------------------------------------------------------------------------------

s1 = 'hello'
s2 = 'hello everyone'
s3 = 'hello everyone hello there'
s4 = 'It is red and that is green'

print(s1.partition('l'))  # ('he', 'l', 'lo')
print(s2.partition(" "))  # ('hello', ' ', 'everyone')
print(s3.partition("hello"))  # ('', 'hello', ' everyone hello there')
print(s4.partition("is"))  # ('It ', 'is', ' red and that is green')
print(s4.partition("Saurabh"))  # ('It is red and that is green', '', '')



# Second Round interview questions

"""1. brief introduction """

"""2. programming questions"""
""" 2.1 find the second highest value"""
# by using sorted()
# res = sorted(set(l))
# *e, smax, max_ = res
# print(f'The second highest value is {smax}')


"""2.2 squares of each element"""
# using list comprehension
# res = [element ** 2 for element in l]
# print(res)

"""2.3 what is the lambda function & solved by above question by using lambda"""
# lambda function
# res = list(map(lambda item: item**2, l))
# print(res)



"""3. What is the difference between a dictionary & JSON"""
"""4. difference between list & tuple"""
"""5. can we add or delete element from the tuple"""
"""6. Have you any knowledge of DataBase"""
"""7. Why did you switch your career in the IT field?"""
"""8. Can we use a break & continue at a time"""












