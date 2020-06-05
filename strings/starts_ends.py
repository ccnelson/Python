
x = 'Hello'

print(x.startswith('H'))
print(x.endswith('o'))
print(x.startswith('X'))

print("Press (c) to continue")
z = input()
while z.startswith('c'):
    print("Press (c) to continue")
    z = input()