
import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', -1)  # wide output

no_of_locs = 10

zero_to_locs = np.arange(0, no_of_locs)  # 0 > no_of_locs

lots_of_hs = np.array(['h' for i in range(no_of_locs)])  # lots of h's

s = pd.Series(lots_of_hs, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y', 'z'])  # some alphabet index

print(s)  # alpha indexes h's

df = pd.DataFrame({'Index': pd.Series([91, 81, 71, 61, 51, 41, 31, 21, 11, 1], index=s.index),
                    'Chromosome': pd.Timestamp(pd.Timestamp.now()),
                    'Phenotype': pd.Series(1.2, index=s.index, dtype='float32'),
                    'Distance': pd.Series([8, 0, 0, 8, 0, 0, 8, 8, 0, 0], index=s.index),
                    'Score': pd.Categorical(["te", "tr", "te", "te", "tr", "te", "te", "tr", "te", "te"]),
                    'Extra': s})

print(df)