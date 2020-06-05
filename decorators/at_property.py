class Thing:
    def __init__(self, my_word):
        self._word = my_word 
    @property
    def word(self):
        return self._word

print( Thing('ok').word )


 #otherwise its just a method as normal

##class Thing:
##    def __init__(self, my_word):
##        self._word = my_word
##    def word(self):
##        return self._word
##
##print( Thing('ok').word() )
