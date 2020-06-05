num = 1
words = "stuff"

print("A number %i and a string %s" % (num, words))

# or

print("A number %r and a string %r" % (num, words))
# r uses standard representation

# or

print("A number {} and a string {}".format(num, words))


# and

y = 300000000

print("{:,}".format(y))  # adds commas
