#### CompareExpectationFormulas.sage 

from CheckExpectationFormulas import *

xMin = 16
xMax = 5000

tblCFunc = GetEComparisonTableCFunc(xMin, xMax)
tblgInv = GetEComparisonTableAbsGInvFunc(xMin, xMax)

fullTable = []
for (x, tblRow) in enumerate(tblCFunc):
    tblRow.extend(tblgInv[x])
    fullTable.append(tblRow)
print(table(fullTable))

