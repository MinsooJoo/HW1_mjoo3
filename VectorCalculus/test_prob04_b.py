import prob04_b
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x = -1

  d2Bdt2 = np.array([-3.73469])

  assert( fncs.AlmostEqual(d2Bdt2,prob04_b.d2Bdt2(x),3) )


# Checking for second set of values
def test_secondTest():
  x = 0

  d2Bdt2 = np.array([-5.77778])

  assert( fncs.AlmostEqual(d2Bdt2,prob04_b.d2Bdt2(x),3) )
