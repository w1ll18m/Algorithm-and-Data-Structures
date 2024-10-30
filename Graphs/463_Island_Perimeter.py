from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # find the size of row and col
        row = len(grid)
        col = len(grid[0])
        # define transformations to get neighbours
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        perimeter = 0
        # maintain a queue of unexplored cells
        queue = deque()
        # maintain a set of explored cells
        seen = set()

        # find the first land cell then break (explore all cells in worst case)
        for i in range(row):
            if len(queue) > 0:
                break
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    seen.add((i, j))
                    break
        
        while len(queue) != 0:
            cell = queue.popleft()

            for neighbour in neighbours:
                ncell = (cell[0] + neighbour[0], cell[1] + neighbour[1])

                # case 1: neighbour cell has already been explored
                if ncell in seen:
                    continue

                # case 2: neighbour cell is not valid -> current cell has border edge
                if not (0 <= ncell[0] < row) or not (0 <= ncell[1] < col):
                    perimeter += 1
                    continue
                
                # case 3: neighbour cell is valid and is water
                if grid[ncell[0]][ncell[1]] == 0:
                    perimeter += 1
                # case 4: neighbour cell is valid and is land
                else:
                    queue.append(ncell)
                    seen.add(ncell)
        
        return perimeter

    '''
    grid[i][j] = 1 represents land and grid[i][j] = 0 represents water
    find the perimeter of the island (only 1)

    we want to explore all land cells -> BFS
    how much a perimeter that a land cell contributes is determined by:
    (1) +1 to perimeter for every neighbour cell thats water
    (2) +1 to perimeter for every edge that is on the border (ex. i = 0, i = row - 1, j = 0, j = col - 1)
    
    find the size of row and col in the grid -> O(1) time
    for each cell, check at most 4 neighbours -> O(1) per cell
    we might need to check every cell thus worst case O(n * m) total time complexity
    '''