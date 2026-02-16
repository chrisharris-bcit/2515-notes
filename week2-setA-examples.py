"""
Week 2 - Modules, Packages, Imports, Recursion 

Review

course = {}
course['name'] = 'ACIT1515'  
# square bracket notation to read/write values in dict
# different from list in that we use a string key instead of numeric

What data types can you loop through?
for v in x:

x could be list, string, tuple, dict

schools = ['BCIT', 'UBC', 'SFU']
schools[1]

num = 0
print(schools[num])
num = 1
print(schools[num])

# return keyword
1. sends a value back to where the function was called

def f(a, b):
    return 'value'

x = f()

def print_formatted(s):
    print(f'{s.upper()}')

print(print_formatted('tom')) # prints TOM, then None

result = print_formatted('tom')
print(result)   # prints None

print(print('Hello'))  # prints Hello, then None
print(None)

Argparse - python library for allowing you to pass arguments to a script in the command-line

    NOTE: similar to sys.argv

    python3 lab1.py
    python3 lab1.py test.txt test2.txt test3.txt
    python3 lab1.py --filename test.txt --db ...

    ssh-keygen -t ed25519 -C "ssomething@something.ca" -f do
"""
# import argparse

# parser = argparse.ArgumentParser(description='This script opens files and stores the data into a database') 
# # create the parser object

# # add arguments (flags)    -f --filename

# # positional argument     python3 script.py test1.txt test2.txt
# parser.add_argument('filename', type=str)
# # parser.add_argument('-f', '--filename', type=str)

# args = parser.parse_args() # grab the arguments, if defined by the user

# if args.filename:
#     print(f'The argument {args.filename} was passed')


"""
Debugging

Whenever you start working on a lab, create a folder and open the folder in VSCode using 
    code folder_name

To use the debugger, click the Run and Debug icon in the left-hand menu
    click 'create a launch.json file'
    Choose Python Debugger
    Choose either Python File or Python with Arguments (if you are using argparse or sys.argv)
    Save launch.json file
    Click the play button **in the debug window**

Add breakpoints (if necessary) by clicking a line to the left of the line-number

Run the script (using the play button in the Run and Debug pane)
Then step through/continue your breakpoints using the floating toolbar
"""
# print('End of script')

"""
Modules

    In Python, a 'module' is just a .py file with functions and declarations
    that gets imported into a script (a 'script' is an application)

        import assignments
        # When you import, the Python interpreter is going to look for a file of the same name. import assignments -> assignments.py. import courses -> courses.py

        import assignments as alib
        # allows you to use the module using a shorter/different name

    Modules are not meant to be run as a 'script'
        i.e.    python3 assignments.py

    assignments.py
        make_folder


    When you import a module, all of the contents of the module are available via the name of the import

    Assuming we have a file called courses.py, that has two functions
        get_courses
        choose_course

    import courses

    courses.get_courses()
    courses.choose_course()

    Imports can be relative
        [lab]
            [lib]
                assignments.py
                courses.py
            [src]
                main.py

    or we can place the modules anywhere in our filesystem and then import them via the PYTHONPATH

        [home]
            [you]
                [modules]
                    assignments.py
                    courses.py

    add to your .bashrc or .zshrc file in your home folder
    export PYTHONPATH="/home/you/modules:$PYTHONPATH"


    Packages - a collection (folder) of modules

        [python_helper]
            __init__.py
            assignments.py
            courses.py

    The __init__.py file is a special file that tells Python that the folder is a package

        - It is run automatically when a package is imported
        - It can run setup code if needed (rarely needed)
        - It can define per-package global variables (rarely needed)

            import python_helper

            python_helper.assignments
            python_helper.courses.get_course

"""

"""
Recursion - A function that calls itself
"""

# def looping(s):
#     print(s)
#     looping(s)

# looping('test') # maximum recursion depth exceeded, 'stack overflow' - the stack runs out of room and the program crashes

"""
NOTE: any function that is called in a python script is put onto a 'stack' - a LIFO (last-in, first-out) data structure
"""

"""
Simple recursion example

To write a recursive function we need to:
1. Determine the 'base case' - i.e. how does it stop calling itself
2. Determine the recursive case - i.e. what does the function when it calls itself
"""
def countdown(num):
    print(num)

    # base case - when num is 1, we're done
    if num == 1: 
        return
    else:
        # recursive case - call countdown
        countdown(num - 1)


countdown(10)  # 10 9 8 7 .. 1 then stop

# !5 -> 5 * 4 * 3 * 2 * 1
# !6 -> 6 * 5 * 4 * 3 * 2 * 1
# !6 -> 6 * !5
def factorial(n):
    # base case
    if n == 1:
        return 1
    
    # recursive
    return n * factorial(n - 1)

result = factorial(6)

"""
STACK
factorial(1)    -->  returns 1
factorial(2)    -->  2
factorial(3)    -->  6
factorial(4)    -->  24
factorial(5)    -->  120
factorial(6)    -->  720
"""




# demo: traceroute is a command-line utility that tells you the route from your machine to a server
# google.com