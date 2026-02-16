import numpy as np

def AlmostEqual(P, Q, digits):
    epsilon = 10 ** -digits
    return np.linalg.norm(P-Q) < epsilon
