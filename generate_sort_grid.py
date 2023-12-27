import random as r

def generate_grid(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    entries_filled = 0
    numbers = list(range(1, size*size + 1))
    
    while True:
        temp_row = r.randint(0, size - 1)
        temp_col = r.randint(0, size - 1)
        temp_index = r.randint(0, len(numbers) - 1)
        
        if grid[temp_row][temp_col] == 0:
            temp_number = numbers.pop(temp_index)
            grid[temp_row][temp_col] = temp_number
            entries_filled += 1
        
        if entries_filled == size * size:
            break
    
    return grid

def sort_grid(grid):
    # Flatten the grid into a 1D list
    flat_grid = [num for row in grid for num in row]
    
    # Sort the list
    flat_grid.sort()
    
    # Reshape the sorted list back into a 2D grid
    size = len(grid)
    sorted_grid = [flat_grid[i:i+size] for i in range(0, len(flat_grid), size)]

    return sorted_grid

# Get the size of the grid from the user
size = int(input("Enter the size of the grid: "))

grid = generate_grid(size)
print(f"Original {size}x{size} Grid:")
for row in grid:
    print(row)

sorted_grid = sort_grid(grid)
print("\nSorted Grid:")
for row in sorted_grid:
    print(row)
