import numpy as np

def find_corner(grid, i, j):
    # Move to top-left corner

    while i < len(grid) and j < len(grid[0]) and grid[i][j] == 0:
        i += 1
        j += 1
    i -= 1
    j -= 1

    # Move along left and top edges to determine location
    while i >= 0 and grid[i][0] == 0:
        i -= 1
        print(i,j)
    while j >= 0 and grid[0][j] == 0:
        j -= 1
        print(i,j)
    return i, j  # return the agent's location

def clean_room(grid):
    n, m = len(grid), len(grid[0])
    clean_squares = set((i, j) for i in range(n) for j in range(m) if grid[i][j] == 1)  # set of dirty squares
    x, y = find_corner(grid)  # find the agent's initial location
    while clean_squares:
        if (x, y) in clean_squares:  # if the agent is on a dirty square, clean it
            clean_squares.remove((x, y))
            grid[x][y] = 0
            print(f"Cleaned square ({x}, {y})")
        if not clean_squares:  # if all squares are clean, stop
            break
        # move to the next dirty square
        dx, dy = min(clean_squares, key=lambda p: abs(p[0]-x) + abs(p[1]-y))
        if dx > x:
            x += 1
            print(f"Moved to square ({x}, {y})")
        elif dx < x:
            x -= 1
            print(f"Moved to square ({x}, {y})")
        elif dy > y:
            y += 1
            print(f"Moved to square ({x}, {y})")
        else:
            y -= 1
            print(f"Moved to square ({x}, {y})")
            
            
matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]] 
x, y = 1, 1
print(find_corner(matriz,x,y))