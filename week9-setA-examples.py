"""
Today:
Object-Oriented Python
Exercise
Lab

Next Week:
Go over exams in class
"""

# def upper(func):
#     def inner(*args, **kwargs):
#         print('')
#         result = func(*args)
#         print('')
#         return result.upper()

# @upper
# def greet(s):
#     return f'Hello {s}!'

# greet = upper(greet) # Correct, intended answer

# def greet(s):
#     return f'Hello {s}!'.upper()

"""
Object-Oriented Python

cwd = Path.cwd()   # Path is a class, cwd() is a method (function)

Dot Notation
any time you see a . you are using a class/object

example:
name = 'nathan '        # string object
name = name.trim()      # string object
name = name.upper()     # string object
OR
name.trim().upper()     # refers to two objects
name is a string (strings are objects)
name.trim() is a new string object

The thing that is to the left of the . is an object or class
The thing that is to the right of the . is either a property or a method
    property -> variable (that belongs to an object or class)
    method -> function (that belongs to an object or class)
"""

"""
Why use Object-Oriented approach?

Can't create an unknown number of dictionaries
Using dictionaries leads to maintenance problems
...
"""
headset = {
    'brand': 'Sony',
    'model': 'zxcvzxc',
    'price': 199.99,
    'color': 'black'
}
headset['price'] = 49.99

headset2 = {
    'brand': 'Apple',
    'model': 'qwer',
    'price': 999.99,
    'color': 'lightpink'
}
"""
Not object-oriented, but an alternative
"""
# constructor function
def init(brand, model, price, color):
    return {
        'brand': brand,
        'model': model,
        'price': price,
        'color': color
    }
headset1 = init('Sony', 'xzvxcvb', 199.99, 'black')
headset2 = init('Apple', 'asdf', 1999.99, 'beige')
"""
OOP approach

Class vs Object
class is the definition (i.e. blueprint)
objects are 'instances' of a class
"""
class Headset:
    # constructor - called automatically when we create an object
    # 'self' is required for most methods in a class
    def __init__(self, brand, model, price, color):
        # self is a reference to the object itself
        self.brand = brand  # self.brand is an object property, brand is var
        self.model = model
        self.price = price
        self.color = color

headset3 = Headset('Sony', 'zxcv', 199.99, 'black')
# headset3 is an object (an instance of Headset class)
print(headset3.brand) # use dot notation instead of []


"""
class variables vs instance variables
@property
@staticmethod
@classmethod
__str__
Enums
"""
# class Account:
#     def __init__(self, ccnum, balance=0.0):
#         self.ccnum = ccnum
#         self.balance = balance

#     # display the credit card with some numbers hidden
#     # getters and setters -> getter is a method that returns a value
#     #                     -> setter is a method that sets the value

#     def get_ccnum(self):
#         # return ccnum[:4] + 'xxxxxxxxxxxx'   DOESN'T WORK, no ccnum variable
#         return self.ccnum[:4] + 'xxxxxxxxxxxx'

# account1 = Account('2345345645675678')
# # print(account1.ccnum)
# print(account1.get_ccnum()) # prints 2345xxxxxxxxxxxx


class Account:
    def __init__(self, ccnum, balance=0.0):
        self._ccnum = ccnum
        self.balance = balance

    @property
    def ccnum(self):
        return self._ccnum[:4] + 'xxxxxxxxxxxx'
    
    @ccnum.setter
    def ccnum(self, newnum):
        if type(newnum) == str and len(newnum) == 16:
            self._ccnum = newnum
        else:
            raise ValueError

account4 = Account('2345345645675678')
# @property and @ccnum.setter cause the interpreter to run functions when regular reads (e.g. print(account4.ccnum)) and writes (e.g. account4.ccnum = ____) occur
print(account4.ccnum) # calls def ccnum(self), which formats the output
account4.ccnum = '4576234512342345' # calls def ccnum(self, newnum) which validates the new value
print(account4.ccnum)


"""
@staticmethods - static methods operate on the class itself, not objects
"""
class Math:
    PI = 3.14  # class variable

    @staticmethod
    def round(num):
        # without @staticmethod, self is going to be assigned to num
        pass

    @staticmethod
    def floor(num):
        # if you need to reference a class variable, use the class name, e.g. Math.PI
        pass

    @staticmethod
    def ceil(num):
        pass

# math1 = Math()
# math1.round(2.5)
Math.round(2.5)
print(Math.PI)

# NOTE: typically 'self' should be the first parameter for any object method
# why? because python automatically (implicitly) passes the reference into the function
# using the @staticmethod decorator, a reference to self is NOT implicitly passed to the function


"""
@classmethod - passes a reference to the class automatically instead of self

often used for multiple constructors (i.e. different ways to create an object from a class)



    
"""
class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def fromstring(cls, datestr):
        # extract numbers from the date string into variables x, y, and z
        # cls IS a reference to the class, not the object (self)

        # use @classmethod instead of referencing the class directly, Date(x, y, z) because it will work correctly later when we start using inheritance
        cls(x, y, z)

Date(2026, 3, 3)
Date.fromstring('...')

"""
Enums - human-readable constants that map values to names
"""
from enum import Enum

class AccountType(Enum):
    CHEQUING = "Chequing"
    SAVINGS = "Savings"
    INVESTMENT = "Investment"

class Account:
    def __init__(self, account_type, balance=0.0):
        self.account_type = account_type
        self.balance = balance

account5 = Account(AccountType.CHEQUING)
print(account5.account_type) # prints AccountType.CHEQUING
print(account5.account_type.value) # prints Chequing