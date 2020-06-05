import time
 
start = time.time()
 
s = 1 + 1
 
elapsed = time.time() - start
 
print("result %s returned in %s seconds" % (s,elapsed))

print("the current time is %r" % time.ctime())
