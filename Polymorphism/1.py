word = "hello"
# len(word)
# internally work word.__len__()

names = ["hai", "hello"]
# names[0]
# internally work names.__getitem__(0)

"hai" in names
# True
# internally work names.__contains__('hai')

names[0] = 'Instagram'
# names.__setitem__(1, 'Instagram')


# names.__delitem__()

# Container Protocols
# 1. __len__()                              -       should return an integer
# 2. __contains__(item)                     -       should return Bool
# 3. __setitem__(index, value)              -
# 4. __getitem__(index)                     -       return the item present in that index

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
# p = Point(1, 2)

# print(len(p))
# TypeError: object of type 'Point' has no len()
# so we have to define __len__()


# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __len__(self):
#         print("Executing __len__")
#         return 2
#
# p = Point(1, 2)
# print(len(p))

# ------------------------------------------------------------------------------------------------------------------
class Point:
    def point(self):
        self.a = a
        self.b = b
        self.points = (a,b)

    def __contains__(self, item):
        return item in self.points              # __contains__ method of tuple class

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError()


p = Point(1, 2)
p[0]        # p.__getitem__(0)  => 1
p[1]        # p.__getitem__(1)  => 2
p[2]        # p.__getitem__(2)  => raise IndexError
