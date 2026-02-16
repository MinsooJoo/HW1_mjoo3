import prob01_b
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  u = -1
  v = 1
  p = 2
  t = 1

  Df = np.array([-36,  -3, 100,  70])

  assert( fncs.AlmostEqual(Df,prob01_b.Df(u,v,p,t),3) )


# Checking for a second set of values
def test_secondTest():
  u = 1
  v = 1
  p = 1
  t = 1

  Df = np.array([20, -1.5, 18, 31 ])

  assert( fncs.AlmostEqual(Df,prob01_b.Df(u,v,p,t),3) )
