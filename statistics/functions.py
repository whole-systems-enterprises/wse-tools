from numpy import std, sqrt
from numpy import mean

#
# compute pooled standard deviation for two groups
#
def pooled_standard_deviation(list_1, list_2):
    n1 = float(len(list_1))
    n2 = float(len(list_2))
    s1 = std(list_1)
    s2 = std(list_2)
    s = sqrt(((n1 - 1.) * s1**2. + (n2 - 1.) * s2**2.) / (n1 + n2 - 2.))
    return s

#
# compute Cohen's d for two groups
#
def cohen_d(list_1, list_2):
    s = pooled_standard_deviation(list_1, list_2)
    u1 = mean(list_1)
    u2 = mean(list_2)
    d = (u1 - u2) / s
    return d
