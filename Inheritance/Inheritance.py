class Parent:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f'Executing Parent Google {self.value}')

    def apple(self):
        print(f'Executing Parent Apple')
        self.google()


# Child class having a separate method (or Completely Independent Method)


class Child(Parent):
    def demo(self):
        print("Executing Demo")


# c = Child(100)
# c.demo()                  # Executing Demo
# c.google()                # Executing Parent Google 100
# c.apple()                 # Executing Parent Apple     # Executing Parent Google 100
#
# print(Child.__mro__)      # (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)
# print(c.__class__.__mro__)  # (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)


# child overriding parent class method


class Child2(Parent):
    def hello_world(self):
        print("Hello World")

    def google(self):
        print("Executing Child2 Google")


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


class Child3(Parent):
    def google(self):
        super().google()
        print(f"Executing child3 Google !!!, {self.value}")


# c = Child3(101)
# c.google()        # Executing Parent Google 101       # Executing child3 Google !!!, 101
# c.apple()         # Executing Parent Apple    #Executing Parent Google 101       # Executing child3 Google !!!, 101
# print(Child3.__mro__)        #
# print(c.__class__.__mro__)   #

# Child class having an extra attribute (Adding a new Attribute)


class Child4(Parent):
    def __init__(self, value, name):
        self.name = name
        super().__init__(value)                         # calling parent class constructor


# c = Child4(734, "Python")
# print(c.name)           # Python
# print(c.value)          # 734


# Child inheriting from more than one parents


class Facebook:                             # Parent2
    def spam(self):
        print("Executing Facebook Spam")


class Child5(Parent, Facebook):
    pass


# c = Child5(496)
# c.spam()            # Executing Facebook Spam
# c.apple()           # Executing Parent Apple        # Executing Parent Google 496



