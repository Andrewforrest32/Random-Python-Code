import numpy as np
import numpy.linalg as la

identity = np.eye(3)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x_inv = la.inv(x)

test = x @ x_inv

if np.allclose(test, identity):
    print(f"Matrix {x} times its inverse {x_inv} is approximately equal to the identity matrix.")
else:
    print("The product of the matrix and its inverse is not equal to the identity matrix.")
