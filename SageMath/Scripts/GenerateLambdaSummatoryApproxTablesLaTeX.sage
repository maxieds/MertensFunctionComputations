#### GenerateLambdaSummatoryApproxTablesLaTeX.sage

from LambdaSummatoryApprox import *

nPrecMode=DefaultNPrec
quietPrintMode=DefaultQuietPrint

initXMin=50000
initXMax=50090
initXPerPage=45
initTbl=GetLambdaApproxTable(initXMin, initXMax, initXPerPage, nPrecMode, quietPrintMode)
print("Initial page LaTeX Table source: \n")
PrintTableInLaTeXForm(initTbl)
print("")

fullXMin=50090
fullXMax=51000
fullXPerPage=75
fullTbl=GetLambdaApproxTable(fullXMin, fullXMax, fullXPerPage, nPrecMode, quietPrintMode)
print("Full pages LaTeX table source: \n")
PrintTableInLaTeXForm(fullTbl, newlineAfter=fullXPerPage)

