#### CalculateGInvSummatoryFunction.sage

from GInvSummatoryFunction import *

xMin = 16
xMax = 10000

valuesTable = GetGInvSummatoryFuncComparisonTable(xMin, xMax)
print(table(valuesTable))

PlotGInvSummatoryFuncSignChanges(xMin, xMax)


