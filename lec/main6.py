# ------------------oops--------------\
# jaroori nhi ki class capital word se start ho in python , small se bhi kr skte h but other programming lang me capital 
# class Factory():
#     a = 12

#     def hello(self):
#         print("how")
   

# to access class things
# print(Factory().a)

# Factory().hello()

# object
# has all the powers that class has 
# obj = Factory()
# print(obj.a)
# obj.hello()

# constructor - -----------

# self - ek location ko target krta h, location ko capture krne k liiye 
# class Factory:
#     def __init__(self,material,pockets):
#         self.material = material
#         self.pockets = pockets
#     def show(self):
#         print(f"your object details are {self.material} and {self.pockets}")

# reebok = Factory("leather",3)
# # print(reebok.pockets)
# reebok.show()

# ----types of attribut in class
# class att - normal att
# instance att - like self.name

#  ----types of methods in class
# instance method - using self like above one
# class method - use @classmethod and takes cls as their param , works with class itself

# self jo h object ki location ko target krta h
# while cls h woh class ki location ko krta h like we can not use cls.age...
# static method - @staticmethod, it does need any param like self or cls , also doest not locate class or object

# class Animal:
#     name = 'lion'
#     def __init__(self,age):
#         self.age = age
#     def show(self):
#         print("hello ")

#     @classmethod
#     def hello(cls):
#         print("i am lion")

#     @staticmethod
#     def static():
#         print("How are you kjdfkljdsl")


# obj = Animal(12)
# obj.static()


# inheritance -----------
# class to inherit props and behaviours from parent
# 

# class Factory():
#     a = "i am attri inside parent factory"
#     def hello(self):
#         print("i am a method and inside parent class factory")

# # child class - can access things of parent
# class FactoryUdaipur(Factory):
#     pass



# obj = FactoryUdaipur()
# # print(obj.a)



# class Animal:
    
#     def __init__(self,age):
#         self.age = age
#     def show(self):
#         print(f"hello animal {self.age}")

#     @classmethod
#     def hello(cls):
#         print("i am lion")

#     @staticmethod
#     def static():
#         print("How are you kjdfkljdsl")

# class Human(Animal):
#     def __init__(self,age,name):
#         super().__init__(age)
#         self.name = name
#     def show(self):
#         print(f"hello animal {self.name},{self.age}")

# obj = Animal(12)
# obj2 = Human(12,"kjlk")
# obj2.show()

# -multilevel inheritence

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
    

# class UFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color

# class MFactory(UFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# in python overloading does not exist , the other method will just overwrit the prev one
#method overriding in python

class Animal:
    def show(self):
        print("1self")


class Human(Animal):
    def show(self):
        print("ji bolo")

# how can we access both and do not override
# 

# access modifiers - public till now were
# protected = _a = 18,just putting underscore in variable or mehtods , but it has no use in python it works as same as public
# private - double underscore __a

# class F:
#     __a = 12

#     def show(self):
#         print(F.__a)

# obj = F()
# obj.show()

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    def area(self):
        pass

# they will make it necessary/rules that perimeter and area should be there in classes without them the classes will not work

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side
#     def perimeter(self):
#         print("it is imp")
    
#     def area(self):
#         print("it is imp ")

# dunder methods - special methods that start and end with double underscores , automat. get call when we perform actions e.g
# __init__, __str__



# class Square:
#     def __init__(self,side):
#         self.side = side
#     def __str__(self):
#         return f"my side is {self.side}"
#     def __add__(self,other):
#         return f"sum of side is {self.side+other.side}"

    

# obj = Square(12)
# obj2 = Square(14)

# # print(obj)
# print(obj+obj2)

# decorator-------------
# @property - even if we do this obj.show - will work
# creating our own decorator

# def decorate(func):
#     def wrapper():
#         print("i will print myself before the function hello ")
#         func()
#         print("i will print after")
#     return wrapper

# @decorate
# def hello():
#     print("hello ")

# hello()

# --------args and kwargs ------
# args - jitne arg dene h dedo uses '*'


# def addition(*args):
#     sum =0
#     for i in args:
#         sum +=i
#     print(sum)

# addition(1,23,3,4,57,2,1,4,6,7,4234,6,6)
# kwargs - keyword and args like dictionary  use '**'

# def info(**kwargs):
    
#     for i in kwargs:
#         print(f"{i}:{kwargs[i]}")
   
# info(name = "piyush",desgignation="nothing")

# list comprehension-------------------

# we can write list , set, dict, if-else statements in one line

# l = [i for i in range(1,21) if i%2 == 0]
# print(l)
 
# #  dic comp
# d = {i: i**2 for i in range(1,10)}
# print(d)

# lambda function - an anonymus function,inline defined using lambda keyword used for short func ,used only once or temp
# can have multip arg but one expression

# add = lambda a,b : a+b
# print(add(12,12))


# map--------------
# takes two things - function- lambda or normal , a DS list ,dict
# a = [1,2,3,4,5,5]
# result = map(lambda x:x**2,a)

# print(list(result))

# filter ----------
# def even(x):
#     if x%2 ==0:
#         return True
#     else:
#         return False

# a = [12,24,35,7]
# result = filter(even,a)
# print(list(result))


# modules and packages ---------------
