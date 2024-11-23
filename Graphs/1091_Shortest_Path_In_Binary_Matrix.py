from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # check if top-left cell and bottom-right cells are '1'
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1 
        # check if the grid is only 1 cell
        if rows == 1 and cols == 1:
            return 1
        
        # initialize the BFS queue with the top-left cell
        queue = deque()
        queue.append((0, 0)) 
        grid[0][0] = 1
        
        path_length = 0
        while len(queue) != 0:
            # exploring a new level so increment path length
            path_length += 1

            for i in range(len(queue)):
                i, j = queue.popleft()

                # explore the neighbours
                for direction in directions:
                    i2, j2 = i + direction[0], j + direction[1]
                    
                    # if the neighbour is bottom-right cell then return the path length
                    if i2 == rows - 1 and j2 == cols - 1:
                        return path_length + 1

                    # if the neighbour is an unvisited clear cell then add it to the queue
                    if i2 in range(rows) and j2 in range(cols) and grid[i2][j2] == 0:
                        grid[i2][j2] = 1
                        queue.append((i2, j2))
        
        # there is no path from top-left to bottom-right cell so return -1
        return -1
    
    '''
    clear path -> path from top-left cell to bottom-right cell
    we can only move to cells where grid[i][j] = 0

    find the shortest path between x and y-> BFS (level by level)
    mark visited cells with grid[i][j] = 1
    thus total time complexity is O(n * m)
    '''
        