# class demo:
#     a = 100         # static variable/class variable
#
#     def __init__(self):         # constructor
#         demo.b = 200
#
#     def m1(self):               # isntance method
#         self.c = 30
#         return self.c
#         # print(demo.c)
#
#     @classmethod
#     def m2(cls):                # class method
#         cls.d = 400             # class variable
#         # demo.e = 500
#         return cls.d
#         # return demo.e
#
#     @staticmethod
#     def m3():                   # static method
#         demo.f = 50
#
#
# # print(demo.__dict__)
# s = demo()
# # print(demo.__dict__)
# # s.m1()
# # s.m2()
# # s.m3()
# # print(demo.__dict__)
# # demo.g = 600
# # print(demo.__dict__)
# # print(demo.a)
# # print(demo.m1(s))
#
# print(demo.m2(demo))



