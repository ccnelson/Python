# genetic module
# new tsp project
# C.NELSON 2019
# v0.1 updated 13/03
# Python 3.6
#################################

import turtle_func as tf
import numpy as np
import mutators as mu
import crossovers as co
import pandas as pd
import random


class Ind:
    def __init__(self, ind, switch, template=None, par1=None, par2=None):
        if switch == 1:
            self.genotype = np.array(np.random.permutation(template))
        elif switch == 2:
            self.genotype = crossover(par1, par2)
        self.index = ind
        self.distance = None
        self.score = None

    def to_dict(self):
        return {'genotype': self.genotype,
                'index': self.index,
                'distance': self.distance,
                'score': self.score, }

    def __repr__(self):
        return '\nG:%s|\nInd:%r|Dist:%r|Score:%r\n' % \
               (self.genotype, self.index, self.distance, self.score)


def crossover(par1, par2):  # this needs attention, cant have orphans
    child1, child2 = co.cross_over(par1, par2, 1)  # 0=random, 1=pbx, 2=obx, 3=pmx (1&2 seem best)  # todo : random crossover appears too random - algo runs 4 ever with stan dev increasing
    child1 = mu.mutation(child1, 6)  # 0=random, 1=dinv, 2=d, 3=ex, 4=ins, 5=inv, 6=shuf  # todo : mutation causes crashes - something to do with numpy
    # 2019 - where does mutations return value go??! # FIXED?
    return np.array(child1) # child 2 abandoned :'( fix this later


class Ga:
    def __init__(self, locations, parents=0, console_out=None, turt=None):
        # setup
        self.parents = parents
        self.no_of_locs = len(locations)
        self.geno_template = np.arange(1, self.no_of_locs)
        self.locations = locations
        self.no_in_population = self.no_of_locs * 8
        self.popu = []
        self.console_out = console_out
        self.turt = turt
        self.generation_no = 0
        self.population_df = None
        self.pop_dist_mean = None
        self.stan_dev = None
        self.par_selection = None

    def measure_distance(self, pop):
        for indi in pop:
            dist = 0
            for index, gene in enumerate(indi.genotype):
                if index == 0:
                    dist += np.linalg.norm(self.locations[0] - self.locations[gene])  # euclidean distance
                if index < (len(indi.genotype) - 1):  # -1 !arrays start from 0!
                    dist += np.linalg.norm(self.locations[gene] - self.locations[indi.genotype[index + 1]])
                if index == (len(indi.genotype) - 1):  # (no_of_location > len(indi.genotype))
                    dist += np.linalg.norm(self.locations[gene] - self.locations[0])
            indi.distance = dist

    def create_pop(self):
        # first gen
        if self.parents == 0:
            for i in range(self.no_in_population):
                self.popu.append(Ind(i, 1, template=self.geno_template))

    def start_algo(self):
        # start
        self.measure_distance(self.popu)
        self.population_df = pd.DataFrame([individual.to_dict() for individual in self.popu])
        self.pop_dist_mean = self.population_df['distance'].mean()
        self.population_df['score'] = self.population_df['distance'].apply(lambda x: 100 / (x / self.pop_dist_mean))
        self.stan_dev = self.population_df['score'].std()
        self.par_selection = self.population_df.nsmallest(4, 'distance')
        pd.set_option('max_columns', 7)
        pd.set_option('max_rows', 7)
        print(self.population_df)
        print(self.stan_dev)
        print(self.par_selection)

        while self.stan_dev > 1:
            if self.generation_no % 10 == 0:
            #    random.seed()
                np.random.seed()
            self.generation_no += 1
            self.popu = []
            self.population_df = []
            # new popu from parents
            for i in range(self.no_in_population):
                a = random.randrange(4)  # random parents
                b = random.randrange(4)
                while b == a:  # but not 2x the same
                    b = random.randrange(4)
                self.popu.append(Ind(i, 2, par1=self.par_selection['genotype'].iloc[a], par2=self.par_selection['genotype'].iloc[b]))
            # measure
            self.measure_distance(self.popu)
            # dataframe
            self.population_df = pd.DataFrame([individual.to_dict() for individual in self.popu])
            print(self.population_df)
            #input()
            # scores and stats
            self.pop_dist_mean = self.population_df['distance'].mean()
            self.population_df['score'] = self.population_df['distance'].apply(lambda x: 100 / (x / self.pop_dist_mean))
            self.stan_dev = self.population_df['score'].std()
            # choose parents
            self.par_selection = []
            self.par_selection = self.population_df.nsmallest(4, 'distance')
            # print progress
            print("\nPopulation:\n", self.population_df.to_string())
            print("\nParent selection:\n", self.par_selection.to_string())
            print("\nNew popu distance mean:\n", self.pop_dist_mean)
            print("generation:", self.generation_no)
            print("\nstand_dev:\n", self.stan_dev)
            #input()
            self.send_to_console(self.par_selection)
        tf.draw_coord(self.turt, self.locations, self.popu[0].genotype)


        # # tests
        self.send_to_console(self.population_df)
        self.send_to_console("\n")
        self.send_to_console(self.par_selection)
        #for j in self.popu:
        #    tf.draw_coord(self.turt, self.locations, j.genotype)

    def returnpop(self):
        return self.popu

    def returninfo(self):
        return """Population = %i\t\nNo of locations = %i """ % (self.no_in_population, self.no_of_locs)

    def send_to_console(self, content):
        self.console_out.insert('end', content)
        self.console_out.see('end')  # scroll to end

    def stop_ga(self):
        self.stan_dev = 0

# ga function should accept:
# 1. locations (first (zero) is home)
# 2. parents (optional)
# 3. parasitic parent X not yet
# 4. gui console out
#
# and return:
# 1. proposed solution
#
#

