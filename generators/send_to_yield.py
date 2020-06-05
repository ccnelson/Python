
def score_tally():
    score = 0
    default = 0.5
    while True:
        incr = yield score # yield makes 'next' and 'send' available
        score += incr if incr is not None else default

gen = score_tally() # instantiate the generator!

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("")
print(gen.send(10)) # gets stored in incr
print("")
print(next(gen)) # doesnt send so incr is none
print(next(gen))
print(next(gen))
print(next(gen))
