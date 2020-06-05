
# import profile
import cProfile


def func():
    string = ""
    for i in range(1000):
        string += str(i)
    return string

#x = func()
#print(x)


cProfile.run('func()')

