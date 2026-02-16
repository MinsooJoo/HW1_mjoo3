import prob01_a
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x = 2
  y = 4
  z = -1

  Df = np.array([-5.23519750e+05, 1.65822863e+02, -9.34271369e+01])

  assert fncs.AlmostEqual(Df,prob01_a.Df(x,y,z),3)


# Checking for a second set of values
def test_secondTest():
  x = -1
  y = 0
  z = 2

  Df = np.array([32,  4, 12.])

  assert fncs.AlmostEqual(Df,prob01_a.Df(x,y,z),3)
