#### CheckExpectationFormulas.py
#### Author: Maxie D. Schmidt
#### Created: 2020.07.21

from sage.all import *

from GlobalConfig import *
from Utils import *
from SpecialFunctions import *
from LambdaSummatoryApprox import *

def ApproxECFunc(x):
    AssertIntegerGreaterThan(x, e)
    constTerm = 1
    funcTerms = log(x) * log(log(x))
    return n(constTerm * funcTerms, DefaultNPrec)

def ExactECFunc(x):
    AssertPositiveInteger(x)
    sumTerms = sum(CFunc(n) for n in range(1, x+1))
    return n(1 / x * sumTerms, DefaultNPrec)

def ApproxEAbsGInvFunc(x):
    AssertIntegerGreaterThan(x, e)
    constTerm = 3 / (pi**2)
    funcTerms = (log(x)**2) * log(log(x))
    return n(constTerm * funcTerms, DefaultNPrec)

def ExactEAbsGInvFunc(x):
    AssertPositiveInteger(x)
    sumTerms = sum(abs(gInvFunc(n)) for n in range(1, x+1))
    return n(1 / x * sumTerms, DefaultNPrec)

def GetEComparisonTableCFunc(xmin, xmax, nprec = DefaultNPrec):
    tblRow = lambda ni: [ni, ExactECFunc(ni) / n(ApproxECFunc(ni), nprec)]
    fullTableData = []
    for rowi in range(xmin, xmax + 1):
        fullTableData.append(tblRow(rowi))
    return fullTableData

def GetEComparisonTableAbsGInvFunc(xmin, xmax, nprec = DefaultNPrec):
    tblRow = lambda ni: [ni, ExactEAbsGInvFunc(ni) / n(ApproxEAbsGInvFunc(ni), nprec)]
    fullTableData = []
    for rowi in range(xmin, xmax + 1):
        fullTableData.append(tblRow(rowi))
    return fullTableData

