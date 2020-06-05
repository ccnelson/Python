
import pandas as pd
import numpy as np
import scipy as sc


class Individual():
    def __init__(self, ind, switch, template=np.empty(0), par1=None, par2=None):
        if switch == 1:
            self.genotype = np.array(np.random.permutation(template))
        elif switch == 2:
            self.genotype = np.array(np.random.permutation(template))
            # self.genotype = crossover(par1, par2)
        self.phenotype = geno_to_pheno(self.genotype)
        self.index = ind
        self.distance = None
        self.score = None

    def to_dict(self):
        return {'genotype': self.genotype,
                'index': self.index,
                'distance': self.distance,
                'phenotype': self.phenotype,
                'score': self.score, }

    def __repr__(self):
        return 'Gene(geno:%r|pheno:%r|index:%r|dist:%r|score:%r)\n' % \
               (self.genotype, self.phenotype, self.index, self.distance, self.score)


def geno_to_pheno(geno):
    x = [0]
    tmp = np.concatenate((x, geno))
    tmp2 = np.concatenate((tmp, x))
    ### now we have zeroes at start and end, we can resolve them against
    ### the list of destinations
    y = []
    for i in tmp2:
        y.append(locations[i])
    z = np.array(y)
    #print("pheno: ", tmp2)
    #return tmp2
    return z

pd.set_option('display.max_colwidth', -1)

no_of_locations = 10
no_in_population = 5

locations = np.random.randint(low=-200, high=201, size=(no_of_locations, 2))
locations_df = pd.DataFrame(locations, columns=['x', 'y'])

print("locations:\n", locations_df)

chromo_template = np.arange(1, no_of_locations)

print("chromo template:\n", chromo_template)

population = []
for i in range(no_in_population):
    population.append(Individual(i, 1, template=chromo_template))

population_df = pd.DataFrame([individual.to_dict() for individual in population])

print("population:\n", population_df.to_string())

