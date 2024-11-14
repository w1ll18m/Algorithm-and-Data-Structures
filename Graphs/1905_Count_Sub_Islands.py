from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # if all cells in component are in grid 1 then return True
        def dfs(i, j):
            # mark the cell as visited
            grid2[i][j] = 0

            isSubIsland = (grid1[i][j] == 1)    # check if cell is a land cell in grid 1
            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]
                
                # explore neighbour if it is unvisited land cell
                if 0 <= i2 < rows and 0 <= j2 < cols and grid2[i2][j2] == 1:
                    isNeighbourSubIsland = dfs(i2, j2)
                    isSubIsland = isSubIsland and isNeighbourSubIsland
            
            return isSubIsland
        
        nofsub = 0
        # count the # of connected components in grid 2 that are sub-islands
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        nofsub += 1

        return nofsub
    
    '''
    island is a group of land cells that are connected 4-directionally
    an island in grid 2 is a sub-island if there is an island in grid 1 that contains all the cells of the island in grid2

    how to check if island is a sub-island -> just check if cells are land in grid 1
        - we can do this check during DFS for one pass
    find all connected components in grid -> DFS
        (i) DFS should return True if all cells in component exist in grid 1
        (ii) count the # of connected components where all cells exist in grid 1
    '''