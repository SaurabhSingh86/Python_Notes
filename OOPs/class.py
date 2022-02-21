"""
1. A Class is collection/set of functions that carry out various operations o instances.
2. Instances are the actual objects/data that your function manipulate on.
"""

# Employee Class

# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#
# emp1 = Employee("Steve", "Jobs", 10000)
# emp2 = Employee("Bill", "Gates", 20000)


# print(Employee)             # => <class '__main__.Employee'>

# print(dir(emp1))            # ['__class__', '__delattr__', '__dict__', '__dir__', ......] => Attributes of emp1
# print(dir(emp2))            # ['__class__', '__delattr__', '__dict__', '__dir__', ......] => Attributes of emp1

# print(emp1.__dict__)        # {'first_name': 'Steve', 'last_name': 'Jobs', 'salary': 10000}
# print(emp2.__dict__)        # {'first_name': 'Bill', 'last_name': 'Gates', 'salary': 20000}
# Notations :-

""""
1. __init__             =>      to save/store the data,
                                constructor
                                special method
                                initiation
                                creating dictionary
                        
2. self                 =>      data

3. local variables      =>      fname, lname, pay

4. instance variable    =>      self.fname
                                self.lame
                                self.salary
                                
5. Instance method      =>      def email(self):

6. __main__             =>      it specifies user-defined class
"""


# -------------------------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def email(self):
#         return f'{self.first_name}.{self.last_name}@company.com'
#
#
# emp1 = Employee("Elon", "Musk", 35000)
# emp2 = Employee("Jeff", "Bezos", 22000)
#
# print(emp1.__dict__)                    # {'first_name': 'Elon', 'last_name': 'Musk', 'salary': 35000}
# print(emp2.__dict__)                    # {'first_name': 'Jeff', 'last_name': 'Bezos', 'salary': 22000}
#
# print(emp1.__dict__["first_name"])      # Elon
# print(emp1.__dict__["last_name"])       # Musk
# print(emp2.__dict__["first_name"])      # Jeff
# emp2.__dict__["first_name"] = "JEFF"
# print(emp2.__dict__["first_name"])      # JEFF
# print(emp2.__dict__["salary"])          # 22000


# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def email(self):
#         return f'{self.first_name}.{self.last_name}@company.com'
#
#     def pay_hike(self, percent_hike):
#         hike_amount = self.salary * percent_hike
#         self.salary = self.salary + hike_amount
#         return self.salary
#
#
# emp1 = Employee("Elon", "Musk", 10000)
# emp2 = Employee("Jeff", "Bezos", 20000)
#
# print(emp1.__dict__)                    # {'first_name': 'Elon', 'last_name': 'Musk', 'salary': 10000}
# print(emp2.__dict__)                    # {'first_name': 'Jeff', 'last_name': 'Bezos', 'salary': 20000}
#
# emp1.pay_hike(.10)
# print(emp1.salary)                      # 11000
# emp2.pay_hike(.20)
# print(emp2.salary)                      # 24000.1
#
# print(emp1.__dict__)                    # {'first_name': 'Elon', 'last_name': 'Musk', 'salary': 11000.0}
# print(emp2.__dict__)                    # {'first_name': 'Jeff', 'last_name': 'Bezos', 'salary': 24000.0}


# ---------------------------------------------------------------------------------------------------------------

# class Calculator:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
#
# c1 = Calculator(1, 2)
# c2 = Calculator(20, 2)
#
# print(c1.add())
# print(c1.sub())
# print(c1.mul())
# print(c2.sub())
# print(c2.div())
# print(c2.mul())


# -------------------------------------------------------------------------------------------------------------------
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#
#
# p1 = Point(1, 2)
# p2 = Point(10, 20)
#
# print(p1.__dict__)                  # {'a': 1, 'b': 2}
# print(p2.__dict__)                  # {'a': 10, 'b': 20}


# -------------------------------------------------------------------------------------------------------------------
# class Player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def attack(self, point):
#         self.health -= point
#
#
# p1 = Player(1, 2)
# p2 = Player(3, 4)
#
# print(p1.__dict__)              # {'x': 1, 'y': 2, 'health': 100}
# print(p2.__dict__)              # {'x': 3, 'y': 4, 'health': 100}
#
# print(p1.__class__.__dict__)    # {'__module__': '__main__', '__init__': <function Player.__init__ at 0x000002.....}
# # or
# print(Player.__dict__)          # {'__module__': '__main__', '__init__': <function Player.__init__ at 0x000002.....}

# -------------------------------------------------------------------------------------------------------------------
# by default value
class Point:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b


p1 = Point()
p2 = Point()


# -------------------------------------------------------------------------------------------------------------------
# *args
# class Employee:
#     def __init__(self, fname, lname, pay, *args, **kwargs):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#         self.args = args
#         self.kwargs = kwargs
#
#
# emp1 = Employee("Ratan", "Tata", 250000, "Industrialist", age=50, county="India")

# print(emp1.__dict__) {'first_name': 'Ratan', 'last_name': 'Tata', 'salary': 250000, 'args': ('Industrialist',),
# 'kwargs': {'age': 50, 'county': 'India'}}


# ------------------------------------------------------------------------------------------------------------------

class Users:
    def __init__(self, users=None):
        self._users = []
        if users:
            for user in users:
                self._users.append(user)

    def append(self, username):
        self._users.append(username)


