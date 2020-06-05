x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# allows changes to x in inner section to change x in outer section
# incidently youd use global to get to the global one
