
import math

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

print(list(map(area, radii)))

#### map applies the function (1st parameter) to the list (2nd parameter)
#### and returns an interable. This is passed to the list contrsuctor

### filter works in a similar fashion

import statistics

avg = statistics.mean(radii)
print(list(filter(lambda x: x > avg, radii)))

## this prints the values in radii, that are above average

## it can also be used to remove empty data

countries = ["", "Argentina", "", "Brazil", "Chile", "Columbia", ""]
print(list(filter(None, countries)))



