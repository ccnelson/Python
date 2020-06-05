
import random


random.seed(a=None, version=2)
# a=None    : system time / os randomisation sources
# version=2 : wider range of seeds


def randy():
    x = random.randrange(10)
    print(x)


randy()