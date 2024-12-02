from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            # check if cell has been visited or is water
            if i not in range(rows) or j not in range(cols) or grid[i][j] == 1:
                return
            # mark the cell as visited
            grid[i][j] = 1

            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]
                dfs(i2, j2)
        
        # call DFS on any land cell that is on the edge of the grid
        for i in range(rows):
            if grid[i][0] == 0: dfs(i, 0)
            if grid[i][cols - 1] == 0: dfs(i, cols - 1)
        for j in range(cols):
            if grid[0][j] == 0: dfs(0, j)
            if grid[rows - 1][j] == 0: dfs(rows - 1, j)
        
        # traverse the grid, call DFS on any remaining land cells, and return the # of DFS calls
        nofclosed = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i, j)
                    nofclosed += 1
        
        return nofclosed
        
    '''
    2D grid consisting of land (0) and water (1)
    find the # of closed islands -> # of connected components that don't have an edge land cell -> DFS or Union Find

    DFS Approach:
    (1) traverse the grid and call DFS on any land cell that is on the edge
    (2) during DFS, mark any visited land cells as grid[i][j] = 1 
    (3) at this point, all land cells that belong to non-closed islands should be marked as water
    (4) traverse the grid and call DFS on any remaining land cells
    (5) count the total # of times that DFS is called during the traversal which represnts the # of closed connected components
    thus total time complexity is O(n) and total space complexity is O(1)
    '''