#### ConclusionSectionAveragedSummatoryFuncs.sage

from SpecialFunctions import *

def TakeRatio(num, denom, rval = 0):
     return rval if denom == 0 else n(num / denom)
##

def AvgGFunc1(x):
     summand = lambda nn: sum(LiouvilleLambda(nn / d) * abs(gInvFunc(d)) for d in divisors(nn))
     return sum(summand(ni) for ni in range(1, x+1))
##

def AvgGFunc2(x):
     summand = lambda nn: sum(LiouvilleLambda(nn / d) * gInvFunc(d) for d in divisors(nn))
     return sum(summand(ni) for ni in range(1, x+1))
##

def AvgGFunc3(x):
     summand = lambda nn: sum(gInvFunc(d) for d in divisors(nn))
     return sum(summand(ni) for ni in range(1, x+1))
##

(xmin, xmax) = (1, 1250)
print("Displaying combined function ratios for x in [%d, %d]:\n" % (xmin, xmax))
print(table([[xi, TakeRatio(AvgGFunc1(xi), GSummatoryFunc(xi)), \
               TakeRatio(AvgGFunc2(xi), GSummatoryFunc(xi)), \
               TakeRatio(AvgGFunc3(xi), GSummatoryFunc(xi))] for xi in range(xmin, xmax+1)]))

print("\nTabulating density of ratios in [-5, 5]:\n")

tbl1 = [TakeRatio(AvgGFunc1(xi), GSummatoryFunc(xi)) for xi in range(xmin, xmax+1)]
density1 = n(len(list(filter(lambda val: -5 <= val and val <= 5, tbl1))) / (xmax + 1 - xmin))
print("Density for function #1", density1)


tbl2 = [TakeRatio(AvgGFunc2(xi), GSummatoryFunc(xi)) for xi in range(xmin, xmax+1)]
density2 = n(len(list(filter(lambda val: -5 <= val and val <= 5, tbl2))) / (xmax + 1 - xmin))
print("Density for function #2", density2)

tbl3 = [TakeRatio(AvgGFunc3(xi), GSummatoryFunc(xi)) for xi in range(xmin, xmax+1)]
density3 = n(len(list(filter(lambda val: -5 <= val and val <= 5, tbl3))) / (xmax + 1 - xmin))
print("Density for function #3", density3)

