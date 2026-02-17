import numpy as np

def dA2dt(t):
    
    ### <--- START OF YOUR CODE
    A = np.array([[t**2, t + 1], 
                  [t**3 + t + 3, 7]])
    dA_dt = np.array([[2 * t, 1], 
                      [3 * t**2 + 1, 0]])
    dA2dt = dA_dt @ A + A @ dA_dt
    ### END OF YOUR CODE --->

    return dA2dt

def main():
    t = 1

    print(dA2dt(t))

if __name__ == "__main__":
    main()