""" 1. WA List comprehension to filter all the languages which starts with 'p' or "P" """
# languages = ["Python", "Java", "Perl", "PHP", "Python", "JS", "C++", "JS", "Python", "Ruby"]
#
# list_ = [item for item in languages if item[0] in "pP"]
# print(list_)


""" 2. WA List comprehension to filter-out those names which are less than 6 characters """
# names = ["apple", "google", "yahoo", "gmail", "flipkart", "instagram", "microsoft"]
#
# l = [name for name in names if len(name) < 6]
# print(l)


""" 3. WA list comprehension to reverse the item of a list if the item is of odd length string otherwise keep the item
 as it is """
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
#
# l1 = [item[::-1] if len(item) % 2 != 0 else item for item in names]
# print(l1)


""" 4. WA list comprehension to raise the elements in the list to the power of their index """
# a = [1, 2, 3, 4, 5]
#
# list_ = [item ** index for index, item in enumerate(a)]
# print(list_)


""" 5. Build a list of tuples with string & its length pair using list comprehension """
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
#
# l2 = [(item, len(item)) for item in names]
# print(l2)


""" 6.  WAP to print all numeric values in a list using list comprehension """
# items = ["apple", 1.2, 'google', '12.6', 26, '100']
#
# res = [element for element in items if isinstance(element, (int, float, complex))]
# print(res)


""" 7. WAP to rotate elements in the list """
# items = ["apple", 1.2, 'google', '12.6', 26, '100']
# n = 3
#
# # Method 1: by using while loop
# i = 1
# while i <= n:
#     *n1, n2 = items
#     items = n2, *n1
#     i += 1
# print(items)

# Method 2: by using for loop

# for i in range(n):
#     remove_element = items.pop()
#     items.insert(0, remove_element)
# print(items)


""" 8. WAP to check if the elements in the second list is series of continuation of the items in the first list """
# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
# c = [*a, *b]
#
# def series(c):
#     dif = c[1] - c[0]
#     for i in range(len(c)-1):
#         if c[i+1] - c[i] == dif:
#             continue
#         else:
#             return "not a series of first list"
#     return 'is a series'


# print(series(c))

l = [1, 2, 3, 4, 5, 6]
a = 7
sum = 0
for i in range(len(l)-1):
    if l[i] + l[i+1] == a:
        print(l[i], l[i+1])


""" 9. Find all max numbers from the below list """
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# max_ = max(numbers)
#
# # Method 1:
#
# list_ = [item for item in numbers if item == max_]
# print(list_)
#
# # Method 2:
# for num in numbers:
#     if num == max_:
#         print(num, end=" ")


""" 10. WA list comprehension to get a list of even numbers from 1-50 """

# even_list = [num for num in range(1, 51) if num % 2 == 0]
# print(even_list)