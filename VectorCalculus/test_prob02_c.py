import prob02_c
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x_1 = 0
  x_2 = 1

  dfou = np.array([[2., 2.]])

  assert( fncs.AlmostEqual(dfou,prob02_c.dfou(x_1,x_2),3) )


# Checking for second set of values
def test_secondTest():
  x_1 = 1
  x_2 = 3

  dfou = np.array([[682.90825539 ,361.53966462]])

  assert( fncs.AlmostEqual(dfou,prob02_c.dfou(x_1,x_2),3) )
