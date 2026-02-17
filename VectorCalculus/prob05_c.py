import numpy as np

def Dh(x_1,x_2,x_3):
    
    ### <--- START OF YOUR CODE
    
    exp_x1 = np.exp(x_1)
    cos_x2 = np.cos(x_2)
    sin_x2 = np.sin(x_2)

    Dh = np.array([
        [exp_x1 * cos_x2, -exp_x1 * sin_x2, 1],
        [exp_x1 * sin_x2,  exp_x1 * cos_x2, 1]
    ])
    
    ### END OF YOUR CODE --->    ### END OF YOUR CODE --->

    return Dh

def main():

    x_1,x_2,x_3=0,1,1

    print(Dh(x_1,x_2,x_3))

if __name__ == "__main__":
    main()