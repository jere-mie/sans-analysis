# functions related to construction of the w vector
import numpy as np
from scipy.special import eval_legendre as lg

# equation 26 function
def e26(l, ad):
    a = (np.power(np.pi*(2.0*l + 1.0), (1.0/2.0)))/float(l)
    b = np.cos(ad)*lg(int(l), np.cos(ad))
    c = lg(int(l+1), np.cos(ad))
    return a*(b-c)

# given ad and number of domains, calculated alphad
# I believe ad is the domain area fraction of EACH domain
    # should confirm with fred
def alpha(n, ad):
    return (np.arccos(1-((2.0*ad)/n)))

# given number of domains and the domain area fraction, creates the corresponding w vector
# w vector is from 1 to 99 inclusive
def create_w(n, ad):
    w = []
    ealpha = alpha(n, ad)
    for i in range(1,100):
        w.append(np.abs(e26(i, ealpha))**2)
    return w

# returns the y value associated with a particular l, alphad, and ad value
# not used in final workflow, but useful for testing against the paper
def y(l, alphad, ad):
    return (abs(e26(l, alphad))**2)/ad


def sum_Cl(wl, angles, nd, ad, l):
    tot = 0
    for i in range(nd):
        for j in range(nd):
            tot+= (np.abs(wl)**2) * lg(l, np.cos(angles[i][j]))
    return tot
