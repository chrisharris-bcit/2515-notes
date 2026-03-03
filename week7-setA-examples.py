"""

1.  Passing functions as arguments
    Return values

"""

def apply(func, x, y):
    # assume f is a function
    # x and y are integers
    return func(x, y)

def f(a, b):
    return a + b

def g(a, b):
    return a - b

result = apply(f, 10, 5)
result = apply(g, 10, 5)

"""

2. Decorators

"""

# write a function called say_hello that takes one parameter (name) and returns a string 
# 'Hello, <name>'

# write a decorator called format that lowercases the output of any function, then apply it to say hello

def format(func):
    def inner(*args, **kwargs):
        return func(*args).lower() # unpacking the tuple
    return inner
        
@format
def say_hello(name):
    return f'Hello {name}'

say_hello('Paul')   # format decorator wraps say_hello
                    # when you call say_hello, format is called (say_hello is inside format)

"""

4. pytest

"""

def add(a, b):
    return a + b

# write a pytest test (function) that tests the add function with 10 and 20 and 
# asserts that the result is 30

def test_add():
    result = add(10, 20)
    assert result == 30

"""

5. pytest runs in two stages

    1. collects the tests
        search for tests/ folder
        search for files that start with test_
        imports all functions

    2. runs the tests
        run the test functions
        check results
        report results

"""

"""

Midterm - no OOP
Topics:
    UV?
    Recursion, Modules, Packages, Imports
    Functions
    Argument Passing
    Decorators
    Exceptions
    Pytest and Fixtures 

Rules:
    - You cannot be more than 1/2 hour late
    - You cannot leave the room for the first half hour
    - No music
    - No phones, laptops, smart glasses, etc.
    - Tuesday 12pm - 2 hours
    - Cheatsheet
    - Bonus Marks

"""

# sum takes a list of ints and returns the sum
# def sum(nums):    

# product takes a list of ints and returns the product     
# def product(nums):

@pytest.fixture
def data():
    return [1, 2, 3, 4, 5]

def test_sum(data):
    result = sum(data) # data IS [1, 2, 3, 4, 5]
    assert result == 15

def test_product(data):
    result = product(data) # data IS [1, 2, 3, 4, 5]
    assert result == 120


"""
26

[2, 7, 11, 15]
[2, 7, 3, 21, 11, 15]

2 + 7
2 + 11
2 + 15
7 + 11
7 + 15
11 + 15

"""
my_list = [2, 7, 11, 15]
target = 26
solution = []  # [2, 3]
for i in range(my_list):
    for j in range(i + 1, my_list):
        if i + j == target:
            solution.append(i)
            solution.append(j)

# iter(), next()

grades = (100, 99, 80, 95)

grades_iter = iter(grades)
next(grades_iter) # 100
next(grades_iter) # 99