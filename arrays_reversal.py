import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x_2D = x.reshape(2, 6)
x_3D = x.reshape(3, 4)
x_4D = x.reshape(4, 3)

# 1. Reverse the elements:
x_reversed = x[::-1]
x_2D_reversed = x_2D[:, ::-1]
x_3D_reversed = x_3D[:, ::-1]
x_4D_reversed = x_4D[:, ::-1]

# 2. Reverse both elements and dimensions:
x_reversed_and_transposed = x[::-1].T
x_2D_reversed_and_transposed = x_2D[::-1, ::-1]
x_3D_reversed_and_transposed = x_3D[::-1, ::-1]
x_4D_reversed_and_transposed = x_4D[::-1, ::-1]

# Print the original arrays:
print("Original arrays:")
print(x)
print(x_2D)
print(x_3D)
print(x_4D)

# Print the reversed arrays:
print("\nElements reversed:")
print(x_reversed)
print(x_2D_reversed)
print(x_3D_reversed)
print(x_4D_reversed)

# Print the reversed and transposed arrays:
print("\nElements and dimensions reversed:")
print(x_reversed_and_transposed)
print(x_2D_reversed_and_transposed)
print(x_3D_reversed_and_transposed)
print(x_4D_reversed_and_transposed)