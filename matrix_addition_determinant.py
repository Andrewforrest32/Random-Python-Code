import numpy as np
import numpy.linalg as la

x = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        x[i, j] = int(input("Enter value for first matrix: "))
        
print(x)
        
y = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        y[i, j] = int(input("Enter value for second matrix: "))

print(y)

xy = x+y
print(xy)

# Calculate and print determinants
det_x = la.det(x)
det_y = la.det(y)
det_xy = la.det(xy)

print("Determinant of x:", det_x)
print("Determinant of y:", det_y)
print("Determinant of xy (element-wise addition):", det_xy)
