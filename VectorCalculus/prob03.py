import numpy as np

def dinvA(x):
    
    ### <--- START OF YOUR CODE


    A = np.array([[1, x**3 + 3], [x**4 + x**2 + 3, x**2 + 1]])

    dA_dx = np.array([[0, 3 * x**2], [4 * x**3 + 2 * x, 2 * x]])
    A_inv = np.linalg.inv(A)
    dinvA = -A_inv @ dA_dx @ A_inv

    ### END OF YOUR CODE --->

    return dinvA

def main():
    x = 1

    print(dinvA(x))

if __name__ == "__main__":
    main()