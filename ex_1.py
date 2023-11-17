# def my_dec(func):
#     def wrapper():
#         print('before decorator')
#         func()
#         print('after decorator')
#     return wrapper
#
# @my_dec
# def hello():
#     print('Hello')
#
# hello()

# class Vector:
#
#     '''eirgheiruh'''
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#
#         if self.validate(x):
#             self.x = x
#
#         if self.validate(y):
#             self.y = y
#         print(Vector.norm2(self.x, self.y))
#         print(self.norm2(self.x, self.y))
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x ** 2 + y ** 3
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD < arg < cls.MAX_COORD
#
#
#
# v = Vector(1, 5)
# print(v.norm2(1, 8))
# print(v.__dict__)
# print(Vector.norm2(1, 8))

# from math import pi
#
# class Cylinder:
#
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return circle * 2 + side
#
#
#
#
#     def __init__(self, diam, high):
#         self.diam = diam
#         self.high = high
#         self.area = self.make_area(self.diam, self.high)
#
#     def __str__(self):
#         return f'diam = {self.diam}, high = {self.high}, area = {self.area}'
#
# c = Cylinder(2, 4)
# print(c)
# print(c.__dict__)

# class MyClass:
#
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1
#
#     @classmethod
#     def total_counts(cls):
#         print('total counts = ', cls.TOTAL_COUNTS)
#
#
#
# class ChildClass(MyClass):
#     TOTAL_COUNTS = 0
#
#     def __init__(self):
#         ChildClass.TOTAL_COUNTS += 1
#
#
#
#
#
# m = MyClass()
# m1 = MyClass()
# MyClass.total_counts()
# cc = ChildClass()
# cc.total_counts()

# class Snow:
#
#     def __init__(self, num):
#         self.num = num
#
#     def make_snow(self, el):
#         for i in range(self.num // el):
#             print('*' * el)
#         print('*' * (self.num % el))
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Snow)):
#             raise TypeError
#         res = other if isinstance(other, int) else other.num
#         return Snow(self.num + res)
#
# s = Snow(1000)
# s.make_snow(10)
# s2 = s + 10000
# s2.make_snow(200)


