
##### regular #####

def f(x):
    return 3*x + 1

print(f(2))

##################

## lambda ## (aka anonymous functions)

g = lambda x: 3*x + 1

print(g(2))

#### other examples ##

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("  leonarD", "EULER"))

##################

h = lambda : print("Howdy")

h()

#################      

names =	['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)
