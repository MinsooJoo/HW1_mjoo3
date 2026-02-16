import numpy as np
import sys
import os
from kfold_crossval import kfold_crossval
import fncs

def test_crossval():
  # Loading training and test data
  script_dir = os.path.dirname(os.path.abspath(__file__))
  x_train = np.loadtxt(os.path.join(script_dir,'Data/x_train.csv'),delimiter=',')
  y_train = np.loadtxt(os.path.join(script_dir,'Data/y_train.csv'),delimiter=',')

  # List of degrees considered for the analysis
  degList =  np.array([0,1,2,3,4,5,6,7,8,9,10])

  # This is the total number of folds
  K = 10

  # Getting arrays with the errors for all folds. We keep track of all errors so
  # the mean and standard deviation can be computed below.
  errPreVal, errVal = kfold_crossval(x_train,y_train,degList,K)

  # Checking dimensions
  assert((errPreVal.shape==(len(degList),K)) and (errVal.shape==(len(degList),K)))

  # Checking for single values
  assert(fncs.AlmostEqual(errVal[3,3],0.0780,4))
  assert(fncs.AlmostEqual(errPreVal[5,5],0.0977,4))
