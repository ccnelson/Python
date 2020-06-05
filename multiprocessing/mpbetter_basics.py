# tidied up
# stores returned values in managed list

from multiprocessing import Process, Manager
import time


def bad_primes(n, L):
    for i in range(2, n):
        if n % i == 0:
            print("n:" + str(n) + " = false")
            return False
    L.append(n)
    print("n:" + str(n) + " = true")
    return True


if __name__ == '__main__':
    with Manager() as manager:
        L = manager.list()
        start = time.time()
        to_check = [15485863, 15485917, 15485933, 15485941]
        procs = []

        for i in to_check:
            procs.append(Process(target=bad_primes, args=(i, L)))

        for k in procs:
            k.start()

        for m in procs:
            m.join()

        end = time.time()
        duration = end - start
        print(duration)
        print(L)