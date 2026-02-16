import numpy as np

def Df(u,v,p,t):
    
    ### <--- START OF YOUR CODE

    f_u = 0
    f_v = 0
    f_p = 0
    f_t = 0

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