#### RestrictedPartialSums.py
#### Author: Maxie D. Schmidt 
#### Created: 2022.03.21

from sage.all import *

from Utils import *
from SpecialFunctions import *

@cached_function
def GHat(z):
    return exp(-PrimeZetaP(2) * z) * (zeta(2) ** (-z)) / gamma(1 + z)

@cached_function
def RestrictedPartialCOmegaSumExactFormula_V1(k, x):
    if x <= 0 or k <= 0:
        return 0
    elif x == 1 and k == 1:
        return 1
    elif x == 1:
        return 0
    elif PrimeBigOmegaFunc(x) == k:
        return CFunc(x) + RestrictedPartialCOmegaSumExactFormula(k, x - 1)
    else:
        return RestrictedPartialCOmegaSumExactFormula(k, x - 1)

@cached_function
def RestrictedPartialCOmegaSumExactFormula(k, x):
    OmegaNEqKIndices = filter(lambda n: PrimeBigOmegaFunc(n) == k, range(1, x + 1))
    return sum(map(lambda n: CFunc(n), OmegaNEqKIndices))

def RestrictedPartialCOmegaSumApproxFormula(k, x):
    return sqrt(2 * pi) * x / log(x) * GHat((2 * k - 1) / log(log(x))) * k * \
           (log(log(x)) ** (2 * k - 3/2)) / (2 ** k) / DoubleFactorial(2 * k - 3)

def RestrictedPartialCOmegaSumRatio(k, x, nprec=12):
    ratioNum = RestrictedPartialCOmegaSumExactFormula(k, x)
    ratioDenom = RestrictedPartialCOmegaSumApproxFormula(k, x)
    preventDivByZero = ratioDenom.is_zero()
    return NaN if preventDivByZero else n(ratioNum / ratioDenom, nprec)
