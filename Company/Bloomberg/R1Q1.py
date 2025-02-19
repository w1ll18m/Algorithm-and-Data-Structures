
"""
const grid = [
    ['.','.','.','o'],
    ['.','x','x','.'],
    ['.','x','x','x'],
    ['.','c','.', "50"]
    
    ride(grid, 2) => True
    
    c -> 10
    c -> 20
    
    
];

ride(grid, gas)
"""
from collections import deque

def ride(grid, gas):
    pos_o = [-1, -1]
    pos_c = [-1, -1]
    
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'o':
                pos_o = [i, j]
            if grid[i][j] == 'c':
                pos_c = [i, j]
    
    if pos_o == [-1, -1]:
        return False
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bfsq = deque()
    bfsq.append(pos_c)
    
    counter = 0
    while len(bfsq) != 0:
        for i in range(len(bsfq)):
            cell = bfsq.popleft()
            grid[cell[0]][cell[1]] = 'X'
            for direction in directions:
                i, j = cell[0] + direction[0], cell[1] + direction[1]
                if 0 <= i < rows and 0 <= j < cols:
                    if grid[i][j] == 'o':
                        return counter <= gas
                    if grid[i][j] != 'X':
                        bfsq.append([i, j])
        counter += 1
                    
    return False