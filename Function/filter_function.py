""" WAP to return even values in the below list """

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# even = lambda num: num % 2 == 0
#
# print(list(map(even, l)))               # [False, True, False, True, False, True, False, True]
# print(list(filter(even, l)))            # [2, 4, 6, 8]


""" WAP that returns a list of strings with odd length"""

# l = ["gmail", "flipkart", "google", "yahoo", "rediff"]
#
# odd_length = lambda item: len(item) % 2 != 0
#
# res = filter(odd_length, l)
# print(tuple(res))


""" WAP which returns all the words starting with vowels in the given sentence """

# sentence = "hello how are you"
# print(list(filter(lambda word: word[0] in "aeiouAEIOU", sentence.split())))
#
#
# def vowels(word):
#     if word[0] in 'aeiouAEIOU':
#         return word
#
#
# print(list(filter(vowels, sentence.split())))

""" WAP to square all the elements which is present even indexing position by using filter """

# l = [10, 20, 30, 40, 40]


# def even_square(item):
#     if item[0] % 2 == 0:
#         return item[1] ** 2
#
#
# res = list(filter(even_square, enumerate(l)))
# print(list(map(even_square, res)))
