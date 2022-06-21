from abc import ABC, abstractmethod     # abstractmethod is a decorator

# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#
#     def __init__(self):
#         self.length = 4
#         self.breadth = 10
#


# # before creating any object If I want to run then it'll execute properly
# # but if we create an object then I want to run then It'll give an Error
#
# rect1 = Rectangle()
# # TypeError: Can't instantiate abstract class Rectangle with abstract methods printarea
# # it means we must have to create one printarea() method then
# # it is compulsory to create a printarea() method if you are inheriting the properties of shape class inside the
# # rectagle class

# ------------------------------------------------------------------------------------------------------------------

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 10

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())            # 40
