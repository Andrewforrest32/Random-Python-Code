import random as R

def reshape_list(rows, columns, list_original):
    """Reshapes a nested list into a new shape with specified rows and columns."""
    print(list_original)
    
    reshaped_list = []
    rows_original = len(list_original)
    
    print(rows_original)
    
    not_1D = False
    for element in list_original:
        if isinstance(element, list):
            not_1D = True

    if rows_original > 1 and not_1D:
        list_1D = []
        columns_original = len(list_original[0])
        for i in range(rows_original):
            for j in range(columns_original):
                list_1D.append(list_original[i][j])
    else:
        list_1D = list_original.copy()
    
    print(list_1D)
    
    if rows == 1:
        return list_1D

    for i in range(rows):
        row = []  # Create an empty row for each iteration
        for j in range(columns):
            temp = list_1D.pop(0)
            row.append(temp)
        reshaped_list.append(row)  # Append the completed row to the reshaped list
    return reshaped_list

even_odd = [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]
shuffled = even_odd.copy()  # Avoid modifying the original list

# Reshape correctly, preserving the nested structure
shuffled = reshape_list(1, 10, shuffled)  # Reshape to a single row with 10 elements
R.shuffle(shuffled)  # Shuffle only the first sublist (nested list)
shuffled = reshape_list(2, 5, shuffled)  # Reshape back to 2 rows and 5 columns

print(shuffled)