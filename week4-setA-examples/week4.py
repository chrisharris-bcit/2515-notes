# from my_package import my_module
import my_package.my_module as mod

result = mod.add([25, 15])
print(result)

# pytest looks for a folder called tests
# any files whose name starts with test_ will be run automatically

# for a non-relative import (i.e. a package that is not in the same folder as this script)
# in .bashrc
# export PATH='/home/chris/packages:$PATH'

# 
# def f(*a):
#     print(a)   # tuple of arguments e.g. (1, 2, 3, ...)

# f()
# f(1, 2)
# f(1, 2, 3, 4, 'Alex')

# def g(p1, p2):
#     print(p1, p2)

# def g(**a):  # * means arguments, ** means keyword args
# def g(*args, **kwargs):
#     print(args, kwargs) # kwargs is { 'p1': 10, 'p2': 20 }

# g(p1 = 10, p2 = 20)
# g(p2 = 20, p1 = 10)