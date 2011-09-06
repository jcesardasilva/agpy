# coding: utf-8
from agpy import readcol
import plfit

blackouts = readcol('blackouts.txt')
cities = readcol('cities.txt')
earthquakes = readcol('earthquakes.txt')
melville = readcol('melville.txt')
solarflares = readcol('solarflares.txt')
terrorism = readcol('terrorism.txt')

#print "quakes 0.00 -7.14 0.00 11.6 0.00 -7.09 0.00 -24.4 0.00 with cut-oﬀ"
#earthquakeP = plfit.plfit(earthquakes)


pl = plfit.plfit(cities.ravel() / 1e3, usefortran=True)
print "Cities (me)     : n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (pl.data.shape[0], pl.data.mean(), pl.data.std(), pl.data.max(), pl._xmin, pl._alpha, pl._ngtx, pl._ks_prob)
print "Cities (Clauset): n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (19447,9.00,77.83,8009,52.46,2.37,580,0.76)

pl = plfit.plfit(melville.ravel())
p,sims = pl.test_pl(usefortran=True, niter=100)
print "Melville (me)     : n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (pl.data.shape[0], pl.data.mean(), pl.data.std(), pl.data.max(), pl._xmin, pl._alpha, pl._ngtx, p)
print "Melville (Clauset): n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (18855,11.14,148.33,14086,7,1.95,2958,0.49)
# count of word use 18 855 11.14 148.33 14 086 7 ± 2 1.95(2) 2958 ± 987 0.49
# words 0.49 4.43 0.00 0.395 0.69 9.09 0.00 4.13 0.00 −0.899 0.18 goo
#
pl = plfit.plfit(solarflares.ravel())
p,sims = pl.test_pl(usefortran=True, niter=100)
print "Solarflares (me)     : n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (pl.data.shape[0], pl.data.mean(), pl.data.std(), pl.data.max(), pl._xmin, pl._alpha, pl._ngtx, p)
print "Solarflares (Clauset): n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (12773, 689.41, 6520.59, 231300, 323, 1.79, 1711, 1.00)

pl = plfit.plfit(terrorism.ravel())
p,sims = pl.test_pl(usefortran=True, niter=100)
print "Terrorism (me)     : n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (pl.data.shape[0], pl.data.mean(), pl.data.std(), pl.data.max(), pl._xmin, pl._alpha, pl._ngtx, p)
print "Terrorism (Clauset): n:%10i mean,std,max: %8.2f,%8.2f,%8.2f xmin: %8.2f alpha: %8.2f ntail: %10i p: %5.2f" % (9101, 4.35, 31.58, 2749, 12, 2.4, 547, 0.68)


# """
# power law log-normal exponential stretched exp. power law + cut-oﬀ support for
# data set p LR p LR p LR p LR p power law
# birds 0.55 -0.850 0.40 1.87 0.06 -0.882 0.38 -1.24 0.12 moderate
# blackouts 0.62 -0.412 0.68 1.21 0.23 -0.417 0.68 -0.382 0.38 moderate
# book sales 0.66 -0.267 0.79 2.70 0.01 3.885 0.00 -0.140 0.60 moderate
# cities 0.76 -0.090 0.93 3.65 0.00 0.204 0.84 -0.123 0.62 moderate
# ﬁres 0.05 -1.78 0.08 4.00 0.00 -1.82 0.07 -5.02 0.00 with cut-oﬀ
# ﬂares 1.00 -0.803 0.42 13.7 0.00 -0.546 0.59 -4.52 0.00 with cut-oﬀ
# HTTP 0.00 1.77 0.08 11.8 0.00 2.65 0.01 0.000 1.00 none
# quakes 0.00 -7.14 0.00 11.6 0.00 -7.09 0.00 -24.4 0.00 with cut-oﬀ
# religions 0.42 -0.073 0.94 1.59 0.11 1.75 0.08 -0.167 0.56 moderate
# surnames 0.20 -0.836 0.40 2.89 0.00 -0.844 0.40 -1.36 0.10 with cut-oﬀ
# wars 0.20 -0.737 0.46 3.68 0.00 -0.767 0.44 -0.847 0.19 moderate
# wealth 0.00 0.249 0.80 6.20 0.00 8.05 0.00 -0.142 0.59 none
# web hits 0.00 -10.21 0.00 8.55 0.00 10.94 0.00 -74.66 0.00 with cut-oﬀ
# web links 0.00 -2.24 0.03 25.3 0.00 -1.08 0.28 -21.2 0.00 with cut-o
# 
# 
# 
# Poisson log-normal exponential stretched exp. power law + cut-oﬀ support for
# data set p LR p LR p LR p LR p LR p power law
# Internet 0.29 5.31 0.00 −0.807 0.42 6.49 0.00 0.493 0.62 −1.97 0.05 with cut-oﬀ
# calls 0.63 17.9 0.00 −2.03 0.04 35.0 0.00 14.3 0.00 −30.2 0.00 with cut-oﬀ
# citations 0.20 6.54 0.00 −0.141 0.89 5.91 0.00 1.72 0.09 −0.007 0.91 moderate
# email 0.16 4.65 0.00 −1.10 0.27 0.639 0.52 −1.13 0.26 −1.89 0.05 with cut-oﬀ
# metabolic 0.00 3.53 0.00 −1.05 0.29 5.59 0.00 3.66 0.00 0.000 1.00 none
# papers 0.90 5.71 0.00 −0.091 0.93 3.08 0.00 0.709 0.48 −0.016 0.86 moderate
# proteins 0.31 3.05 0.00 −0.456 0.65 2.21 0.03 0.055 0.96 −0.414 0.36 moderate
# species 0.10 5.04 0.00 −1.63 0.10 2.39 0.02 −1.59 0.11 −3.80 0.01 with cut-oﬀ
# terrorism 0.68 1.81 0.07 −0.278 0.78 2.457 0.01 0.772 0.44 −0.077 0.70 moderate
# words 0.49 4.43 0.00 0.395 0.69 9.09 0.00 4.13 0.00 −0.899 0.18 goo
#
#
#
#
# quantity n hxi σ xmax xˆmin α n ˆ tail p
# count of word use 18 855 11.14 148.33 14 086 7 ± 2 1.95(2) 2958 ± 987 0.49
# protein interaction degree 1846 2.34 3.05 56 5 ± 2 3.1(3) 204 ± 263 0.31
# metabolic degree 1641 5.68 17.81 468 4 ± 1 2.8(1) 748 ± 136 0.00
# Internet degree 22 688 5.63 37.83 2583 21 ± 9 2.12(9) 770 ± 1124 0.29
# telephone calls received 51 360 423 3.88 179.09 375 746 120 ± 49 2.09(1) 102 592 ± 210 147 0.63
# intensity of wars 115 15.70 49.97 382 2.1 ± 3.5 1.7(2) 70 ± 14 0.20
# terrorist attack severity 9101 4.35 31.58 2749 12 ± 4 2.4(2) 547 ± 1663 0.68
# HTTP size (kilobytes) 226 386 7.36 57.94 10 971 36.25 ± 22.74 2.48(5) 6794 ± 2232 0.00
# species per genus 509 5.59 6.94 56 4 ± 2 2.4(2) 233 ± 138 0.10
# bird species sightings 591 3384.36 10 952.34 138 705 6679 ± 2463 2.1(2) 66 ± 41 0.55
# blackouts (×10
# 3
# ) 211 253.87 610.31 7500 230 ± 90 2.3(3) 59 ± 35 0.62
# sales of books (×10
# 3
# ) 633 1986.67 1396.60 19 077 2400 ± 430 3.7(3) 139 ± 115 0.66
# population of cities (×10
# 3
# ) 19 447 9.00 77.83 8 009 52.46 ± 11.88 2.37(8) 580 ± 177 0.76
# email address books size 4581 12.45 21.49 333 57 ± 21 3.5(6) 196 ± 449 0.16
# forest ﬁre size (acres) 203 785 0.90 20.99 4121 6324 ± 3487 2.2(3) 521 ± 6801 0.05
# solar ﬂare intensity 12 773 689.41 6520.59 231 300 323 ± 89 1.79(2) 1711 ± 384 1.00
# quake intensity (×10
# 3
# ) 19 302 24.54 563.83 63 096 0.794 ± 80.198 1.64(4) 11 697 ± 2159 0.00
# religious followers (×10
# 6
# ) 103 27.36 136.64 1050 3.85 ± 1.60 1.8(1) 39 ± 26 0.42
# freq. of surnames (×10
# 3
# ) 2753 50.59 113.99 2502 111.92 ± 40.67 2.5(2) 239 ± 215 0.20
# net worth (mil. USD) 400 2388.69 4 167.35 46 000 900 ± 364 2.3(1) 302 ± 77 0.00
# citations to papers 415 229 16.17 44.02 8904 160 ± 35 3.16(6) 3455 ± 1859 0.20
# papers authored 401 445 7.21 16.52 1416 133 ± 13 4.3(1) 988 ± 377 0.90
# hits to web sites 119 724 9.83 392.52 129 641 2 ± 13 1.81(8) 50 981 ± 16 898 0.00
# links to web sites 241 428 853 9.15 106 871.65 1 199 466 3684 ± 151 2.336(9) 28 986 ± 1560 0.00
# 
# 
# Poisson log-normal exponential stretched exp. power law + cut-oﬀ support for
# data set p LR p LR p LR p LR p LR p power law
# Internet 0.29 5.31 0.00 −0.807 0.42 6.49 0.00 0.493 0.62 −1.97 0.05 with cut-oﬀ
# calls 0.63 17.9 0.00 −2.03 0.04 35.0 0.00 14.3 0.00 −30.2 0.00 with cut-oﬀ
# citations 0.20 6.54 0.00 −0.141 0.89 5.91 0.00 1.72 0.09 −0.007 0.91 moderate
# email 0.16 4.65 0.00 −1.10 0.27 0.639 0.52 −1.13 0.26 −1.89 0.05 with cut-oﬀ
# metabolic 0.00 3.53 0.00 −1.05 0.29 5.59 0.00 3.66 0.00 0.000 1.00 none
# papers 0.90 5.71 0.00 −0.091 0.93 3.08 0.00 0.709 0.48 −0.016 0.86 moderate
# proteins 0.31 3.05 0.00 −0.456 0.65 2.21 0.03 0.055 0.96 −0.414 0.36 moderate
# species 0.10 5.04 0.00 −1.63 0.10 2.39 0.02 −1.59 0.11 −3.80 0.01 with cut-oﬀ
# terrorism 0.68 1.81 0.07 −0.278 0.78 2.457 0.01 0.772 0.44 −0.077 0.70 moderate
# words 0.49 4.43 0.00 0.395 0.69 9.09 0.00 4.13 0.00 −0.899 0.18 goo
# # 
# """


