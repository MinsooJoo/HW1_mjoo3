import numpy as np

def Df(u,v,p,t):
    
    ### <--- START OF YOUR CODE

    f_u = 16 * u * t**3 * p + 4 * u * t
    f_v = -0.5 * v**(-0.5) * p**2 * t**(-5) - 1
    f_p = 8 * u**2 * t**3 - 2 * np.sqrt(v) * p * t**(-5) + 12 * p**3
    f_t = 24 * u**2 * t**2 * p + 5 * np.sqrt(v) * p**2 * t**(-6) + 2 * u**2

    ### END OF YOUR CODE --->
    return np.array([[f_u,f_v,f_p,f_t]])

def main():
    u = 1
    v = 1
    p = 1
    t = 1
    print(Df(u,v,p,t))

if __name__ == "__main__":
    main()