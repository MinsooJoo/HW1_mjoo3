from kfold_split import kfold_split
import sys
import numpy as np
import fncs

def test_firstTest():
  x = np.array([1, 2, 3, 4, 5, 6])
  y = np.array([1, 2, 3, 4, 5, 6])

  K = 6

  # Checking first fold
  x_preval, y_preval, x_val, y_val = kfold_split(x,y,K,0)
  tmp = np.array([2,3,4,5,6])
  assert(x_val==1 and y_val==1 and (x_preval==tmp).all() and (y_preval==tmp).all())

  # Checking fifth fold
  x_preval, y_preval, x_val, y_val = kfold_split(x,y,K,4)
  tmp = np.array([1,2,3,4,6])
  assert(x_val==5 and y_val==5 and (x_preval==tmp).all() and (y_preval==tmp).all())


def test_secondTest():
  x = np.array([1, 2, 3, 4, 5, 6])
  y = np.array([1, 2, 3, 4, 5, 6])
  
  K = 3

  # Checking first fold
  x_preval, y_preval, x_val, y_val = kfold_split(x,y,K,0)
  tmp = np.array([3,4,5,6])
  tmp_val = np.array([1,2])
  assert((x_val==tmp_val).all() and (y_val==tmp_val).all() and (x_preval==tmp).all() and (y_preval==tmp).all())

  # Checking third fold
  x_preval, y_preval, x_val, y_val = kfold_split(x,y,K,2)
  tmp = np.array([1,2,3,4])
  tmp_val = np.array([5,6])
  assert((x_val==tmp_val).all() and (y_val==tmp_val).all() and (x_preval==tmp).all() and (y_preval==tmp).all())
