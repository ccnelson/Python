
import timeit


def the_func():
    x = "-".join(str(n) for n in range(100))
    print(x)


y = timeit.timeit(the_func,number=1000)

print(y)


