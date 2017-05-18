import math
from sys import stdin

def sierp_circ(n):
    return int(math.ceil((n+1)*math.log10(3.0) - n*math.log10(2.0)))

case = 1
for line in stdin:
    print "Case {0}: {1}".format(case, sierp_circ(int(line)))
    case += 1