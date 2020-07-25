#### LambdaSummatoryApprox.py
#### Author: Maxie D. Schmidt
#### Created: 2020.07.20

from sage.all import *

from GlobalConfig import *
from Utils import *
from SpecialFunctions import *

@cached_function
def LiouvilleL0(x):
    AssertPositiveInteger(x)
    return sum(MertensM(floor(x / d**2)) for d in range(1, floor(sqrt(x)) + 1))

def LiouvilleLSignRatio(x):
    AssertPositiveInteger(x)
    return sign(LiouvilleL(x)) / ((-1) ** floor(log(log(x))))

def LiouvilleLApproxV1(x):
    AssertPositiveInteger(x)
    return x / log(x) * sum(((-log(log(x)))**(k-1)) / factorial(k-1) \
            for k in range(1, floor(log(log(x))) + 1))

def LiouvilleLApproxV2(x):
    AssertIntegerGreaterThan(x, e)
    return (x ** 0.25) / sqrt(log(x)) / sqrt(log(log(x)))

@cached_function
def LambdaAst(n):
    AssertPositiveInteger(n)
    if n == 1:
        return 1
    return (-1) ** PrimeNuOmegaFunc(n)

def LambdaAstL(x):
    AssertPositiveInteger(x)
    return sum(LambdaAst(n) for n in range(1, x+1))

def CHatConstantApprox(x):
    return 1 / 4.0 / product(1 - 1 / (p - 1)**2 for p in PrimesList(x)[1:])

CHatConstant = CHatConstantApprox(1000)

def LambdaAstLApprox(x):
    AssertIntegerGreaterThan(x, e)
    return x / sqrt(2 * pi) / sqrt(log(log(x)))

def GetLambdaApproxTable(xmin, xupper, xvalsPerPage = 75, nprec = DefaultNPrec, quietRunMode = True):
    tblRow = lambda x: [x, LiouvilleL(x), LiouvilleLSignRatio(x), \
                           n(LiouvilleL(x) / LiouvilleLApproxV1(x), nprec), \
                           n(LiouvilleL(x) / LiouvilleLApproxV2(x), nprec), \
                           x, LambdaAstL(x), n(LambdaAstL(x) / LambdaAstLApprox(x), nprec)]
    fullTblData = []
    for x in range(1, floor((xupper - xmin) / 2.0 / xvalsPerPage) + 1):
        if not quietRunMode:
            print("x = {0} ... {0}".format(x, xmin + 2 * x * xvalsPerPage))
        for x0 in range(0, xvalsPerPage):
            tblRowData = tblRow(xmin + x0 + (x-1) * 2 * xvalsPerPage)
            tblRowDataSpliced = tblRow(xmin + x0 + (2 * x - 1) * xvalsPerPage)
            tblRowData.extend(tblRowDataSpliced)
            fullTblData.append(tblRowData)
    return fullTblData

