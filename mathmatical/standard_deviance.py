# standard deviation =
# square root of variance

import statistics

listx = [1,2,3]

variance = statistics.pvariance(listx)

print("Variance: ", variance)

stan_dev = variance ** 0.5

print("Standard deviation: ", stan_dev)

