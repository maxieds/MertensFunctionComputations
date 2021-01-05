
<img src="https://github.com/maxieds/MertensFunctionComputations/blob/master/Images/RepositoryHeader.png" />

<img src="https://github.com/maxieds/MertensFunctionComputations/blob/master/Images/MVProbabilisticPrimes.png" />

# Computations with the Mertens function

The source code in this repository catalogs supplementary computations including tables and 
symbolic summation and integration calculations used in my article documenting work with the 
Mertens function (2021). 
The sources come in two flavors: 
[Mathematica notebook format](https://github.com/maxieds/MertensFunctionComputations/tree/master/MathematicaNotebooks) and 
[sage (python3 source) format](https://github.com/maxieds/MertensFunctionComputations/tree/master/SageMath). 

There is a listing of some additional 
[documentation files](https://github.com/maxieds/MertensFunctionComputations/tree/master/Docs) in the subdirectory. 
The other computational experiments, e.g., to verify numerical expectation or average order 
formulas from the article found 
[in this directory](https://github.com/maxieds/MertensFunctionComputations/tree/master/SageMath/Scripts), 
should be self explanatory from context. 
Feel free to contact the author if any errors are present or if 
[other issues](https://github.com/maxieds/MertensFunctionComputations/issues) arise. 

## Some example computations to get started (SageMath)


The key Dirichlet inverse function sequence, $g^{-1}(n)$, is defined and computed as in the tables that 
appear in the appendix to the article in 
[this Mathematica notebook](https://github.com/maxieds/MertensFunctionComputations/blob/master/MathematicaNotebooks/GInvFunctionSequenceCalculations.nb).
We can also use ``sage`` (working with ``python3``) to compute this sequence and its summatory 
function $G^{-1}(x)$ as follows:
```bash
$ cd SageMath
$ sage
sage: attach("Scripts/AttachAllFiles.sage")
sage: print(table([[nx, gInvFunc(nx), GSummatoryFunc(nx)] for nx in range(1, 111)]))
  1     1      1
  2     -2     -1
  3     -2     -3
  4     2      -1
  5     -2     -3
  6     5      2
  7     -2     0
  8     -2     -2
  9     4      2
  10    5      7
  11    -2     5
  12    -11    -6
  13    -2     -8
  14    5      -3
  15    5      2
  16    4      6
  17    -2     4
  18    -13    -9
  19    -2     -11
  20    -11    -22
  21    5      -17
  22    5      -12
  23    -2     -14
  24    18     4
  25    6      10
  26    5      15
  27    -6     9
  28    -7     2
  29    -2     0
  30    -30    -30
  31    -2     -32
  32    -6     -38
  33    5      -33
  34    5      -28
  35    5      -23
  36    43     20
  37    -2     18
  38    5      23
  39    5      28
  40    18     46
  41    -2     44
  42    -23    21
  43    -2     19
  44    -7     12
  45    -13    -1
  46    5      4
  47    -2     2
  48    -30    -28
  49    6      -22
  50    -19    -41
  51    5      -36
  52    -7     -43
  53    -2     -45
  54    23     -22
  55    5      -17
  56    -1     -18
  57    5      -13
  58    5      -8
  59    -2     -10
  60    104    94
  61    -2     92
  62    5      97
  63    -13    84
  64    10     94
  65    5      99
  66    -16    83
  67    -2     81
  68    -7     74
  69    5      79
  70    -16    63
  71    -2     61
  72    -109   -48
  73    -2     -50
  74    5      -45
  75    -19    -64
  76    -7     -71
  77    5      -66
  78    -16    -82
  79    -2     -84
  80    -30    -114
  81    9      -105
  82    5      -100
  83    -2     -102
  84    67     -35
  85    5      -30
  86    5      -25
  87    5      -20
  88    9      -11
  89    -2     -13
  90    81     68
  91    5      73
  92    -7     66
  93    5      71
  94    5      76
  95    5      81
  96    44     125
  97    -2     123
  98    -19    104
  99    -13    91
  100   47     138
  101   -2     136
  102   -16    120
  103   -2     118
  104   9      127
  105   -16    111
  106   5      116
  107   -2     114
  108   -93    21
  109   -2     19
  110   -16    3
```
Given that we have "nice", easy to work with exact formulas for $g^{-1}(n)$ when $n$ is squarefree, 
a large subset of the integers with limiting density approximately ``TODO``, we may begin to wonder 
how closely (and when) we can approximate $G^{-1}(x)$ up to a predictably bounded constant by restricting 
the summands to only those $n$ such that $\mu^2(n) = 1$? Take any bounds $(\alpha, \beta)$ and try 
modifying the next script example! Here we have selected $(\alpha, \beta) \mapsto (0, 1), (-1, 0)$ in the 
next listings:
```bash
$ cd SageMath
$ sage
sage: load("Scripts/CompareSquarefreeSumsToGInv.sage")
  25    10      1.30000000000000       0.360000000000000   0.360000000000000
  50    -41     0.414634146341463      0.460000000000000   0.260000000000000
  75    -64     0.328125000000000      0.520000000000000   0.293333333333333
  100   138     0.000000000000000      0.570000000000000   0.310000000000000
  125   -219    0.178082191780822      0.504000000000000   0.304000000000000
  150   286     -0.143356643356643     0.540000000000000   0.300000000000000
  175   145     -0.620689655172414     0.462857142857143   0.400000000000000
  200   -335    0.468656716417910      0.510000000000000   0.370000000000000
  225   219     -0.00456621004566210   0.546666666666667   0.346666666666667
  250   595     -0.0840336134453782    0.508000000000000   0.400000000000000
  275   51      -1.74509803921569      0.461818181818182   0.443636363636364
  300   -703    0.186344238975818      0.466666666666667   0.420000000000000
  325   -517    0.274661508704062      0.507692307692308   0.387692307692308
  350   -103    -0.0291262135922330    0.491428571428571   0.420000000000000
  375   1018    -0.0589390962671906    0.474666666666667   0.442666666666667
  400   1086    0.0681399631675875     0.472500000000000   0.450000000000000
  425   232     0.159482758620690      0.503529411764706   0.423529411764706
  450   -989    0.0606673407482305     0.526666666666667   0.404444444444444
  475   -1195   0.0585774058577406     0.551578947368421   0.383157894736842
  500   -1532   0.0593994778067885     0.574000000000000   0.364000000000000

Now within a detailed interval:

  465   -1033   0.0542110358180058   0.541935483870968   0.391397849462366
  466   -1028   0.0496108949416342   0.542918454935622   0.390557939914163
  467   -1030   0.0514563106796116   0.543897216274090   0.389721627408994
  468   -1168   0.0453767123287671   0.544871794871795   0.388888888888889
  469   -1163   0.0412725709372313   0.545842217484009   0.388059701492537
  470   -1179   0.0542832909245123   0.546808510638298   0.387234042553191
  471   -1174   0.0502555366269165   0.547770700636943   0.386411889596603
  472   -1165   0.0506437768240343   0.548728813559322   0.385593220338983
  473   -1160   0.0465517241379310   0.549682875264271   0.384778012684989
  474   -1176   0.0595238095238095   0.550632911392405   0.383966244725738
  475   -1195   0.0585774058577406   0.551578947368421   0.383157894736842
  476   -1165   0.0600858369098712   0.552521008403361   0.382352941176471
  477   -1178   0.0594227504244482   0.553459119496855   0.381551362683438
  478   -1173   0.0554134697357204   0.554393305439331   0.380753138075314
  479   -1175   0.0570212765957447   0.555323590814196   0.379958246346555
  480   -1669   0.0401437986818454   0.556250000000000   0.379166666666667
  481   -1664   0.0372596153846154   0.557172557172557   0.378378378378378
  482   -1659   0.0343580470162749   0.558091286307054   0.377593360995851
  483   -1675   0.0435820895522388   0.559006211180124   0.376811594202899
  484   -1636   0.0446210268948655   0.559917355371901   0.376033057851240
  485   -1631   0.0416922133660331   0.560824742268041   0.375257731958763
  486   -1569   0.0433397068196303   0.561728395061728   0.374485596707819
  487   -1571   0.0445576066199873   0.562628336755647   0.373716632443532
  488   -1562   0.0448143405889885   0.563524590163934   0.372950819672131
  489   -1557   0.0417469492614001   0.564417177914110   0.372188139059305
  490   -1479   0.0439486139283300   0.565306122448980   0.371428571428571
  491   -1481   0.0452397029034436   0.566191446028513   0.370672097759674
  492   -1434   0.0467224546722455   0.567073170731707   0.369918699186992
  493   -1429   0.0433869839048285   0.567951318458418   0.369168356997972
  494   -1445   0.0539792387543253   0.568825910931174   0.368421052631579
  495   -1391   0.0560747663551402   0.569696969696970   0.367676767676768
  496   -1410   0.0553191489361702   0.570564516129032   0.366935483870968
  497   -1405   0.0519572953736655   0.571428571428571   0.366197183098592
  498   -1421   0.0626319493314567   0.572289156626506   0.365461847389558
  499   -1423   0.0639494026704146   0.573146292585170   0.364729458917836
  500   -1532   0.0593994778067885   0.574000000000000   0.364000000000000
```
