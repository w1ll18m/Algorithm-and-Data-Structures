from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()

        def dfs(i, j):
            # do nothing if the cell is invalid or already visited
            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] == -1:
                return
            # if the cell is water then add to the BFS queue
            if grid[i][j] == 0:
                queue.append((i, j))
                grid[i][j] = -1
                return
            
            # mark the cell as visited
            grid[i][j] = -1

            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]
                dfs(i2, j2)
        
        # intialize the BFS queue (using DFS to discover the first island and its neighbouring water cells)
        stop = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    stop = True
                    break    
            if stop: break

        noflevels = 1
        while len(queue) != 0:
            # process the entire level at a time
            for _ in range(len(queue)):
                i, j = queue.popleft()

                # explore the neighbours
                for direction in directions:
                    i2, j2 = i + direction[0], j + direction[1]

                    # check if cell is valid and unvisited
                    if 0 <= i2 < rows and 0 <= j2 < cols and grid[i2][j2] != -1:
                        # if cell is land then we reached the other island so return the # of steps it took
                        if grid[i2][j2] == 1:
                            return noflevels

                        # if cell is water then add it to the queue and mark it as visited
                        grid[i2][j2] = -1
                        queue.append((i2, j2))

            # next level has no land cells so we must explore another level
            noflevels += 1

    '''
    there are exactly 2 islands (connected components) in the grid
    we want to find the smallest # of 0s to flip -> find the shortest distance from island 1 to island 2 -> multi-source + multi-level BFS
    (1) use DFS to discover the first island and add any neighbouring water cells to the queue
        - this is the first level of BFS
        - mark the cell as visited by marking grid[i][j] = -1
    (2) perform multi-level BFS while keeping track of the # of levels until we reach a level with a land cell
    thus total time complexity is O(n * m) to execute DFS once and BFS once
    '''
        