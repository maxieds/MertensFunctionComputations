#### GenerateLambdaSummatoryApproxTablesLaTeX.sage

from LambdaSummatoryApprox import *

nPrecMode=DefaultNPrec
quietPrintMode=DefaultQuietPrint

initXMin=100000
initXMax=100090
initXPerPage=45
initTbl=GetLambdaApproxTable(initXMin, initXMax, initXPerPage, nPrecMode, quietPrintMode)
print("Initial page LaTeX Table source: \n")
PrintTableInLaTeXForm(initTbl)
print("")

fullXMin=100090
fullXMax=100350
fullXPerPage=75
fullTbl=GetLambdaApproxTable(fullXMin, fullXMax, fullXPerPage, nPrecMode, quietPrintMode)
print(table(fullTbl))
#print("Full pages LaTeX table source: \n")
#PrintTableInLaTeXForm(fullTbl, newlineAfter=fullXPerPage)

