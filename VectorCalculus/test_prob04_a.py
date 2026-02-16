import prob04_a
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  t = 0

  dA2dt = np.array([[4,7],[7,4]])

  assert( fncs.AlmostEqual(dA2dt,prob04_a.dA2dt(t),3) )


# Checking for second set of values
def test_secondTest():
  t = 1

  dA2dt = np.array([[17,12],[42,13]])

  assert( fncs.AlmostEqual(dA2dt,prob04_a.dA2dt(t),3) )
