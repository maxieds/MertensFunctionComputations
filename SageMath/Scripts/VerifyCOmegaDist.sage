#### VerifyCOmegaDist.sage

from sage.all import *
from SpecialFunctions import *

HIST_NUM_BINS = 650
B0_CONSTANT = 3.0 / 2.0 

@cached_function
def GetNormalizedCFuncListWithProgress(xupper, mux, sigmax, printPause=5000):
    if printPause < 1 or xupper < 1:
         raise ValueError
    normalizedFuncValues = []
    startXMin, curXMin = 1, 1
    while curXMin <= xupper:
         normalizedFuncValues += [ (CFunc(n) - mux) / sigmax \
				   for n in range(curXMin, min(curXMin + printPause, xupper) + 1) ]
         curXMin += printPause
         percentComplete = float((curXMin - startXMin) / (xupper + 1 - startXMin))
         print("   ==> DONE computing #%d of #%d values ... %2.2f%% COMPLETED!" % \
			(curXMin - startXMin, xupper, percentComplete))
    return normalizedFuncValues

def DisplayCOmegaDistCDFV1(xupper, withExactCDF=True):
    mux = B0_CONSTANT * log(log(xupper)) * log(log(log(xupper)))
    sigmax = B0_CONSTANT * log(log(xupper)) * log(log(log(xupper)))
    normalizedFuncValues = GetNormalizedCFuncListWithProgress(xupper, mux, sigmax)
    stdNormalDist = RealDistribution('gaussian', 1)
    plotMin, plotMax = min(normalizedFuncValues), max(normalizedFuncValues)
    funcHist = histogram(normalizedFuncValues, bins=HIST_NUM_BINS, color='lime', edgecolor='green', hatch='*', 
                         alpha=0.2, density=True, cumulative=True, range = [ plotMin, plotMax ])
    if withExactCDF:
        stdNormalDistCDF = lambda zz: n(stdNormalDist.cum_distribution_function((zz + 1) / log(mux * abs(zz + 1))))
        overlayPlot = plot(stdNormalDistCDF, (floor(plotMin), ceil(plotMax)), 
                           color='darkgray', linestyle='--')
        return funcHist + overlayPlot
    return funcHist

def DisplayCOmegaDistCDFV2(xupper, withExactCDF=True):
    mux = B0_CONSTANT * sqrt(log(log(xupper)))
    sigmax = B0_CONSTANT * log(log(xupper))
    normalizedFuncValues = GetNormalizedCFuncListWithProgress(xupper, mux, sigmax)
    stdNormalDist = RealDistribution('gaussian', 1)
    plotMin, plotMax = min(normalizedFuncValues), max(normalizedFuncValues)
    funcHist = histogram(normalizedFuncValues, bins=HIST_NUM_BINS, color='cyan', edgecolor='blue', hatch='x', 
                         alpha=0.2, density=True, cumulative=True)
    if withExactCDF:
        stdNormalDistCDF = lambda zz: n(stdNormalDist.cum_distribution_function((zz + mux) / log(mux * abs(zz + mux))))
        overlayPlot = plot(stdNormalDistCDF, (floor(plotMin), ceil(plotMax)), 
                           color='darkgray', linestyle='--')
        return funcHist + overlayPlot
    return funcHist

def DisplayCOmegaDistCDFV3(xupper, withExactCDF=True):
    mux = B0_CONSTANT * log(log(xupper)) * log(log(log(xupper)))
    sigmax = B0_CONSTANT * log(log(xupper)) * log(log(log(xupper)))
    normalizedFuncValues = GetNormalizedCFuncListWithProgress(xupper, mux, sigmax)
    stdNormalDist = RealDistribution('gaussian', 1)
    plotMin, plotMax = min(normalizedFuncValues), max(normalizedFuncValues)
    funcHist = histogram(normalizedFuncValues, bins=HIST_NUM_BINS, color='violet', edgecolor='purple', hatch='x', 
                         alpha=0.2, density=True, cumulative=True)
    if withExactCDF:
        stdNormalDistCDF = lambda zz: n(stdNormalDist.cum_distribution_function(zz))
        overlayPlot = plot(stdNormalDistCDF, (floor(plotMin), ceil(plotMax)), 
                           color='darkgray', linestyle='--')
        return funcHist + overlayPlot
    return funcHist


#XUpper = 10000
XUpper = 1000000

#plotV1 = DisplayCOmegaDistCDFV1(XUpper)
#show(plotV1)

#plotV2 = DisplayCOmegaDistCDFV2(XUpper)
#show(plotV2)

plotV3 = DisplayCOmegaDistCDFV3(XUpper)
print("\n=============================\n")
show(plotV3)
