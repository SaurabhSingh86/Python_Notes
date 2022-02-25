# class A:
#     def __init__(self):
#         self._internal = 0          # An iternal/Private attribute
#         self.public = 1             # A public attribute
#
#     def public_method(self):
#         print("Public Method")
#         return self._internal
#
#     def _private_method(self):
#         print("Internal Method")
#
#
# class Spam:
#     def __init__(self, text):
#         self.text = text
#
#     def _clean_up(self):
#         return text.strip()
#
#     def split_text(self):
#         temp = self._clean_up(self.text)
#         return temp.split()
#
#     def get_len(self):
#         temp = self._clean_up(self.text)
#         return len(temp)

# ----------------------------------------------------------------------------------------------------------------
# ====>> setters & getters

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @property
#     def radius(self, value):
#         if not isintance(value, int):
#             raise TypeError()
#         self._radius = value
#
#     @property
#     def circumference(self):
#         return self._radius * 3.14 * 2


