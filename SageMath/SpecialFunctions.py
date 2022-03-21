#### SpecialFunctions.py
#### Author: Maxie D. Schmidt 
#### Created: 2020.07.21

from sage.all import *
from Utils import *

def DoubleFactorial(n):
    if n < -1:
        raise ValueError
    return gamma(n + 1 / 2) * (2 ** n) / sqrt(pi)

## Algorithm taken from:
## https://mathoverflow.net/a/320042
@cached_function
def MertensM(x):
    AssertNonNegativeInteger(x)
    if x == 0:
        return 0
    elif x == 1:
        return 1
    #mertensFuncSum1 = sum(MertensM(floor(x/k)) for k in range(2, floor(sqrt(x)) + 1)) 
    #mertensFuncSum2 = sum((floor(x/k) - floor(x/(k+1))) * MertensM(k) \
    #                        for k in range(1, floor(sqrt(x)) + 1)) 
    #return 1 - mertensFuncSum1 - mertensFuncSum2
    return sum(moebius(n) for n in range(1, x+1))

def PrimeNuOmegaFunc(n):
    AssertPositiveInteger(n)
    return len(prime_divisors(n))

@cached_function
def PrimeBigOmegaFunc(n):
    AssertPositiveInteger(n)
    bigOmegaPari = "bigomega({0})".format(n)
    return int(pari(bigOmegaPari))

def PrimesList(x):
    AssertIntegerGreaterThan(x, 1)
    return prime_range(1, x)

@cached_function
def LiouvilleL(x):
    AssertPositiveInteger(x)
    return sum(MertensM(floor(x / d**2)) for d in range(1, floor(sqrt(x)) + 1))

def LiouvilleLambda(n):
    AssertPositiveInteger(n)
    if n == 1:
        return 1
    return LiouvilleL(n) - LiouvilleL(n-1)

def PrimeZetaP(s, nprec=16):
    if real(s) <= 1 and real(s) > 0:
        raise NotImplemented
    maxPrime = ceil(10 ** (nprec / real(s)))
    return sum(map(lambda p: p ** (-s), prime_range(2, maxPrime + 1)))

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

@cached_function
def CFunc(n):
    return CknFunc(PrimeBigOmegaFunc(n), n)

@cached_function
def CFuncExplicit(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return factorial(PrimeBigOmegaFunc(n)) * product(map(lambda pp: 1 / factorial(pp[1]), list(factor(n))))

@cached_function
def GSummatoryFunc(x):
    AssertPositiveInteger(x)
    return sum(CFunc(n) * LiouvilleLambda(n) * MertensM(floor(x/n)) for n in range(1, x+1))

@cached_function
def gInvFunc(n):
    AssertPositiveInteger(n)
    if n == 1:
        return 1
    else:
        return GSummatoryFunc(n) - GSummatoryFunc(n-1)


