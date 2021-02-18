
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
  1     1     1
  2     -2    -1
  3     -2    -3
  4     2     -1
  5     -2    -3
  6     5     2
  7     -2    0
  8     -2    -2
  9     2     0
  10    5     5
  11    -2    3
  12    -7    -4
  13    -2    -6
  14    5     -1
  15    5     4
  16    2     6
  17    -2    4
  18    -7    -3
  19    -2    -5
  20    -7    -12
  21    5     -7
  22    5     -2
  23    -2    -4
  24    9     5
  25    2     7
  26    5     12
  27    -2    10
  28    -7    3
  29    -2    1
  30    -16   -15
  31    -2    -17
  32    -2    -19
  33    5     -14
  34    5     -9
  35    5     -4
  36    14    10
  37    -2    8
  38    5     13
  39    5     18
  40    9     27
  41    -2    25
  42    -16   9
  43    -2    7
  44    -7    0
  45    -7    -7
  46    5     -2
  47    -2    -4
  48    -11   -15
  49    2     -13
  50    -7    -20
  51    5     -15
  52    -7    -22
  53    -2    -24
  54    9     -15
  55    5     -10
  56    9     -1
  57    5     4
  58    5     9
  59    -2    7
  60    30    37
  61    -2    35
  62    5     40
  63    -7    33
  64    2     35
  65    5     40
  66    -16   24
  67    -2    22
  68    -7    15
  69    5     20
  70    -16   4
  71    -2    2
  72    -23   -21
  73    -2    -23
  74    5     -18
  75    -7    -25
  76    -7    -32
  77    5     -27
  78    -16   -43
  79    -2    -45
  80    -11   -56
  81    2     -54
  82    5     -49
  83    -2    -51
  84    30    -21
  85    5     -16
  86    5     -11
  87    5     -6
  88    9     3
  89    -2    1
  90    30    31
  91    5     36
  92    -7    29
  93    5     34
  94    5     39
  95    5     44
  96    13    57
  97    -2    55
  98    -7    48
  99    -7    41
  100   14    55
  101   -2    53
  102   -16   37
  103   -2    35
  104   9     44
  105   -16   28
  106   5     33
  107   -2    31
  108   -23   8
  109   -2    6
  110   -16   -10
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
  25    7      1.85714285714286      0.400000000000000   0.240000000000000
  50    -20    -0.200000000000000    0.360000000000000   0.300000000000000
  75    -25    0.000000000000000     0.426666666666667   0.293333333333333
  100   55     0.381818181818182     0.530000000000000   0.260000000000000
  125   -78    0.230769230769231     0.528000000000000   0.232000000000000
  150   76     -0.263157894736842    0.500000000000000   0.240000000000000
  175   -13    5.30769230769231      0.428571428571429   0.314285714285714
  200   -127   0.905511811023622     0.470000000000000   0.275000000000000
  225   91     -0.0549450549450549   0.484444444444444   0.271111111111111
  250   169    -0.319526627218935    0.440000000000000   0.344000000000000
  275   -40    2.32500000000000      0.400000000000000   0.356363636363636
  300   -192   0.703125000000000     0.396666666666667   0.326666666666667
  325   -167   0.874251497005988     0.443076923076923   0.301538461538462
  350   99     -0.656565656565657    0.440000000000000   0.291428571428571
  375   242    -0.528925619834711    0.410666666666667   0.333333333333333
  400   243    -0.238683127572016    0.385000000000000   0.375000000000000
  425   16     -5.93750000000000     0.362352941176471   0.397647058823529
  450   -268   0.716417910447761     0.360000000000000   0.377777777777778
  475   -334   0.476047904191617     0.393684210526316   0.357894736842105
  500   -336   0.535714285714286     0.424000000000000   0.340000000000000

Now within a detailed interval:

  465   -248   0.584677419354839   0.380645161290323   0.365591397849462
  466   -243   0.576131687242798   0.381974248927039   0.364806866952790
  467   -245   0.579591836734694   0.383297644539615   0.364025695931477
  468   -319   0.445141065830721   0.384615384615385   0.363247863247863
  469   -314   0.436305732484076   0.385927505330490   0.362473347547974
  470   -330   0.463636363636364   0.387234042553191   0.361702127659574
  471   -325   0.455384615384615   0.388535031847134   0.360934182590234
  472   -316   0.468354430379747   0.389830508474576   0.360169491525424
  473   -311   0.459807073954984   0.391120507399577   0.359408033826638
  474   -327   0.486238532110092   0.392405063291139   0.358649789029536
  475   -334   0.476047904191617   0.393684210526316   0.357894736842105
  476   -304   0.523026315789474   0.394957983193277   0.357142857142857
  477   -311   0.511254019292605   0.396226415094340   0.356394129979036
  478   -306   0.503267973856209   0.397489539748954   0.355648535564854
  479   -308   0.506493506493506   0.398747390396660   0.354906054279749
  480   -404   0.386138613861386   0.400000000000000   0.354166666666667
  481   -399   0.378446115288221   0.401247401247401   0.353430353430353
  482   -394   0.370558375634518   0.402489626556017   0.352697095435685
  483   -410   0.395121951219512   0.403726708074534   0.351966873706004
  484   -396   0.409090909090909   0.404958677685950   0.351239669421488
  485   -391   0.401534526854220   0.406185567010309   0.350515463917526
  486   -378   0.415343915343915   0.407407407407407   0.349794238683128
  487   -380   0.418421052631579   0.408624229979466   0.349075975359343
  488   -371   0.428571428571429   0.409836065573771   0.348360655737705
  489   -366   0.420765027322404   0.411042944785276   0.347648261758691
  490   -336   0.458333333333333   0.412244897959184   0.346938775510204
  491   -338   0.461538461538462   0.413441955193483   0.346232179226069
  492   -308   0.506493506493506   0.414634146341463   0.345528455284553
  493   -303   0.498349834983498   0.415821501014199   0.344827586206897
  494   -319   0.523510971786834   0.417004048582996   0.344129554655870
  495   -289   0.577854671280277   0.418181818181818   0.343434343434343
  496   -300   0.556666666666667   0.419354838709677   0.342741935483871
  497   -295   0.549152542372881   0.420523138832998   0.342052313883300
  498   -311   0.572347266881029   0.421686746987952   0.341365461847390
  499   -313   0.575079872204473   0.422845691382766   0.340681362725451
  500   -336   0.535714285714286   0.424000000000000   0.340000000000000
```
