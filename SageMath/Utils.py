#### Utils.py 
#### Author: Maxie D. Schmidt
#### Created: 2020.07.21

from sage.all import *

def AssertInteger(n):
    if not isinstance(n, int) and not isinstance(n, sage.rings.integer.Integer) and \
       (isinstance(n, sage.rings.rational.Rational) and not n.is_integer()):
        raise ValueError("Input {0} is not an integer: {1}".format(n, type(n)))
    return True


def AssertPositiveInteger(n):
    if not AssertInteger(n) or n <= 0:
        raise ValueError("Input {0} is not a positive integer: {1}".format(n, type(n)))
    return True

def AssertNonNegativeInteger(n):
    return AssertIntegerGreaterThan(n, -1)

def AssertIntegerGreaterThan(n, gthan):
    if n <= gthan or not AssertInteger(n):
        raise ValueError("Input {0} <= {1}".format(n, gthan))
    return True

def PrintTableInLaTeXForm(tbl, newlineAfter = 0):
    latexArraySep = str(" & ")
    for (ridx, tblRow) in enumerate(tbl):
        if newlineAfter > 0 and (ridx % newlineAfter) == 0:
            print("")
        print(latexArraySep.join([str(te) for te in tblRow]), " \\\\")

