## lambda-summatory-func-approx.py
## Author: Maxie D. Schmidt
## Created: 2020.07.20

from sage.all import *

@cached_function
def MertensM(x):
    if x == 1:
        return 1
    mertensFuncSum1 = sum(MertensM(floor(x/k)) for k in range(2, floor(sqrt(x)) + 1))
    mertensFuncSum2 = sum((floor(x/k) - floor(x/(k+1))) * MertensM(k) \
                            for k in range(1, floor(sqrt(x)) + 1))
    return 1 - mertensFuncSum1 - mertensFuncSum2 

def LiouvilleL(x):
    return sum(MertensM(floor(x / d**2)) for d in range(1, floor(sqrt(x)) + 1))

def LiouvilleLSignRatio(x):
    return sign(LiouvilleL(x)) / ((-1) ** floor(log(log(x))))

def LiouvilleLApproxV1(x):
    return x / log(x) * sum((-log(log(x))) ** (k-1) / factorial(k-1) \
            for k in range(1, floor(log(log(x))) + 1))

def LiouvilleLApproxV2(x):
    return (x ** 0.75) * sqrt(log(log(x))) / sqrt(log(log(x)))

def PrimeNuOmegaFunc(n):
    return len(prime_divisors(n))

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
    latexArraySep = str(' & ')
    for tblRow in tbl:
        print(latexArraySep.join(tblRow))

def GetApproxTable(xmin, xupper, xvalsPerPage = 75, nprec = 4):
    tblRow = lambda x: [x, LiouvilleL(x), LiouvilleLSignRatio(x), \
                           n(LiouvilleL(x) / LiouvilleLApproxV1(x), nprec), \
                           n(LiouvilleL(x) / LiouvilleLApproxV2(x), nprec), \
                           x, LambdaAstL(x), n(LambdaAstL(x) / LambdaAstLApprox(x), nprec)]
    fullTblData = []
    for x in range(1, floor((xupper - xmin) / 2.0 / xvalsPerPage) + 1):
        for x0 in range(0, xvalsPerPage):
            tblRowData = tblRow(xmin + x0 + (x-1) * 2 * xvalsPerPage)
            tblRowDataSpliced = tblRow(xmin + x0 + (2 * x - 1) * xvalsPerPage)
            tblRowData.extend(tblRowDataSpliced)
            fullTblData.append(tblRowData)
    return fullTblData

