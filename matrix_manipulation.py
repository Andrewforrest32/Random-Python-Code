import numpy as np

x = np.array([[1,1,-1,7],[1,-1,2,3],[2,1,1,9]])

def swap_rows(matrix):
    row1 = int(input("Which row do you want to swap (1,2,3): "))
    row2 = int(input("Which other row (1,2,3): "))
    temp = matrix[row1-1].copy()
    matrix[row1-1] = matrix[row2-1]
    matrix[row2-1] = temp
    return matrix
    
def add_sub_rows(matrix):
    row1 = int(input("Which row do you want to add/sub to (1,2,3): "))
    row2 = int(input("Which row do you want to use(1,2,3): "))
    multiple = int(input(f"Enter the amount of row {row2} you want to add or subtract: "))
    matrix[row1-1] = matrix[row1-1]+multiple*matrix[row2-1]
    return matrix
    
def multiply_row(matrix):
    row = int(input("Which row do you want to multiply (1,2,3): "))
    multiple = int(input(f"Enter the amount you want to multiply row {row} by: "))
    matrix[row-1] = matrix[row-1]*multiple
    return matrix

def divide_row(matrix):
    row = int(input("Which row do you want to divide (1,2,3): "))
    multiple = int(input(f"Enter the amount you want to divide row {row} by: "))
    matrix[row-1] = matrix[row-1]/multiple
    return matrix

while True:
    print(x)
    choice = int(input("Do you want to swap rows(1), add/substract rows(2), multiply a row(3), divide a row(4) or done(5): "))
    if choice == 5:
        break
    elif choice == 1:
        x = swap_rows(x)
    elif choice == 2:
        x = add_sub_rows(x)
    elif choice == 3:
        x = multiply_row(x)
    elif choice == 4:
        x = divide_row(x)
    else:
        print("Invalid choice!")

print("The final matrix is:")
print(x)