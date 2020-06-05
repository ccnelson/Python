
import random as r
import timeit

def mutA(): # mid
    g = list("1234567")
    x = r.sample(population=g, k=2)
    a, b = g.index(x[0]), g.index(x[1])
    g[a], g[b] = g[b], g[a]

def mutB(): # fastest
    g = list("1234567")
    numA = r.randrange(len(g))
    numB = r.randrange(len(g))
    while numA == numB:
        numB = r.randrange(len(g))    
    g[numA], g[numB] = g[numB], g[numA]
    
def mutC(): # slowest
    g = list("1234567")
    x = r.sample(range(len(g)), 2)
    g[x[0]], g[x[1]] = g[x[1]], g[x[0]]

def mutD(): # 2nd fastest 
    g = list("1234567")
    h = list(g)
    numA = g.pop(r.randrange(len(g)))
    numB = g.pop(r.randrange(len(g)))
    a = h.index(numA)
    b = h.index(numB)
    h[a], h[b] = h[b], h[a]


print("mutA: ", timeit.timeit(mutA, number=1000))
print("mutB: ", timeit.timeit(mutB, number=1000))
print("mutC: ", timeit.timeit(mutC, number=1000))
print("mutD: ", timeit.timeit(mutD, number=1000))



