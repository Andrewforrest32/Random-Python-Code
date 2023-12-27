import numpy as np
import numpy.linalg as la

matrix = np.zeros((3, 3))

temp = int(input("Enter the initial entry: "))
increment = int(input("How much should each entry increase by: "))

for row in matrix:  # loop through rows
    for j in range(matrix.shape[1]):  # loop through columns
        row[j] = temp
        temp += increment

print(matrix)
print(la.det(matrix))

if la.matrix_rank(matrix) != matrix.shape[0] and la.det(matrix) == 0:
    print("The matrix is non-invertible")
else:
    print(la.inv(matrix))