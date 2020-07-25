#### GInvSummatoryFunction.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

from GlobalConfig import *
from Utils import *
from SpecialFunctions import *

def GetGInvSummatoryFuncLowerBoundApprox(x):
    AssertIntegerGreaterThan(x, e)
    constantTerm = 1 / sqrt(2 * pi) * 6 / (pi**2)
    return log(x) * sqrt(log(log(x)))

def GetGInvSummatoryFuncComparisonTable(xmin, xmax, nprec = DefaultNPrec):
    fullTable = []
    for x in range(xmin, xmax + 1):
        tblRow = [x, GSummatoryFunc(x), n(GSummatoryFunc(x) / GetGInvSummatoryFuncLowerBoundApprox(x), nprec)]
        fullTable.append(tblRow)
    return fullTable

def GetGInvSummatoryFuncSignChanges(xmin, xmax):
    AssertPositiveInteger(xmin)
    AssertNonNegativeInteger(xmax - xmin)
    signChangeXList = []
    for x in range(xmin, xmax + 2):
        if sign(GSummatoryFunc(x + 1)) != sign(GSummatoryFunc(x)): 
            signChangeXList.append([x + 1])
    return signChangeXList

def PlotGInvSummatoryFuncSignChanges(xmin, xmax):
    AssertPositiveInteger(xmin)
    AssertNonNegativeInteger(xmax - xmin)
    signChangeXList = GetGInvSummatoryFuncSignChanges(xmin, xmax)
    signChangeXListXAxis = range(1, len(signChangeXList) + 1)
    xPlotFuncValues = np.arange(xmin, xmin + len(signChangeXList), 1)
    yPlotFuncValues = [log(log(x)) for x in xPlotFuncValues]
    plotXAxis = r""
    plotYAxis = r"$x \in \mathbb{Z}^{+}$"
    plotTitle = r"Values of $x \geq 2$ such that \\ $\operatorname{sgn}(G^{-1}(x)) \neq \operatorname{sgn}(G^{-1}(x-1))$"
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.plot(signChangeXListXAxis, signChangeXList, 'bs', xPlotFuncValues, yPlotFuncValues, 'g--')
    plt.title(plotTitle)
    plt.xlabel(plotXAxis)
    plt.ylabel(plotYAxis)
    #plt.show()
    tempImgPath = GetTempFileSavePath("png", "PlotGInvSummatoryFuncSignChanges-XMin={0}-XMax={1}".format(xmin, xmax))
    plt.savefig(tempImgPath)
    DisplayImage(tempImgPath)
