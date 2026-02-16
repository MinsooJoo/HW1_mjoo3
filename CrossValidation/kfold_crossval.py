import numpy as np
import polyfit as pf
from kfold_split import kfold_split

def kfold_crossval(x_train,y_train,degList,K):
    # Initializing range of degree values to be tested and errors.
    # Make sure your output has these dimensions.
    errPreVal = np.zeros((len(degList),K))
    errVal = np.zeros((len(degList),K))

    for i in range(0,K):
        x_preval, y_preval, x_val, y_val = kfold_split(x_train,y_train,K,i)

        # Computing pre-validation training and validation RMSE for each degree value

        ### <--- START OF YOUR CODE

        #...

        ### END OF YOUR CODE --->

    return errPreVal, errVal