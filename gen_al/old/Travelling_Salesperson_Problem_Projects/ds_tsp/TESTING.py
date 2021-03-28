import pandas as pd
import numpy as np
from scipy.spatial import distance

pd.set_option('display.max_colwidth', -1)  # wide output

# testing the main idea to vectorise distance measurement
# 1 locations ✓
# 2 chromosome ✓
# 3 phenotype ✓
# 4 phenotype translation ✓
# 5 distance calculations

# 1 LOCATIONS
no_of_locs = 5                                                            # number of destinations
locations = np.random.randint(low=-200, high=201, size=(no_of_locs, 2))     # actual coordinates
loc_indexes = np.arange(1, no_of_locs)                                      # 0 > no_of_locs
# 2 CHROMOSOME
genotype = np.array(np.random.permutation(loc_indexes))                     # a chromosome
# 3 PHENOTYPE
phenotype = np.concatenate(([0], genotype, [0]))                            # put a '0' in front and end
# 4 PHENOTYPE TRANSLATION
phenotype_list = [locations[n] for n in phenotype]                          # put coordinates in a list
phenotype_markup = np.array(phenotype_list)                                 # cast it into a numpy array (?doing it in 1 line returns a generator?)
# 5 DISTANCE CALCULATION
#dist = distance.pdist(phenotype_markup)
#dist = distance.euclidean(phenotype_markup)
#dist = np.linalg.norm(phenotype_markup, ord=('fro'))
#dist = distance.pdist(phenotype_markup, lambda u, v: np.sqrt(((u-v)**2).sum()))
#dist = np.apply_along_axis(np.linalg.norm, 0, phenotype_markup)
#dist = np.apply_along_axis(lambda row:np.linalg.norm(row), 1, phenotype_markup)
#dist = np.apply_along_axis(np.linalg.norm, 0, phenotype_markup)
#tot_dist = np.sum(dist)
                                                                            # TESING
print("loc_indexes", loc_indexes)                                           # print stuff
print("locations", locations)
print("genotype", genotype)
print("phenotype", phenotype)
print("phenotype_markup", phenotype_markup)
#print("distances", dist)
#print("total distance", tot_dist)


