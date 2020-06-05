class Test_1():
    def __init__(self):
        self.x = 1
        self.y = 2

class Test_2():
    def __init__(self):
        self.x = 1
        self.y = 2

one = Test_1()
two = Test_2()

########################
## this files classes ##

import sys
import inspect

current_module = sys.modules[__name__]

class_list = inspect.getmembers(current_module)

print(class_list[0][0])
print(class_list[1][0])
print()

###########################
## another files classes ##

import class_test_file

for name, obj in inspect.getmembers(class_test_file):
    if inspect.isclass(obj):
        print(name)

###########################



