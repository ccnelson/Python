from copy import deepcopy

#create new list instead of link to copied one
#ie you can edit both lists later and they
#are independant

list_1 = ['1', '1', '2']
list_2 = []
list_2 = deepcopy(list_1)

print(list_1)
print(list_2)

list_1[1] = '8'
list_2[1] = '0'

print(list_1)
print(list_2)

# alternatively, use list() to build new list

y = ["1", "2", "3", "4"]
x = list(y)
x[2] = "test"
print(y)
print(x)
