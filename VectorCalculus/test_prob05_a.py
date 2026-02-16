import prob05_a
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  z_1 = 1
  z_2 = 2

  Df = np.array([[ 2 , 1]])

  assert( fncs.AlmostEqual(Df,prob05_a.Df(z_1,z_2),3) )


# Checking for second set of values
def test_secondTest():
  z_1 = -1
  z_2 = 4

  Df = np.array([[ 4,-1]])

  assert( fncs.AlmostEqual(Df,prob05_a.Df(z_1,z_2),3) )
