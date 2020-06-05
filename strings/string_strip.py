
##################
### our string ###

a = ".)43.dffw.wefwfwfw"

##########################
### remove with filter ###

b = ''.join(filter(lambda z: z.isdigit(), a))
print(b)

#############################
### remove with re module ###

import re
c = re.sub("\D", "", a)
print(c)
