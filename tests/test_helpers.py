# the following adds '../' to the python path to allow for me to import from calculations
from numpy import angle
from utils import updatePath, almost_equals
updatePath()

from calculations.helpers import e26, alpha, sum_Cl, angle_between, generate_angles

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

# test angle_between with the same vector
def test_angle_between_same_vector():
    v1 = [1,1,1]
    v2 = [1,1,1]
    assert(almost_equals(angle_between(v1, v2), 0))

# test angle_between with different vectors
def test_angle_between_different_vectors():
    v1 = [1,1,1]
    v2 = [1,1,2]
    assert(almost_equals(angle_between(v1, v2), 0.33984))

# tests fred's angles
def test_angles_fred():
    vectors = [
        [0, 0, 1],
        [-0.4714045208, -0.8164965809, -0.3333333333],
        [-0.4714045208, 0.8164965809, -0.3333333333],
        [0.9428090416, 0, -0.3333333333]
    ]
    angles = [
        [0, 1.9106, 1.9106, 1.9106],
        [1.9106, 0, 1.9106, 1.9106],
        [1.9106, 1.9106, 0, 1.9106],
        [1.9106, 1.9106, 1.9106, 0]
    ]
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            assert(almost_equals(angle_between(vectors[i], vectors[j]), angles[i][j], 0.0001))

def test_gen_angles():
    vectors = [
        [0, 0, 1],
        [-0.4714045208, -0.8164965809, -0.3333333333],
        [-0.4714045208, 0.8164965809, -0.3333333333],
        [0.9428090416, 0, -0.3333333333]
    ]
    expected = [
        [0, 1.9106, 1.9106, 1.9106],
        [1.9106, 0, 1.9106, 1.9106],
        [1.9106, 1.9106, 0, 1.9106],
        [1.9106, 1.9106, 1.9106, 0]
    ]
    angles = generate_angles(vectors)
    for i in range(len(angles)):
        for j in range(len(angles)):
            assert(almost_equals(angles[i][j], expected[i][j]))