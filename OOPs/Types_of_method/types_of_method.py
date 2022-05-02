# 1=> Instance Method:

# class Student:
#     '''This is a student class'''
#
#     def __init__(self, name, roll, mark):
#         self.name = name
#         self.roll = roll
#         self.mark = mark
#
#     def school_name(self):
#         print("My Institute name is Pyspider")
#
#     def display(self):
#         print("My name is: ", self.name)
#         print("My roll is: ", self.roll)
#         print("My mark is: ", self.mark)
#         self.school_name()
#
#
# s1 = Student("Mohan", 1, 90)
# s2 = Student("Rohan", 2, 98)
# s3 = Student("Sohan", 3, 95)
#
# s1.display()
# print()
# print(s2.name)

# My name is:  Mohan
# My roll is:  1
# My mark is:  90
# My Institute name is Pyspider
#
# Rohan


# 2=> Class Method:

# class Demo:
#     def __init__(self):
#         print("Constructor")
#
#     def m1(self):
#         print("Instance Method")
#
#     @classmethod
#     def m2(cls):
#         print("Class Method")
#
#     @staticmethod
#     def m3():
#         print("Static Method")
#
#
# s = Demo()
# Demo.m2()
# print()
# s.m2()
#
# Constructor
# Class Method
#
# Class Method


# 3=> Static Method:
class Demo:
    def __init__(self):
        print("Constructor")

    def m1(self):
        print("Instance Method")

    @classmethod
    def m2(cls):
        print("Class Method")

    @staticmethod
    def m3():
        print("Static Method")


s = Demo()
Demo.m3()
print()
s.m3()

# Constructor
# Static Method
#
# Static Method