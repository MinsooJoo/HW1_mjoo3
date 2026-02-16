import prob05_d
import sys
import numpy as np
import fncs

# Checking for a first set of values
def test_firstTest():
  x_1 = 0
  x_2 = 0
  x_3 = 0

  dfogoh = np.array([[ 8 , 7 , 15]])

  assert( fncs.AlmostEqual(dfogoh,prob05_d.dfogoh(x_1,x_2,x_3),3) )


# Checking for second set of values
def test_secondTest():
  x_1 = 1
  x_2 = 1
  x_3 = 1

  dfogoh = np.array([[ 72.25294112, -91.74187192, 46.89247496]])

  assert( fncs.AlmostEqual(dfogoh,prob05_d.dfogoh(x_1,x_2,x_3),3) )
