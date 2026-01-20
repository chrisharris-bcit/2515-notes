"""
Marks for quiz, lab 1

Topics for today:
Decorators (functions)
UV - modern command-line alternative/replacement for pip
"""

# Functions can return values
def f():
    return 'ran f'

result = f()

# Functions can return values of any type
def g():
    return [1, 2, 3, 4]

def h():
    return { 'message': 'ran h' }

result = h()
# print(result['message'])

def j():
    # 1. a function can be declared inside another function
    # 2. a function that is declared inside another function is usually
    #       called an 'inner' function (but can be named anything)
    def k():
        return 'ran k'
    
    return k

result = j() # result is the return value of j
# result is k (the return value of j), a function
inner_result = result() # runs the 'result' function, which IS k
# print(inner_result)

# Decorators - shorthand way to modify an existing function by wrapping it in another function

def authenticate(func):
    # do something before we run func (whatever function is passed in)
    def inner():
        response = input('Please enter your password: ')
        if response == 'batman123456':
            return func()
        else:
            print('Incorrect password')
    return inner

@authenticate
def list_grades():
    return 'listing grades...'

def list_courses():
    return 'listing courses...'

def list_user_info():
    return 'listing user info...'

def list_instructor():
    return 'Tom'

options = {
    'list_courses': list_courses,
    'list_user_info': list_user_info,
    'list_grades': list_grades,
    'list_instructor': list_instructor
}

# menu = []
# for k, v in options.items():
#     menu.append(k.replace('_', ' ').title()) # e.g. List Courses

"""
Script - self-contained application in a .py file
Module - functions in a .py file that are imported into a script
Package - folder of modules with an __init__.py

If we want to define some functions that can be imported by another script
AND we want to also be able to run the same file as a script, 
we need the 'main guard'

__name__ is a special variable that the interpreter sets when running a file

if the file is a module that is being imported, __name__ is set to the name of the module 

If the file is a script, __name__ is set to __main__
"""
if __name__ == '__main__':
    # this is what the file should do if run as a script
    
    while True:
        # List Comprehension
        menu = [k.replace('_', ' ').title() for k, v in options.items()]
        
        # * 'unpacks' the sequence into separate values 
        print(*menu, sep='\n')

        response = input('Please choose an option: ')
        response = response.replace(' ', '_').lower()

        # List Courses -> list_courses
        if response in options.keys():
            print(options[response]())
            
"""
UV - modern command-line alternative/replacement for pip

uv
    lists all available commands and options

uv init
    create a project

uv add ______
    install a package

uv venv
"""