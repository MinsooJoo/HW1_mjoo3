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
    
    # 1. calculate h(x) (=y)
    h_val = h(x_1, x_2, x_3)
    y_1 = h_val[0, 0]
    y_2 = h_val[1, 0]

    # 2. calculate g(y) (=z)
    g_val = g(y_1, y_2)
    z_1 = g_val[0, 0]
    z_2 = g_val[1, 0]

    # 3. calculate jacobian
    Dh_val = Dh(x_1, x_2, x_3)
    Dg_val = Dg(y_1, y_2)
    Df_val = Df(z_1, z_2)

    # 4. Chain rule: Df * Dg * Dh
    dfogoh = Df_val @ Dg_val @ Dh_val

    ### END OF YOUR CODE --->

    return dfogoh

def main():

    x_1,x_2,x_3=0,0,0

    print(dfogoh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()
