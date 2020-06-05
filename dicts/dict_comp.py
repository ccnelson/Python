

# from keys
x = dict.fromkeys(range(1, 11), True)
print(x)

# from range
y = {k: k for k in range(10)}
print(y)

# from iterable
iterab = list("01234567")
d = {(key, value) for (key, value) in zip(range(8), iterab)}
print(d)

# odered from iterable
string = "hello"
dict = {}
for i, j in enumerate(string):
    dict[i] = j
print(dict)
