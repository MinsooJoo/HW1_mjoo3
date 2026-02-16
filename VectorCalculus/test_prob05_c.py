import prob05_c
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x_1 = 0
  x_2 = 0
  x_3 = 0

  Dh = np.array([[1,0,1],[0 , 1, 1]])

  assert( fncs.AlmostEqual(Dh,prob05_c.Dh(x_1,x_2,x_3),3) )


# Checking for second set of values
def test_secondTest():
  x_1 = 0
  x_2 = 1
  x_3 = 1

  Dh = np.array([[0.54030231, -0.84147098 , 1],[0.84147098,  0.54030231,  1]])

  assert( fncs.AlmostEqual(Dh,prob05_c.Dh(x_1,x_2,x_3),3) )
