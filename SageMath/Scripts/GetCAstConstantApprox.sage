#### GetCAstConstantApprox.sage

from SpecialFunctions import *

def CAstApprox(x):
     evalue = sum(CFunc(n) for n in range(1, x+1)) / x
     return n(evalue / log(x) / sqrt(log(log(x))))
##

def GAstApprox(x):
     evalue = sum(gInvFunc(n) for n in range(1, x+1)) / x
     return n(evalue / (log(x) ** 2) / sqrt(log(log(x))))
##

(xmin, xmax) = (4, 15000)
ntbl = [[xi, CAstApprox(xi)] for xi in range(xmin, xmax+1)]
print(table(ntbl))

(xmin, xmax) = (4, 15000)
ntbl = [[xi, GAstApprox(xi)] for xi in range(xmin, xmax+1)]
print(table(ntbl))
