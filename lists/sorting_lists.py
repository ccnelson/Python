
fruits = ['grape', 'raspberry', 'apple', 'banana']

print("original")
print(fruits)

print("sorted (default alphabetical)") # returns new list
print(sorted(fruits))

print("original is unchanged")
print(fruits)

print("sorted reverse") # returns new list
print(sorted(fruits, reverse=True))
print("sorted by length")
print(sorted(fruits, key=len))
print("sorted by length reversed")
print(sorted(fruits, key=len, reverse=True))
print("original")
print(fruits)

print("sorted in place (original is changed)") # sorts list in place. no new list
fruits.sort()
print(fruits)
