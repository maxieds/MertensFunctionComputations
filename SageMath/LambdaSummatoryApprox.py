#### lambda-summatory-func-approx.py
#### Author: Maxie D. Schmidt
#### Created: 2020.07.20

from sage.all import *

## Algorithm taken from:
## https://mathoverflow.net/a/320042
@cached_function
def MertensM(x):
    if x == 1:
        return 1
    mertensFuncSum1 = sum(MertensM(floor(x/k)) for k in range(2, floor(sqrt(x)) + 1))
    mertensFuncSum2 = sum((floor(x/k) - floor(x/(k+1))) * MertensM(k) \
                            for k in range(1, floor(sqrt(x)) + 1))
    return 1 - mertensFuncSum1 - mertensFuncSum2 

## Algorithm of Lehmer taken from:
## https://www.ams.org/journals/mcom/1960-14-072/S0025-5718-1960-0120198-5/S0025-5718-1960-0120198-5.pdf
@cached_function
def LiouvilleL(x):
    gval = ceil(sqrt(x))
    LSum1 = sum(MertensM(floor(x / k**2)) for k in range(1, gval + 1))
    LSum2 = sum(moebius(ell) * floor(sqrt(x / ell)) for ell in range(1, floor(x / gval**2) + 1))
    LTerm3 = MertensM(floor(x / gval**2)) * floor(sqrt(x / gval**2))
    return LSum1 + LSum2 - LTerm3

def LiouvilleL0(x):
    return sum(MertensM(floor(x / d**2)) for d in range(1, floor(sqrt(x)) + 1))

def LiouvilleLSignRatio(x):
    return sign(LiouvilleL(x)) / ((-1) ** ceil(log(log(x))))

def LiouvilleLApproxV1(x):
    return x / log(x) * sum(((-log(log(x)))**(k-1)) / factorial(k-1) \
            for k in range(1, floor(log(log(x))) + 1))

def LiouvilleLApproxV2(x):
    return (x ** 0.25) / sqrt(log(x)) / sqrt(log(log(x)))

def PrimeNuOmegaFunc(n):
    return len(prime_divisors(n))

@cached_function
def LambdaAst(n):
    if n == 1:
        return 1
    return (LiouvilleL(n) - LiouvilleL(n - 1)) * ((-1) ** PrimeNuOmegaFunc(n))

def LambdaAstL(x):
    return sum(LambdaAst(n) for n in range(1, x+1))

def PrimesList(x):
    return prime_range(1, x)

def CHatConstantApprox(x):
    return 1 / 4.0 / product(1 - 1 / (p - 1)**2 for p in PrimesList(x)[1:])

CHatConstant = CHatConstantApprox(1000)

def LambdaAstLApprox(x):
    return 2 * CHatConstant / 3.0 * x

def PrintTableInLaTeXForm(tbl):
    latexArraySep = str(" & ")
    for tblRow in tbl:
        print(latexArraySep.join([str(te) for te in tblRow]), " \\\\")

def GetApproxTable(xmin, xupper, xvalsPerPage = 75, nprec = 4, quietRunMode = True):
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

