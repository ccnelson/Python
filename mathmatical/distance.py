
# quickest method yet
# takes 0.0001

import math
import time

genotype = [1, 2, 3]
locs = [(-10.0, 10.0), (10.0, 10.0), (10.0, -10.0), (-10.0, -10.0)]

def measure_dist(gene, loc):
    tdist = 0
    tdist += math.sqrt(((locs[0][0]-locs[1][0])**2)+((locs[0][1]-locs[1][1])**2))
    for i in gene:
        if i < len(gene):
            tdist += math.sqrt(((locs[i][0]-locs[i+1][0])**2)+((locs[i][1]-locs[i+1][1])**2))
        else:
            tdist += math.sqrt(((locs[i][0]-locs[0][0])**2)+((locs[i][1]-locs[0][1])**2))
    print(tdist)

start = time.perf_counter()
measure_dist(genotype, locs)
end = time.perf_counter()

dur = end - start

print(dur)
