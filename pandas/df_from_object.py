
import pandas as pd


class Some(object):
    def __init__(self, a, b):  # standard init def
        self.a = a
        self.b = b

    def to_dict(self):  # special method
        return {'a': self.a,
                'b': self.b, }


list_of_objects = [Some(3, 9), Some(4, 16)]  # a list to instantiate objects

x = pd.DataFrame([i.to_dict() for i in list_of_objects])  # cast into dataframe

y = x['a'].mean()  # get avg.

print(x.to_string())

print("mean of a: ", y)