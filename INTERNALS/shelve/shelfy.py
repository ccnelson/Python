
import shelve

d = shelve.open('dbfile', flag='c') # c option opens, or creates file.
                                    # if the db existed from earlier code
                                    # it may fail to open.
                                    # delete db and let it recreate
d["1"] = "first"    # store date at key "1" - keys are strings
d["2"] = [0, 3, 2, 3, 2, 0] # store array
d["three"] = "3r and final" 

key_list = list(d.keys()) # list keys

temp = d['2']             # extracts the copy
temp.append(5)             # mutates the copy
d['2'] = temp               # stores copy

#temp = d['three']             
#temp.append(5)         You cannot mutate strings
#d['three'] = temp

print(d["1"])
print(d["2"])
print(d["three"])

print(key_list)

d.close()
