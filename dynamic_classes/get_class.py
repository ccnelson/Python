                         # n is an index to a section
def gclass_info(n, obj): # of text showing class info
    y = type(obj).mro() # get that class info
    y = y[n]            # find the part we want
    y = str(y)          # turn into a string
    y = y[17:-2]        # slice string
    return y            # return slice
    
