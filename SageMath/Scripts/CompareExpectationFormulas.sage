#### CompareExpectationFormulas.sage 

from CheckExpectationFormulas import *

xMin = 16
xMax = 1500

tblCFunc = GetEComparisonTableCFunc(xMin, xMax)
tblgInv = GetEComparisonTableAbsGInvFunc(xMin, xMax)

fullTable = []
for x in range(xMin, xMax + 1):
    tblRow = tblCFunc[x]
    tblRow.extend(tblgInv[x])
    fullTable.append(tblRow)
print(table(fullTable))

