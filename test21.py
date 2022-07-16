#
# s1 = input("enter your string")
# def demo(s):
#     if s == s[::-1]:
#         print("it is palindrome:")
#     else:
#         print("it is not palindrome:")
#
#
# demo(s1)

# s = "iam purnima am working in  teest ysmtrs from five years"
# # res = ""
# res = s.replace(" ", "")
# # print(res)
# s1 = ""
# # for index,item in enumerate(res):
# #     if index == 4:
# #         s1 = s1 + " "
# #     else:
# #         s1 += item
#
# # print(s1)
# #  4th space
# count = 0
#
# for item in res:
#     if count == 4:
#         s1 += " "
#         count = 0
#     else:
#         s1 += item
#         count += 1
#
# print(s1)



# st = "Python is programming language"
# s1 = st.replace(" ", "")
# print(s1)
#
# def space(s, count_ = 0):
#     res = ""
#     for char in s:
#         count_ += 1
#         if count_ % 4 == 0:
#             res += char + " "
#         else:
#             res += char
#     return res
#
#
# print(space(s1))


s = "Python is programming language"


def space2(s1):
    l = s1.split()
    print(l)
    l1 = []
    for _ in range(0, len(l), 4):
        l1.append(" ")
    res = "".join(l1)
    return res


print(space2(s))


# def fibonachi(n, a=0, b=1):
#     while a <= n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#
#
# fibonachi(14)


n = int(input("Enter your number: "))
for num in range(1, n+1):
    while num > 0:
        print(num, end=" ")
        num -= 1
    print()

