#### SpecialFunctions.py
#### Author: Maxie D. Schmidt 
#### Created: 2020.07.21

from sage.all import *

from Utils import *

## Algorithm taken from:
## https://mathoverflow.net/a/320042
@cached_function
def MertensM(x):
    AssertNonNegativeInteger(x)
    if x == 0:
        return 0
    elif x == 1:
        return 1
    mertensFuncSum1 = sum(MertensM(floor(x/k)) for k in range(2, floor(sqrt(x)) + 1)) 
    mertensFuncSum2 = sum((floor(x/k) - floor(x/(k+1))) * MertensM(k) \
                            for k in range(1, floor(sqrt(x)) + 1)) 
    return 1 - mertensFuncSum1 - mertensFuncSum2

def PrimeNuOmegaFunc(n):
    AssertPositiveInteger(n)
    return len(prime_divisors(n))

def PrimeBigOmegaFunc(n):
    AssertPositiveInteger(n)
    bigOmegaPari = "bigomega({0})".format(n)
    return int(pari(bigOmegaPari))

def PrimesList(x):
    AssertIntegerGreaterThan(x, 1)
    return prime_range(1, x)

## Algorithm of Lehmer taken from:
## https://www.ams.org/journals/mcom/1960-14-072/S0025-5718-1960-0120198-5/S0025-5718-1960-0120198-5.pdf
@cached_function
def LiouvilleL(x):
    AssertNonNegativeInteger(x)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    gval = ceil(sqrt(x))
    LSum1 = sum(MertensM(floor(x / k**2)) for k in range(1, gval + 1)) 
    LSum2 = sum(moebius(ell) * floor(sqrt(x / ell)) for ell in range(1, floor(x / gval**2) + 1)) 
    LTerm3 = MertensM(floor(x / gval**2)) * floor(sqrt(x / gval**2))
    return LSum1 + LSum2 - LTerm3

def LiouvilleLambda(n):
    AssertPositiveInteger(n)
    if n == 1:
        return 1
    return LiouvilleL(n) - LiouvilleL(n-1)

@cached_function
def CknFunc(k, n):
    AssertPositiveInteger(n)
    AssertNonNegativeInteger(k)
    if k == 0 and n == 1:
        return 1
    elif k == 0:
        return 0
    else:
        divSum = sum(CknFunc(k-1, d) * PrimeNuOmegaFunc(n/d) for d in divisors(n))
        return divSum
    return 0

def CFunc(n):
    return CknFunc(PrimeBigOmegaFunc(n), n)

@cached_function
def GSummatoryFunc(x):
    AssertPositiveInteger(x)
    return sum(CFunc(n) * LiouvilleLambda(n) * MertensM(floor(x/n)) for n in range(1, x+1))

def gInvFunc(n):
    AssertPositiveInteger(n)
    if n == 1:
        return 1
    else:
        return GSummatoryFunc(n) - GSummatoryFunc(n-1)


