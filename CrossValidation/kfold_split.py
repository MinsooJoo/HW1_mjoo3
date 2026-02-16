import numpy as np

def kfold_split(x,y,K,kcurr):
    # Extracting number of samples in the data
    N = len(x)

    # Specifying the number of samples in a fold
    Nfold = int(np.floor(N/K))

    ### <--- START OF YOUR CODE

    idxVal = 0
    idxPreVal = 0

    ### END OF YOUR CODE --->

    x_preval = x[idxPreVal]
    y_preval = y[idxPreVal]

    x_val = x[idxVal]
    y_val = y[idxVal]

    return x_preval, y_preval, x_val, y_val
