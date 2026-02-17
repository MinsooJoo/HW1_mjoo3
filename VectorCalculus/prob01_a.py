import numpy as np

def Df(x,y,z):
    
    ### <--- START OF YOUR CODE
    f_x = 12 * x**2 * y**2 - 2 * z**3 / x**3 - 16 * x**15
    f_y = 8 * x**3 * y - 4 * y**3 * np.exp(z) + 4
    f_z = -y**4 * np.exp(z) + 3 * z**2 / x**2
    ### END OF YOUR CODE --->

    return np.array([[f_x,f_y,f_z]])

def main():
    x = -1
    y = 0
    z = 2
    df = Df(x,y,z)
    
    print(df)
    print(df.shape)

if __name__ == "__main__":
    main()