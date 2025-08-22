def min_area_cover_all_ones(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    top = rows
    bottom = -1
    left = cols
    right = -1
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r < top:
                    top = r
                if r > bottom:
                    bottom = r
                if c < left:
                    left = c
                if c > right:
                    right = c
                    
    if top == rows:  # no 1 found
        return 0
    
    height = bottom - top + 1
    width = right - left + 1
    
    return height * width

# Example usage:
grid = [[0, 1, 0], [1, 0, 1]]
print(min_area_cover_all_ones(grid))  # Output: 6
