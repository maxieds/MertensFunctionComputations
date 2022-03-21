#### VerifyRestrictedCOmegaSums.sage

from sage.all import *
from SpecialFunctions import *
from RestrictedPartialSums import *

XMin, XMax = ceil(exp(exp(1))), 100000
KMax = ceil(3 / 2 * log(log(XMax)))
XStepSize = 250
PrintProgress = True

TableHeaderRow = [ "x" ] + [ k for k in range(1, KMax + 1) ]
GetXRatioRowFunc = lambda x: [ RestrictedPartialCOmegaSumRatio(k, x) for k in range(1, KMax + 1) ]
RatioTableData = [ TableHeaderRow ]

print("Checking ratios converge to columnwise constant for x in [%d, %d] where k in [1, %d] ..." % (XMin, XMax, KMax))

curXMin = XMin
while curXMin <= XMax:
    RatioTableData += [ [ x ] + GetXRatioRowFunc(x) for x in range(curXMin, curXMin + XStepSize + 1) ]
    if PrintProgress:
        print("   ===> DONE computing ratios for %d <= x <= %d ... [%2.2f%%]" % \
              (curXMin, curXMin + XStepSize, 100.0 * float((curXMin + XStepSize) / XMax)))
    curXMin += XStepSize
if PrintProgress:
    print("")

print(table(RatioTableData))

