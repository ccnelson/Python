
## multiple all numbers in a list

from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multiplier = lambda x, y : x * y
print(reduce(multiplier, data))

### heres the same in a for loop

product = 1
for x in data:
    product = product * x

print(product)

#### reduce only if you really need it
####  it takes a function with two arguments, and a sequence of data
#### reduce applies the function to the first two terms, next it will
#### apply the function to the output value, and the third piece of data.
#### it then repeats untill the end of sequence
