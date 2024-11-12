from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nofrows = len(grid)
        nofcols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            # case: cell is not valid, water, or visited
            if i < 0 or i >= nofrows or j < 0 or j >= nofcols or grid[i][j] == 0 or grid[i][j] == -1:
                return 0
            
            # case: cell is land and unvisited
            perimeter = 0
            grid[i][j] = -1     # mark the current cell as visited

            # check if neighbour cells are not land
            if i == 0 or grid[i-1][j] == 0:
                perimeter += 1
            if i == nofrows - 1 or grid[i+1][j] == 0:
                perimeter += 1
            if j == 0 or grid[i][j-1] == 0:
                perimeter += 1
            if j == nofcols - 1 or grid[i][j+1] == 0:
                perimeter += 1
            
            # recurse on neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]
                perimeter += dfs(i2, j2)
            
            return perimeter
        
        # find and recurse on the first land cell
        for i in range(nofrows):
            for j in range(nofcols):
                if grid[i][j] == 1:
                    return dfs(i, j)
            
    '''
    grid[i][j] = 1 represents land and grid[i][j] = 0 represents water
    find the perimeter of the island (only 1)

    we want to explore all land cells -> DFS
    how much a perimeter that a land cell contributes is determined by:
    (1) +1 to perimeter for every neighbour cell thats water
    (2) +1 to perimeter for every edge that is on the border (ex. i = 0, i = row - 1, j = 0, j = col - 1)
    we can mark a visited cell as -1 to ensure O(1) space complexity
    
    find the size of row and col in the grid -> O(1) time
    for each cell, check at most 4 neighbours -> O(1) per cell
    we might need to check every cell thus worst case O(n * m) total time complexity
    '''