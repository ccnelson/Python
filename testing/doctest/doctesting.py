"""
example module demonstrating doctests
doctest identifies the following tests:

>>> square_it(2)
4
>>> square_it(10)
100

"""

def square_it(n):
    x = n * n
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# run this from cmd line
# $ python doctesting.py -v
# (ommiting -v will provide no response upon successful test)


    
