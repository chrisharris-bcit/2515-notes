"""
Inheritance (+ Multiple Inheritance)
ABC (Abstract Base Classes)
MRO (Method Resolution Order)
"""

# Inheritance - 'is-a' relationship between two classes

# Course (generic, represents a BCIT course)
# Flipped (specific, represents a particular type of BCIT course)
# Project e.g. ACIT 3900 (specific, represents a particular type of BCIT course)
# from random import randint

# class Course:
#     def __init__(self, title, num_credits, course_number, instructor, grade=0):
#         self.title = title
#         self.num_credits = num_credits 
#         self.course_number = course_number 
#         self.instructor = instructor
#         self.grade = grade

#     def submit_assignment(self, grade):
#         self.grade += randint(0, 100)

# # in Python, to create an inheritance between two classes, pass the 'parent' class after the class name
# # the 'child' class inherits (automatically includes) everything from the parent
# class ProjectCourse(Course):
#     def __init__(self, title, num_credits, course_number, instructor, client, grade=0):
#         # any properties that belong to the parent class need to passed to the parent constructor
#         # we can pass arguments to the parent constructor using super().__init__()
#         super().__init__(title, num_credits, course_number, instructor, grade)
#         self.client = client

#     def weekly_meeting(self, participants):
#         pass

# acit3900 = ProjectCourse('acit2515', 3, 98754, 'Chris', 0, 'BCIT Nursing')
# acit3900.submit_assignment() # part of Course, NOT Project Course


# # Multiple Inheritance - inheriting from multiple classes
# # Animal
# # Pets
# # Dog
# # Hedgehog
# class Animal:
#     def __init__(self, age, color, **kwargs):
#         super().__init__(kwargs)
#         self.age = age
#         self.color = color

# class Pet:
#     def __init__(self, name, **kwargs):
#         super().__init__(kwargs)
#         self.name = name

# # in Python you can inherit from multiple comma-separated classes
# class Hedgehog(Animal, Pet):
#     def __init__(self, age, color, name, num_spikes):
#         super().__init__(age, color, name)
#         self.num_spikes = num_spikes

# nick = Hedgehog(age=1, color='beige', name='Nick', num_spikes=50)

from abc import ABC, abstractmethod
"""
ABC - abstract base classes
(a type of inheritance that enforces behaviour)

An abstract base class declares placeholder methods that *have* to be implemented by classes that inherit the ABC
"""
class Account(ABC):
    # no init method, only has method definitions with no functionality

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# TypeError! deposit and withdraw
# class ChequingAccount(Account):
#     def __init__(self, balance=0):
#         self.balance = balance

class ChequingAccount(Account):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance = amount

account1 = ChequingAccount()
print(ChequingAccount.__mro__)

"""
MRO - Method Resolution Order
"""
# class A:
#     def __init__(self, x):
#         pass

#     def do_something():
#         print('A')

# class B():
#     pass

#     def do_something():
#         print('B')

# class C(A, B):


# test = C()
# test.do_something()
# """
# Q: how do you figure which version of the method is called?

# Use MRO -> inherited classes will be checked in order (and you can view the order by printing C.__mro__ to the console)

# A:  If C implements the method it is used
#     If C does not implement the method:
#         C inherits from A, B, so A will be tried first
#         If A doesn't contain the method, try B
#         etc.
# """
# print(C.__mro__)