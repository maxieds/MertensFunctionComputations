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
    return pari(bigOmegaPari)

def PrimesList(x):
    AssertIntegerGreaterThan(x, 1)
    return prime_range(1, x)

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



