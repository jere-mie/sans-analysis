# functions related to construction of the w vector
import numpy as np
import random
from scipy.special import eval_legendre as lg

# equation 26 function, from Fred's paper
def e26(l, ad):
    a = (np.power(np.pi*(2.0*l + 1.0), (1.0/2.0)))/float(l)
    b = np.cos(ad)*lg(int(l), np.cos(ad))
    c = lg(int(l+1), np.cos(ad))
    return a*(b-c)

# given ad and number of domains, calculated alphad
# ad is the TOTAL domain area fraction
def alpha(n, ad):
    return (np.arccos(1-((2.0*ad)/n)))

# this gives the sum of each Cl matrix. Since we don't actually need the 
# Cl matrix itself, we only use the sum
def sum_Cl(wl, angles, nd, ad, l):
    tot = 0
    for i in range(nd):
        for j in range(nd):
            tot+= (np.abs(wl)**2) * lg(l, np.cos(angles[i][j]))
    return tot

# returns the angle between two vectors
def angle_between(vector1, vector2):
    v1_u = vector1 / np.linalg.norm(vector1)
    v2_u = vector2 / np.linalg.norm(vector2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

# generates a matrix of angles based on an input list of vectors
def generate_angles(vectors):
    angles = np.zeros(len(vectors)**2).reshape(len(vectors), len(vectors))
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            angles[i][j] = angle_between(vectors[i], vectors[j])
    return angles

# returns true if the domains overlap, false otherwise
# u and v are domain center vectors (numpy arrays)
# ~~au and av are the domain half angles~~
# we're going to just use one alpha instead
def domainsOverlap(u, v, alphad):
    return np.arccos(np.dot(u, v) / (np.linalg.norm(u)*np.linalg.norm(v))) < (2*alphad)

def anyOverlap(vectors, trial, alphad):
    for i in vectors:
        if domainsOverlap(i, trial, alphad):
            return True
    return False

# creates and returns a random point on a sphere
# essentially, generates our trial domain
# this will generate (x, y, z) coords
def randomSpherePt(radius):
    u = random.random()
    v = random.random()
    phi = np.arccos(2*v-1)
    theta = 2*np.pi*u
    return np.array([np.cos(theta)*np.sin(phi), (np.sin(theta)*np.sin(phi)),  (np.cos(phi))])

# returns a list of domain center vectors
def randomDomainCentres(n, ad):
    alphad = alpha(n=n, ad=ad)
    vectors = [randomSpherePt(1)]
    for i in range(n-1):
        trialpt = randomSpherePt(1)
        while anyOverlap(vectors, trialpt, alphad):
            trialpt = randomSpherePt(1)
        vectors.append(trialpt)
    return vectors

#############################

# ARCHIVED FUNCTIONS, NO
# LONGER USED!

#############################

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
