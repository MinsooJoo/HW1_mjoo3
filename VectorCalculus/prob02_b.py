import numpy as np

def Du(x_1,x_2):
    
    ### <--- START OF YOUR CODE
    Du = np.array([[x_2, x_1],[2 * x_1, -2 * x_2]])
    ### END OF YOUR CODE --->

    return Du

def main():
    x_1 = 1
    x_2 = -1
    print(Du(x_1,x_2))

if __name__ == "__main__":
    main()