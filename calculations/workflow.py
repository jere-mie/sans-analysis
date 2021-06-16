import numpy as np

def step1(F, Omat):
    Wp = [] # initializing

    for i in range(len(F)): # doing matrix multiplication
        Wp.append(F[i].dot(Omat))

    Wp = np.array(Wp) # making np array so we can swap axes
    Wp = np.swapaxes(Wp, 0, 2) # swapping axes
    return Wp

def step2(Wp, w):
    # Wp = |Wp^2|
    for i in range(len(Wp)):
        for j in range(len(Wp[0])):
            for k in range(len(Wp[0][0])):
                Wp[i][j][k] = np.abs(Wp[i][j][k]**2)
    Imon = [] # initializing
    for i in range(len(Wp)):
        Imon.append(Wp[i].dot(w))
    Imon = np.array(Imon)
    return Imon

def step3(Imon, s):
    Imon = np.swapaxes(Imon,0,1) # swapping axes
    ipoly = Imon.dot(s) # dotting and making the out curve
    return ipoly

# generates homogeneous curve
def homo(F0, Omat, Tmat, s, ad):
    H0 = F0.dot(Tmat)
    K0 = F0.dot(Omat)
    Ihom = np.zeros(len(H0)*len(H0[0])).reshape(len(H0),len(H0[0]))
    s = np.array(s)

    sqrpi = np.longdouble(np.sqrt(np.pi))
    sqrpiby2 = np.longdouble(sqrpi*2)

    for i in range(len(H0)):
        for j in range(len(H0[0])):
            p1 = np.longdouble(sqrpiby2*H0[i][j])
            p2 = 2*ad*sqrpi
            p2*=K0[i][j]
            psum = p1+p2
            Ihom[i][j] = np.longdouble(np.power(psum,2))

    # generating ihom and fhom
    ihom = Ihom.dot(s)

    fhom = np.zeros(len(ihom))
    for i in range(len(Ihom)):
        fhom[i] = np.longdouble(0)
        for j in range(len(Ihom[i])):
            fhom[i]+=(s[j]*np.sqrt(Ihom[i][j]))    

    return (ihom, fhom)

