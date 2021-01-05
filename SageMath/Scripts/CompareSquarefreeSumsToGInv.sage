#### CompareSquarefreeSumsToGInv.sage

from GInvSummatoryFunction import *
from SpecialFunctions import *

def GInvSqfreeFunc(x): 
     sqfreeQ = lambda nidx: moebius(nidx) ** 2
     return sum(sqfreeQ(ni) * gInvFunc(ni) for ni in range(1, x+1))
##

def ComputeRawSummatoryFuncRatioTable(xmax):
     return [0 if GSummatoryFunc(ni) == 0 else n(GInvSqfreeFunc(ni) / GSummatoryFunc(ni)) for ni in range(1, xmax+1)]
##

def TallyDensityInRange(alpha, beta, x):
     fullValuesLst = ComputeRawSummatoryFuncRatioTable(x)
     lstInRange = list(filter(lambda ni: alpha <= ni and ni <= beta, fullValuesLst))
     return n(len(lstInRange) / x)
##

def DisplayDensityTable(alpha, beta, xmin, xmax, xdelta = 1): 
     if beta < alpha:
          raise ValueError("Wrong interval form of beta <= alpha specified!")
     densityCompRow = lambda xi: [xi, GSummatoryFunc(xi), \
                                   0 if GSummatoryFunc(xi) == 0 else n(GInvSqfreeFunc(xi) / GSummatoryFunc(xi)), \
                                   TallyDensityInRange(alpha, beta, xi), \
                                   TallyDensityInRange(-beta, -alpha, xi)]
     return table([densityCompRow(x) for x in range(xmin, xmax+1, xdelta)])
##

(initAlpha, initBeta) = (0, 1)
(xmin, xmax, xdelta) = (25, 500, 25)
print(DisplayDensityTable(initAlpha, initBeta, xmin, xmax, xdelta))

print("\nNow within a detailed interval:\n")
(xmin, xmax, xdelta) = (465, 500, 1)
print(DisplayDensityTable(initAlpha, initBeta, xmin, xmax, xdelta))
