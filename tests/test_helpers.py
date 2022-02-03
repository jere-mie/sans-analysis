# the following adds '../' to the python path to allow for me to import from calculations
from testUtils import updatePath, almost_equals
updatePath()

from calculations.helpers import e26, alpha, sum_Cl

# tests e26 and sum
def test_e26_and_sumCl():
    expected = [0, 0, 1.025704585, 0.3820158745, 0]
    l = [1,2,3,4,5]
    ad = 0.2
    nd = 4
    angles = [
        [0, 1.9106, 1.9106, 1.9106],
        [1.9106, 0, 1.9106, 1.9106],
        [1.9106, 1.9106, 0, 1.9106],
        [1.9106, 1.9106, 1.9106, 0]
    ]
    wl0 = [e26(i, alpha(nd, ad)) for i in l]
    for i in range(len(l)):
        assert(almost_equals(sum_Cl(wl0[i], angles, nd, ad, l[i]), expected[i]))