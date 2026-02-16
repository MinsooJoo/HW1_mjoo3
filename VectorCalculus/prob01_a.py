import numpy as np

def Df(x,y,z):
    
    ### <--- START OF YOUR CODE

    f_x = 0
    f_y = 0
    f_z = 0

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