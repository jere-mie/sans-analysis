# functions regarding the generation/reading/etc of the different matrices
import numpy as np
import struct
from scipy.integrate import quad
from scipy.special import spherical_jn as jn

# generating D, M, O, T (O=Omega, T=Theta)
def generateDMOT(r,s,ps,t,z,d,m):
    Dmat = np.full((len(r),len(s)), ps)
    Mmat = np.full((len(r),len(s)), ps)

    # Dmat stuff
    for i in range(len(s)):
        for j in range(len(r)):
            if r[j] == t[i]+z[0]+1:
                for elem in d:
                    Dmat[j][i] = elem
                    j+=1

    # Mmat stuff
    for i in range(len(s)):
        for j in range(len(r)):
            if r[j] == t[i]+z[0]+1:
                for elem in m:
                    Mmat[j][i] = elem
                    j+=1

    Omat = Dmat-Mmat
    Tmat = Mmat - ps
    return (Dmat, Mmat, Omat, Tmat)

# fname=filename, dimensions=array or tuple of dimensions (dimensions = [a,b,c] => F[a][b][c])
def readFText(fname, dimensions):
    f = open(fname, 'r')
    F = f.read()
    f.close()
    F = F.split(' ')
    F = F[0:len(F)-1]
    for i in range(len(F)):
        F[i] = float(F[i])
    # we used to reshape to len(w)+1, len(q), len(r)
    F = np.array(F).reshape(dimensions[0], dimensions[1], dimensions[2])
    return F

def readFBin(fname, dimensions):
    tot = dimensions[0]*dimensions[1]*dimensions[2]
    F = np.zeros(tot)
    with open(fname, 'rb') as f:
        for i in range(tot):
            F[i] = struct.unpack('f', f.read(4))[0]
    # this is the old reshaping: F = F.reshape(100, 1900, 500)
    F = F.reshape(dimensions[0], dimensions[1], dimensions[2])
    return F

def generateF(rlower, rstep, numr, qlower, qstep, numq, llower, lstep, numl):
    # helper function for integrating
    def integrand(x,l):
        return jn(l,x) * x**2

    # performs the necessary integration to create F elements
    def integrated(q,r1,r2,l):
        return (q**-3)*(quad(integrand,q*r1,q*r2, args=(l))[0])

    rl = rlower
    ql = qlower
    elems = 0

    F = []
    for i in range(numl):
        qlower = ql
        rlower = rl
        for j in range(numq):
            rlower = rl
            for k in range(numr):
                elems+=1
                F.append(integrated(qlower,rlower,rlower+rstep,llower))
                rlower+=rstep
            qlower+=qstep
        llower+=lstep
        print(f"{i+1} of {numl}")
    return F

# generates F matrix, but nothing inputted, so user is asked for values
def generateFPrompt():
    rlower = int(input("R lower bound: "))
    rstep = int(input("R step: "))
    numr = int(input("Number of R Elements: "))

    qlower = float(input("Q lower bound: "))
    qstep = float(input("Q step: "))
    numq = int(input("Number of Q Elements: "))

    llower = int(input("L lower bound: "))
    lstep = int(input("L step: "))
    numl = int(input("Number of L Elements: "))
    return generateF(rlower, rstep, numr, qlower, qstep, numq, llower, lstep, numl)


# writes F to a text file, separated by spaces 
def writeFText(fname, F):
    with open(fname, 'w') as f:
        for i in range(len(F)):
            for j in range(len(F[i])):
                for k in range(len(F[i][j])):
                    f.write(f'{F[i][j][k]} ')

# writes F to a binary file
def writeFBin(fname, F):
    with open(fname, 'wb') as f:
        for i in F:
            f.write(struct.pack('f', i))
