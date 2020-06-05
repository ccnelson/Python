
import timeit
import functools


def my_func(A, B):
    print(A)
    print(B)


t = timeit.Timer(functools.partial(my_func, "this", "that"))
print(t.timeit(5))
