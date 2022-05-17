""" 1. Operator Overloading """


# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#
# b1 = Book(200)
# b2 = Book(300)
#
# print(b1 + b2)

##TypeError: unsupported operand type(s) for +: 'book' and 'book'

# How to overcome it

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):                  # __add__ is a magic method to add two object that is created from class
#         return self.pages + other.pages        # here self is nothing but b1 object & other is  nothing but b2 object
#
#
# b1 = Book(200)
# b2 = Book(300)
#
# print(b1+b2)            # # 500


# #))Overloading > employee Class Objects:---->
#
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __ge__(self,other):
#         return self.salary >= other.salary
#
#
# e1=employee("Elon",20000)
# e2=employee("Steve",20000)
#
# print(e1>=e2)
#
#
# #))Overloading <= employee Class Objects:---->
#
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __le__(self,other):
#         return self.salary<=other.salary
#
#
# e1=employee("Elon",20000)
# e2=employee("Steve",30000)
# print(e1<=e2)
#
# # Note:--> <= can also manage >= and vice versa
#
# #))Program to Overload Multiplication Operator to Work on employee salary Objects:
#
# class employee:
#     def __init__(self,name,salary_per_day):
#         self.name=name
#         self.salary_per_day=salary_per_day



# class working_day:
#     def __init__(self,no_of_working_days):
#         self.no_of_working_days=no_of_working_days
#
#     def __mul__(self,other):
#         return self.no_of_working_days * other.salary_per_day
#
#
# e=employee("Mark",750)
# s=working_day(27)
# print(s*e)


# class parent:
#     def marry(self):
#         print("Akansha")
#
# class child(parent):
#     def marry(self):
#         print("Anshika")
#
# s = child()
# s.marry()
