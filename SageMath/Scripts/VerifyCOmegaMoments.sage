#### VerifyCOmegaMoments.sage

from sage.all import *
from SpecialFunctions import *

def GetAverageOrderExact(x):
    return sum(map(lambda n: CFunc(n), range(1, x + 1))) / x

def GetVarianceExact(x):
    secondMoment = sum(map(lambda n: CFunc(n) ** 2, range(1, x + 1))) / x
    firstMomentSq = GetAverageOrderExact(x) ** 2
    return sqrt(secondMoment - firstMomentSq)

def GetAverageOrderCompareRatio(x):
    approx = 0 if x < exp(exp(1)) else log(log(x)) * log(log(log(x))) 
    exact = GetAverageOrderExact(x)
    return n(approx / exact)

def GetVarianceCompareRatio(x):
    approx = 0 if x < exp(exp(1)) else sqrt(x) * log(log(x)) * log(log(log(x)))
    exact = GetVarianceExact(x)
    return n(approx / exact)

XMin, XMax = ceil(exp(exp(1))), 100000
XStepSize = 250
PrintProgress = True

TableHeaderRow = [ "x", "AVG-ORDER", "VARIANCE" ]
GetXRatioRowFunc = lambda x: [ x, GetAverageOrderCompareRatio(x), GetVarianceCompareRatio(x) ]
RatioTableData = [ TableHeaderRow ]

print("Checking moment ratios converge to a constant for x in [%d, %d] ..." % (XMin, XMax))

curXMin = XMin
while curXMin <= XMax:
    RatioTableData += [ GetXRatioRowFunc(x) for x in range(curXMin, curXMin + XStepSize + 1) ]
    if PrintProgress:
        print("   ===> DONE computing ratios for %d <= x <= %d ... [%2.2f%%]" % \
              (curXMin, curXMin + XStepSize, 100.0 * float((curXMin + XStepSize) / XMax)))
    curXMin += XStepSize
if PrintProgress:
    print("")

print(table(RatioTableData))
