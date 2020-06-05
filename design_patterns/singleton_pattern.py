class _Singleton(object):

    def __init__(self):
        # just for the sake of information
        self.instance = "Instance at %d" % self.__hash__()


_singleton = _Singleton()

def Singleton(): return _singleton

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
print(vars(s1))
print(vars(s2))
