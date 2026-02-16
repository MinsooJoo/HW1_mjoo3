import numpy as np

def kfold_split(x,y,K,kcurr):
    # Extracting number of samples in the data
    N = len(x)

    # Specifying the number of samples in a fold
    Nfold = int(np.floor(N/K))

    ### <--- START OF YOUR CODE
    start_idx = kcurr * Nfold

    if kcurr == K-1:
        end_idx = N
    else:
        end_idx = (kcurr + 1) * Nfold

    idxVal = np.arange(start_idx, end_idx)
    idxPreVal = np.setdiff1d(np.arange(N), idxVal)

    ### END OF YOUR CODE --->

    x_preval = x[idxPreVal]
    y_preval = y[idxPreVal]

    x_val = x[idxVal]
    y_val = y[idxVal]

    return x_preval, y_preval, x_val, y_val
