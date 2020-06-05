import shelve

def use_db():
    d = shelve.open('dbfile', flag='c')
    d["1"] = "first"   
    d["2"] = [0, 3, 2, 3, 2, 0] 
    d["three"] = "3r and final" 
    return d

db = use_db()

print(db["1"])

temp = "second"
db["1"] = temp
print(db["1"])

db.close()


