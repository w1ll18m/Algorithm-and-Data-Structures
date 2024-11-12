from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nofrows = len(grid)
        nofcols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def findAreaOfIsland(i, j):
            # mark the cell as visited
            grid[i][j] = 0

            area = 1    # current cell contributes 1 to the area of the island
            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]

                if 0 <= i2 < nofrows and 0 <= j2 < nofcols and grid[i2][j2] == 1:
                    # explore neighbour if it is unvisted land cell
                    area += findAreaOfIsland(i2, j2)
            
            return area
        
        max_area = 0
        # find the area of the largest connected component
        for i in range(nofrows):
            for j in range(nofcols):
                if grid[i][j] == 1:
                    cur_area = findAreaOfIsland(i, j)
                    max_area = max(max_area, cur_area)
        
        return max_area
    
    '''
    find the area of the largest island (connected component) -> DFS
    need to explore all connected components -> (1) iterate through the entire grid and call DFS on unvisited land cell
                                                (2) for each DFS, the area of the island is the # of visited cells
                                                (3) keep track of the largest value of DFS (represents largest island)
    mark cells as visited by setting grid[i][j] = 0 thus O(1) space complexity
    since we visit each cell once then total time complexity is O(n)
    '''