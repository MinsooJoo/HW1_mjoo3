import prob05_b
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  y_1 = 1
  y_2 = 2

  Dg = np.array([[1,2],[4 , -1]])

  assert( fncs.AlmostEqual(Dg,prob05_b.Dg(y_1,y_2),3) )


# Checking for second set of values
def test_secondTest():
  y_1 = -1
  y_2 = 4

  Dg = np.array([[1,2],[4 , -1]])

  assert( fncs.AlmostEqual(Dg,prob05_b.Dg(y_1,y_2),3) )
