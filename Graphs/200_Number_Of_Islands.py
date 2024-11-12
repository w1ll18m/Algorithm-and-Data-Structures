from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nofrows = len(grid)
        nofcols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            # mark the current cell as visited
            grid[i][j] = "-1"

            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]

                # don't explore cells not in the grid
                if i2 < 0 or i2 >= nofrows or j2 < 0 or j2 >= nofcols:
                    continue
                # explore neighbour if it is an unvisted land cell
                if grid[i2][j2] == "1":
                    dfs(i2, j2)
        
        nofislands = 0
        # count the # of times that DFS is called on an unvisted land cell
        for i in range(nofrows):
            for j in range(nofcols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    nofislands += 1
        
        return nofislands
    
    '''
    find the # of islands (connected components) -> DFS since we need to explore all cells
    if we call DFS on an unvisited land cell in an island, all cells in that island will be explored
    thus (1) iterate through the entire grid and call dfs on each unvisited land cell
         (2) count and return the # of times DFS is called
    mark cells as visited by setting grid[i][j] = -1 -> O(1) space complexity
    since we visit each cell once then total time complexity is O(n)
    '''