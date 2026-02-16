import prob02_b
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x_1 = 1
  x_2 = 1

  Du = np.array([[ 1  ,1],[ 2 ,-2]])

  assert( fncs.AlmostEqual(Du,prob02_b.Du(x_1,x_2),3) )


# Checking for second set of values
def test_secondTest():
  x_1 = 1
  x_2 = -1

  Du = np.array([[-1 , 1],[ 2 , 2]])

  assert( fncs.AlmostEqual(Du,prob02_b.Du(x_1,x_2),3) )
