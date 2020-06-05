
import pdb

pdb.set_trace()

def combine(s1,s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 +'"'   # encloses it in double quotes,...
    return s3            # and returns it.

aX = "aaa"

bX = "bbb"
cX = "ccc"
final = combine(aX,bX)
print(final)

# "n" = next
# <Enter> = repeat last pdb command
# "q" = quit
# "p" = print variable (i.e: "p a" OR "p a, b, c")
# "c" = continue running program to end
# "l" = list source
# "s" = step into subroutine
#       "r" = continue to end of current subroutine
#
#####################################################
# change varibales at runtime
#
# (Pdb) aX = "qqq"
#
# (Pdb) !b = "ppp"  ## <--- the exclamation is because b is
#                                   a pdb keyword
#   
#####################################################
