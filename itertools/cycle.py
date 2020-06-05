import itertools

x = itertools.cycle('abcd')

for i in range(10):
    print(next(x))
