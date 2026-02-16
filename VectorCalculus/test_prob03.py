import prob03
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x = -1

  dinvA = np.array([[ 0.40625 , 0.21875 ],[-1.140625 , 0.078125]])

  assert( fncs.AlmostEqual(dinvA,prob03.dinvA(x),3) )
  

# Checking for second set of values
def test_secondTest():
  x = 1

  dinvA = np.array([[ 0.11728395, -0.29012346],[-0.23765432 , 0.11419753]])

  assert( fncs.AlmostEqual(dinvA,prob03.dinvA(x),3) )
