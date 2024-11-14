from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        current = deque()
        # add all treasure cells to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    current.append((i, j))
        
        distance = 1
        while len(current) != 0:
            # explore all cells in the current level
            for _ in range(len(current)):
                i, j = current.popleft()

                # explore the neighbours
                for direction in directions:
                    i2, j2 = i + direction[0], j + direction[1]

                    # if the neighbour is valid and unvisited land cell then change it to current distance
                    if 0 <= i2 < rows and 0 <= j2 < cols and grid[i2][j2] == 2147483647:
                        grid[i2][j2] = distance
                        current.append((i2, j2))
            
            distance += 1

        # return grid

    '''
    mxn graph -> water (-1), treasure chest (0), and land (INF)

    want to find shortest distance from all cells to any treasure cell -> BFS
    need to process nodes based on their distance from the source (treasure cells) -> BFS (levels)
    (1) initialize a queue and add treasure cells 
    (2) as long as queue is not empty then explore all neighbours
        - keep track of the current level (aka current distance from source cells)
        - if neighbour is a land cell then add it to the queue and change it to current distance
        - if neighbour is a treasure chest or water then do nothing
    since we visit each cell at most once then total time complexity is O(nxm)
    we are tracking distance on top of the provided grid thus total space complexity is O(nxm) for the queue
    '''