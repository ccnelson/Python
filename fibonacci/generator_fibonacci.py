def fib(m):
    a, b = 0, 1
    while a < m:
        yield a
        a, b = b, a + b

upto = 10000000000000000000000000000000000000000000000000000000000000000

gen = fib(upto)

for i in range(upto):
    try:
        print(next(gen))
    except:
        break
