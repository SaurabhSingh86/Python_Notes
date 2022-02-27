""" Create three classes Dad, Mom and child and get first name, middle name & last name and last name should be the
same  for every class """


# class Dad:
#     def __init__(self, fname, mname, lname="Singh"):
#         self.first_name = fname
#         self.middle_name = mname
#         self.last_name = lname
#
#     def display(self):
#         print(self.first_name, self.middle_name, self.last_name)
#
#
# class Mom(Dad):
#     pass
#
#
# class Child(Mom):
#     pass
#
#
# c = Child("Ss", "V")
# c.display()             # Ss V Singh
#
# m = Mom("S", "R")
# m.display()             # S R Singh
#
# d = Dad("R", "B")
# d.display()             # R B Singh


""" Create a class that delays other class functionality """

from time import sleep


class Delay:
    def __init__(self, func):
        self.func = func
        self.delay = 2

    def __call__(self, *args, **kwargs):
        sleep(self.delay)
        return self.func


@Delay
class Arithmetic:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)


a = Arithmetic(7, 3)
a.add()
a.sub()
