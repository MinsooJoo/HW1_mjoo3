import prob02_a
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  z_1 = 0
  z_2 = 1

  Df = np.array([[0,-1]])

  assert( fncs.AlmostEqual(Df,prob02_a.Df(z_1,z_2),3) )


# Checking for second set of values
def test_secondTest():
  z_1 = 1
  z_2 = 1

  Df = np.array([[ 2.71828183 ,-2.71828183]])

  assert( fncs.AlmostEqual(Df,prob02_a.Df(z_1,z_2),3) )
