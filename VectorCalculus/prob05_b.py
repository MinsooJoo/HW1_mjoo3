import numpy as np

def Dg(y_1,y_2):
    
    ### <--- START OF YOUR CODE
    Dg = np.array([[1, 2],
                   [4, -1]])    ### END OF YOUR CODE --->

    return Dg

def main():

    y_1,y_2=-1,4

    print(Dg(y_1,y_2))

if __name__ == "__main__":
    main()