############################################################
# C.NELSON 2018                                            #
# genetic algorithm for tsp permutation problem            #
# using numpy stack for vectorised distance calculations   #
# and fast stats via dataframes                            #
############################################################
import numpy as np
import pandas as pd
import crossovers as co
import mutators as mu
import random
import turtle_func as tf
import turtle
import time


class Ind():
    def __init__(self, ind, switch, template=np.empty(0), par1=None, par2=None):
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
        return 'Gene(geno:%r|Ind:%r|Dist:%r|Score:%r)\n' % \
               (self.genotype, self.index, self.distance, self.score)


class Datastore:
    locations = []


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def crossover(par1, par2):  # this needs attention, cant have orphans
    child1, child2 = co.cross_over(par1, par2, 0)  # 0=random, 1=pbx, 2=obx, 3=pmx (1&2 seem best)
    mu.mutation(child1, 0)  # 0=random, 1=dinv, 2=d, 3=ex, 4=ins, 5=inv, 6=shuf
    ### 2019 - where does mutations return value go??!
    return np.array(child1) # child 2 abandoned :'( fix this later


def measure_distance(pop):
    for indi in pop:
        dist = 0
        for index, gene in enumerate(indi.genotype):
            if index == 0:
                dist += np.linalg.norm(Datastore.locations[0] - Datastore.locations[gene])  # euclidean distance
            if index < (len(indi.genotype) - 1):  # -1 !arrays start from 0!
                dist += np.linalg.norm(Datastore.locations[gene] - Datastore.locations[indi.genotype[index+1]])
            if index == (len(indi.genotype) - 1):  # (no_of_location > len(indi.genotype))
                dist += np.linalg.norm(Datastore.locations[gene] - Datastore.locations[0])
        indi.distance = dist


def gen_algo():
    start = time.time()
    random.seed()
    np.random.seed()
    # turtle setup
    dave = turtle.Turtle()
    bob = turtle.Turtle()
    ts = dave.getscreen()
    turtle.setup(600, 500)
    ts.bgcolor('black')
    ts.tracer(0, 0)  # fast as you can pls turtles
    ts.title('tsp vectorised')
    dave.speed(0)
    tf.draw_grid(dave, 400)
    # main setup
    no_of_locations = 15
    no_in_population = no_of_locations * 8
    generation_no = 0
    Datastore.locations = np.random.randint(low=-200, high=201, size=(no_of_locations, 2))
    locations_df = pd.DataFrame(Datastore.locations, columns=['x', 'y'])
    print("\nLocations:\n", locations_df)
    # use turtle to illustrate points
    for i, loc in enumerate(Datastore.locations):
        dave.pu()
        tf.draw_point(dave, loc, i)
    geno_template = np.arange(1, no_of_locations)
    # first popu
    popu = []
    for i in range(no_in_population):
        popu.append(Ind(i, 1, template=geno_template))
    # measure
    measure_distance(popu)
    # dataframe
    population_df = pd.DataFrame([individual.to_dict() for individual in popu])
    # scores and stats
    pop_dist_mean = population_df['distance'].mean()
    population_df['score'] = population_df['distance'].apply(lambda x: 100 / (x / pop_dist_mean))
    stan_dev = population_df['score'].std()
    # choose parents
    par_selection = population_df.nsmallest(4, 'distance')
    # begin loop
    while stan_dev > 0:
        if generation_no % 10 == 0:
            random.seed()
            np.random.seed()
        generation_no += 1
        popu = []
        # new popu from parents
        for i in range(no_in_population):
            a = random.randrange(4)  # random parents
            b = random.randrange(4)
            while b == a:            # but not 2x the same
                b = random.randrange(4)
            popu.append(Ind(i, 2, par1=par_selection['genotype'].iloc[a], par2=par_selection['genotype'].iloc[b]))
        # measure
        measure_distance(popu)
        # dataframe
        population_df = pd.DataFrame([individual.to_dict() for individual in popu])
        # scores and stats
        pop_dist_mean = population_df['distance'].mean()
        population_df['score'] = population_df['distance'].apply(lambda x: 100 / (x / pop_dist_mean))
        stan_dev = population_df['score'].std()
        # choose parents
        par_selection = []
        par_selection = population_df.nsmallest(4, 'distance')
        # print progress
        # print("\nPopulation:\n", population_df.to_string())
        #print("\nParent selection:\n", par_selection.to_string())
        #print("\nNew popu distance mean:\n", pop_dist_mean)
        print("generation:", generation_no)
        print("\nstand_dev:\n", stan_dev)
        # maybe send to turtle here?

    # and then final turtle here
    tf.draw_coord(bob, Datastore.locations, par_selection['genotype'].iloc[0])
    bob.color('white')
    bob.goto(0, 200)
    bob.write('aprx best route', True, align="center", font=12)  # write some text
    end = time.time()
    duration = end - start
    #print("Possible combinations:", factorial(no_of_locations))
    print("Possible combinations: %r" % "{:,}".format(factorial(no_of_locations)))
    print("In %r seconds" % duration)
    print("Individuals involved:", (no_in_population * generation_no))


if __name__ == "__main__":
    # execute only if run as a script
    pd.set_option('display.max_colwidth', -1)
    gen_algo()
    turtle.mainloop()


