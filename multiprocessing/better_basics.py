# tidied up

from multiprocessing import Process
import time


def bad_primes(n):
    for i in range(2, n):
        if n % i == 0:
            print("n:" + str(n) + " = false")
            return False
    print("n:" + str(n) + " = true")
    return True


if __name__ == '__main__':
    start = time.time()
    to_check = [15485863, 15485917, 15485933, 15485941]
    procs = []

    for i in to_check:
        procs.append(Process(target=bad_primes, args=(i,)))

    for k in procs:
        k.start()

    for m in procs:
        m.join()

    end = time.time()
    duration = end - start
    print(duration)