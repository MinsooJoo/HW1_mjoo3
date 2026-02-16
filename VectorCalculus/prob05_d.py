import numpy as np
from prob05_a import Df
from prob05_b import Dg
from prob05_c import Dh

def f(z_1,z_2):
    return z_1*z_2 + 1

def g(y_1,y_2):
    return np.array([[y_1+2*y_2],[4*y_1-y_2]])

def h(x_1,x_2,x_3):
    return np.array([[np.exp(x_1)*np.cos(x_2)+x_3],[np.exp(x_1)*np.sin(x_2)+x_3]])

def dfogoh(x_1,x_2,x_3):
    
    ### <--- START OF YOUR CODE
    dfogoh = np.array(0)
    ### END OF YOUR CODE --->

    return dfogoh

def main():

    x_1,x_2,x_3=0,0,0

    print(dfogoh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()
