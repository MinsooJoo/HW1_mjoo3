import numpy as np

# These functions below provide an implementation of a linear fitting of monomials to the data.

# Function that creates the X matrix as defined for fitting our model
def create_X(x,deg):
    X = np.ones((len(x),deg+1))
    for i in range(1,deg+1):
        X[:,i] = x**i
    return X

# Function for predicting the response
def predict(x,beta):
    return np.dot(create_X(x,len(beta)-1),beta)

# Function for fitting the model
def fit(x,y,deg):
    return np.linalg.lstsq(create_X(x,deg),y,rcond=None)[0]

# Function for computing the MSE
def rmse(y,yPred):
    se = (y-yPred)**2
    return np.sqrt(np.mean(se))