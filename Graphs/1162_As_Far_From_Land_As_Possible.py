from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nofland = 0

        # initialize a queue with all of the land cells in the grid
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = -1
                    nofland += 1
        
        # check if grid is not all land and not all water
        if nofland == 0 or nofland == n ** 2:
            return -1
        
        distance = -1
        while len(queue) != 0:
            distance += 1

            for i in range(len(queue)):
                node = queue.popleft()
                last_node = node

                # explore the neighbours
                for direction in directions:
                    i2, j2 = node[0] + direction[0], node[1] + direction[1]

                    # explore all valid unvisited neighbours
                    if i2 in range(n) and j2 in range(n) and grid[i2][j2] != -1:
                        queue.append((i2, j2))
                        grid[i2][j2] = -1
        
        return distance

    '''
    nxn grid -> 0 = water and 1 = land
    find a water cell such that its distance to the nearest land cell is maximized -> find water cell with longest shortest path -> multi-source + level BFS
    (1) initialize a queue with all of the land cells in the grid
        (a) if nofland == 0 or nofland == n^2 then return -1 (all land or all water)
    (2) perform level BFS until we reach the last level (which should contain only 1 node)
    (3) the node in the last level has the longest shortest path so return it
    thus total time complexity is O(n^2) and total space complexity is O(n) to maintain the queue
        - set grid[i][j] = -1 to mark it as visited
    '''