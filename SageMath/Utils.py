#### Utils.py 
#### Author: Maxie D. Schmidt
#### Created: 2020.07.21

from sage.all import *

def AssertInteger(n):
    if not isinstance(n, int) and not isinstance(n, sage.rings.integer.Integer):
        raise ValueError("Input {0} is not a positive integer: {1}".format(n, type(n)))
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

def PrintTableInLaTeXForm(tbl):
    latexArraySep = str(" & ")
    for tblRow in tbl:
        print(latexArraySep.join([str(te) for te in tblRow]), " \\\\")

