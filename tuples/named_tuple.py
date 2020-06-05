
from collections import namedtuple

Colour = namedtuple('Colour', ['hue', 'saturation', 'luminosity'])

p = Colour(170, 0.1, 0.6) # remember tuples are immutable

print(p)

if p.hue > 50:
    print('yes')

############# or ##############

print("\nsource for tuple creationn\n\n")

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=22)
print(p._source)

