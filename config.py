import numpy as np
import pandas as pd
from scipy.stats import mode

def get_mols(numbers, target, mass_range, partial=[], partial_sum=0):
    x1 = target + mass_range
    x2 = target - mass_range
    if mode(partial)[1] > 30:
        return
    if (partial_sum <= x1) and (partial_sum >= x2):
        yield partial
    if partial_sum >= x1:
        return
    for n in numbers:
        c = int((x1 - partial_sum)// n )
        i = numbers.index(n)
        if c == 0:
            continue
        yield from get_mols(numbers[i+1:], target, mass_range,
                            partial + [n]*c, partial_sum + n*c)

atomic_mass={
12.000000:       'C',
13.003355:     '¹³C',
14.003074:       'N',
15.000109:  '¹⁵N',
15.994915:       'O',
16.999131:  '¹⁷O',
17.999159:  '¹⁸O',
 1.007825:       'H',
 2.014102:      '²H',
 3.016029:     '³He',
 4.002603:      'He',
 6.015123:      'Li',
 7.016005:     '⁷Li',
 9.012183:      'Be',
10.012938:       'B',
11.009305:     '¹¹B',
18.998403:       'F',
19.992439:      'Ne',
20.993845: '²¹Ne',
21.991384: '²²Ne',
22.989770:      'Na',
23.985045:      'Mg',
24.985839: '²⁵Mg',
25.982595: '²⁶Mg',
26.981541:      'Al',
27.976928: '²⁸Si',
28.976496: '²⁹Si',
29.973772: '³⁰Si',
30.973763:       'P',
31.972072:  '³²S',
32.971459:  '³³S',
33.967868:  '³⁴S',
34.968853: '³⁵Cl',
35.967079:  '³⁶S',
35.967546:      'Ar',
36.965903: '³⁷Cl',
37.962732: '³⁸Ar',
38.963708:       'K',
39.962383: '⁴⁰Ar',
39.962591: '⁴⁰Ca',
39.963999:  '⁴⁰K',
40.961825:  '⁴¹K',
41.958622: '⁴²Ca',
42.958770: '⁴³Ca',
43.955485: '⁴⁴Ca',
53.939612: '⁵⁴Fe',
55.934939: '⁵⁶Fe',
56.935396: '⁵⁷Fe',
57.935347: '⁵⁸Ni'
}
