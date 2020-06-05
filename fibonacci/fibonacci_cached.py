# caches each result in dictionary
# uses recursion to check if dictionary
# has answer each time
##################################################
#                   NOTE
# using this method on fibonacci numbers
# over #950th position (too many digits to count)
# only works if you build up to them, otherwise
# recursion depth limit is reached
##################################################


fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

#for n in range(1, 9500):
#    print(n, ":", fibonacci(n))

for i in range(1, 51): # calculates ratio between values
    print(fibonacci(i+1) / fibonacci(i))

n = 950
print(n, ":", fibonacci(n))
