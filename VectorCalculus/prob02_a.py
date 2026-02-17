import numpy as np

def Df(z_1,z_2):
    
    ### <--- START OF YOUR CODE
 
    Df = np.array([[(1 + z_1 - z_2) * np.exp(z_1), -np.exp(z_1)]])
    ### END OF YOUR CODE --->

    return Df

def main():
    z_1 = 1
    z_2 = 1
    print(Df(z_1,z_2))

if __name__ == "__main__":
    main()