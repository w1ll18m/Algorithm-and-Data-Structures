from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pacific = set()
        atlantic = set()
        queue = deque()

        # add all the cells in the left edge to the queue
        for i in range(rows):
            queue.append((i, 0))
            pacific.add((i, 0))
        # add all the cells in the top edge to the queue
        for j in range(1, cols):
            queue.append((0, j))
            pacific.add((0, j))
        
        # call BFS to explore all cells that can reach the pacific ocean
        while len(queue) != 0:
            i, j = queue.popleft()
            
            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]

                # if the neighbour is valid and unvisited then add it to the queue
                if 0 <= i2 < rows and 0 <= j2 < cols and ((i2, j2) not in pacific) and heights[i2][j2] >= heights[i][j]:
                    queue.append((i2, j2))
                    pacific.add((i2, j2))
        
        # maintain a list of cells that can reach both oceans
        both = []
        
        # add all the cells in the right edge to the queue
        for i in range(rows):
            queue.append((i, cols - 1))
            atlantic.add((i, cols - 1))
            # check if cell can reach the pacific ocean
            if (i, cols - 1) in pacific:
                both.append([i, cols - 1])
        # add all the cells in the bottom edge to the queue
        for j in range(cols - 1):
            queue.append((rows - 1, j))
            atlantic.add((rows - 1, j))
            # check if cell can reach the pacific ocean
            if (rows - 1, j) in pacific:
                both.append([rows - 1, j])
        
        # call BFS to explore all cells that can reach the atlantic ocean
        while len(queue) != 0:
            i, j = queue.popleft()
            
            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]

                # if the neighbour is valid and unvisited then add it to the queue
                if 0 <= i2 < rows and 0 <= j2 < cols and ((i2, j2) not in atlantic) and heights[i2][j2] >= heights[i][j]:
                    queue.append((i2, j2))
                    atlantic.add((i2, j2))

                    # check if cell can reach the pacific ocean
                    if (i2, j2) in pacific: 
                        both.append([i2, j2])

        return both

    '''
    pacific ocean -> borders islands left (heights[0][0] - heights[n-1][0]) and top edges (heights[0][0] - heights[0][m-1])
    atlantic ocean -> borders islands right (heights[0][m-1] - heights[n-1][m-1]) and bottom edges (heights[n-1][0] - heights[n-1][m-1])

    for each node, we want to find a path to edge node -> DFS/BFS?
    equivalently, find all nodes that are reachable from edge nodes -> multi-source BFS
        - nodes that are reachable from top-left edge nodes can flow into pacific
        - nodes that are reachable from bottom-right edge nodes can flow into atlantic

    maintain sets representing cells that can flow to pacific and cells that can flow to atlantic
    (1) initialize a queue and add all top-left edge nodes
        - add them to set of cells that can flow to pacific
    (2) call BFS to explore all neighbours that are reachable from source nodes
        - explore neighbour if its height is greater or equal (neighbour flows into current)
    (3) repeat with bottom-right edge nodes to determine all cells that can flow to atlantic
    (4) return list of cells that exist in both sets

    we visit each node at most twice thus total time complexity is O(nxm)
    we store each node at most twice thus total space complexity is O(nxm)
    '''
        