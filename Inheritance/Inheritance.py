# class Parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f'Executing Parent Google {self.value}')
#
#     def apple(self):
#         print(f'Executing Parent Apple')
#         self.google()
#
#
# # Child class having a separate method (or Completely Independent Method)
#
#
# class Child(Parent):
#     def demo(self):
#         print("Executing Demo")
#
#
# c = Child(100)
# c.demo()                  # Executing Demo
# c.google()                # Executing Parent Google 100
# c.apple()                 # Executing Parent Apple     # Executing Parent Google 100
#
# print(Child.__mro__)      # (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)
# print(c.__class__.__mro__)  # (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)


# child overriding parent class method


# class Child2(Parent):
#     def hello_world(self):
#         print("Hello World")
#
#     def google(self):
#         print("Executing Child2 Google")
#
#
# c = Child2(99)
# c.hello_world()           # Hello World
# c.google()                # Executing Child2 Google
# c.apple()                 # Executing Parent Apple           # Executing Child2 Google
# print(Child2.__mro__)     # (<class '__main__.Child2'>, <class '__main__.Parent'>, <class 'object'>)
# print(c.__class__.__mro__)#

# ---------------------------------------------------------------------------------------------------------------------
#   >> Child.__mro__ => Method Resolution Order
#   >> super()       => It is a function used to access parent class attributes(attributes can be method, variables etc)
# ---------------------------------------------------------------------------------------------------------------------


# Child adding extra functionality and reusing the original functionality of the parent class


# class Child3(Parent):
#     def google(self):
#         super().google()
#         print(f"Executing child3 Google !!!, {self.value}")
#
#
# c = Child3(101)
# c.google()        # Executing Parent Google 101       # Executing child3 Google !!!, 101
# c.apple()         # Executing Parent Apple    #Executing Parent Google 101       # Executing child3 Google !!!, 101
# print(Child3.__mro__)        #
# print(c.__class__.__mro__)   #

# Child class having an extra attribute (Adding a new Attribute)


# class Child4(Parent):
#     def __init__(self, value, name):
#         self.name = name
#         super().__init__(value)                         # calling parent class constructor
#
#
# c = Child4(734, "Python")
# print(c.name)           # Python
# print(c.value)          # 734


# Child inheriting from more than one parents


# class Facebook:                             # Parent2
#     def spam(self):
#         print("Executing Facebook Spam")
#
#
# class Child5(Parent, Facebook):
#     pass
#
#
# c = Child5(496)
# c.spam()            # Executing Facebook Spam
# c.google()          # Executing Parent Google 496
# c.apple()           # Executing Parent Apple        # Executing Parent Google 496
# print(Child5.__mro__)
# (<class '__main__.Child5'>, <class '__main__.Parent'>, <class '__main__.Facebook'>, <class 'object'>)
# print(c.__class__.__mro__)
# (<class '__main__.Child5'>, <class '__main__.Parent'>, <class '__main__.Facebook'>, <class 'object'>)


# Advanced Inheritance


# class Parent:
#     def spam(self):
#         print("Parent Spam")
#
#
# class Child1(Parent):
#     def spam(self):
#         print("Child1 Spam")
#         super().spam()
#
#
# class Child2(Parent):
#     def spam(self):
#         print("Child2 Spam")
#         super().spam()
#

# c1 = Child1()
# c1.spam()           # Child1 Spam       # Parent Spam

# c2 = Child2()
# c2.spam()           # Child2 Spam       # Parent Spam


# Multiple Inheritance


# class Child3(Child1, Child2):
#     pass
#
#
# c3 = Child3()
# c3.spam()       # Child1 Spam   # Child2 Spam   # Parent Spam
# print(Child3.__mro__)
# #(<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Child2'>, <class '__main__.Parent'>,
# <class 'object'>)
#
# print(c3.__class__.__mro__)
# # (<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Child2'>, <class '__main__.Parent'>,
# <class 'object'>)


class Parent:
    def demo(self):
        print("Class Parent Demo")


class Demo(Parent):
    def demo(self):
        print("Class Demo demo")
        super().demo()


class Spam(Parent):
    def demo(self):
        print("Class Spam demo")
        super().demo()


class Child1(Spam, Demo):        # order matters
    pass


c1 = Child1()
c1.demo()           # Class Spam demo   # Class Demo demo   # Class Parent Demo
print(Child1.__mro__)
# (<class '__main__.Child1'>, <class '__main__.Spam'>, <class '__main__.Demo'>, <class '__main__.Parent'>,
# <class 'object'>)


class Child2(Demo, Spam):
    pass


c2 = Child2()
# c2.demo()           # Class Demo demo   # Class Spam demo   # Class Parent Demo
# print(c2.__class__.__mro__)
# (<class '__main__.Child2'>, <class '__main__.Demo'>, <class '__main__.Spam'>, <class '__main__.Parent'>,
# <class 'object'>)



# Multi-level inheritance


# class A:
#     def demo(self):
#         print("Class A Demo")
#
#
# class B(A):
#     def demo(self):
#         print("Class B Demo")
#         super().demo()
#
#
# class C(B):
#     def demo(self):
#         print("Class C Demo")
#         super().demo()


# a = A()
# a.demo()        # Class A Demo      #

# b = B()
# b.demo()        # Class B Demo       # Class A Demo
#
# c1 = C()
# c1.demo()       # Class C Demo           # Class B Demo     # Class A Demo


# Overriding Class variables


# class Spam:
#     a = 10
#
#     def apple(self):
#         print("class Apple", self.__class__.a)
#
#
# class Apple(Spam):
#     a = 20      # Override the value of class variable "a" in parent class
#
#     def google(self):
#         print('google')


