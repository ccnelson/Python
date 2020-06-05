
import pandas as pd
import numpy as np


# ## website examples
##
s = pd.Series([1, 3, 5, 6])
print(s)

dates = pd.date_range('20130101', periods=4)
print(dates)

df = pd.DataFrame(np.random.randn(4,4), index=dates, columns=['Ay', 'Bee', 'Cee', 'Dee'])
print(df)

df2 = pd.DataFrame({'Ayy': pd.Series([9, 8, 7, 6], index=dates),
                    'Bee': pd.Timestamp('20130102'),
                    'Cee': pd.Series(1, index=dates, dtype='float32'),
                    'Dee': pd.Series([8, 0, 0, 8], index=dates),
                    'Eee': pd.Categorical(["test", "train", "test", "train"]),
                    'eF': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.describe())
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_values(by='Bee'))
s = pd.Series([(3.7, 4), (4.2, 0.7), (-0.1, -7.8)])
print('\n\tSeries:\n', s)
df = pd.DataFrame(s, columns=['x/y'])
print()
print("\n\tDataframe: \n", df)
print("\n\tElement: \n", df.iloc[0])

#########################################################################

