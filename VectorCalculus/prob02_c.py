import numpy as np
from prob02_a import Df
from prob02_b import Du

def f(z1,z2):
    return (z1-z2)*np.exp(z1)

def u(x1,x2):
    return np.array([[x1*x2],[x1**2 - x2**2]])

def dfou(x_1,x_2):
    
    ### <--- START OF YOUR CODE
    u_val = u(x_1, x_2)
    z_1 = u_val[0, 0]
    z_2 = u_val[1, 0]

    Df_val = Df(z_1, z_2)
    Du_val = Du(x_1, x_2)

    dfou = Df_val @ Du_val
    ### END OF YOUR CODE --->

    return dfou

def main():

    x_1,x_2=1,3

    print(dfou(x_1,x_2))

if __name__ == "__main__":
    main()