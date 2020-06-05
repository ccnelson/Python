##################################################
#                   NOTE
# using this method on fibonacci numbers
# over #330th position
# only works if you build up to them, otherwise
# recursion depth limit is reached
##################################################



from functools import lru_cache #least recently used cache

@lru_cache(maxsize = 1000) # default 128
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(330)) # maximum recursion reached above this 

#for i in range(1, 500): # but building up to it is fine
#    print(fibonacci(i))
