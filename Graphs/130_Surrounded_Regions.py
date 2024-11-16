from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        # add all left/right edge 'O' cells to the queue
        for i in range(rows):
            for j in [0, cols - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))
                    board[i][j] = 'OO'
        # add all top/bottom edge 'O' cells to the queue
        for j in range(1, cols - 1):
            for i in [0, rows - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))
                    board[i][j] = 'OO'
        
        # call BFS to explore all cells that can reach an edge 'O' cell
        while len(queue) != 0:
            i, j = queue.popleft()

            # explore the neighbours
            for direction in directions:
                i2, j2 = i + direction[0], j + direction[1]

                # if the neighbour is valid and unvisted then add it to the queue
                if 0 <= i2 < rows and 0 <= j2 < cols and board[i2][j2] == 'O':
                    queue.append((i2, j2))
                    board[i2][j2] = 'OO'
        
        # iterate through the entire grid and capture all surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'OO':
                    board[i][j] = 'O'

    '''
    surround -> none of the region's cells are on the edge of the board

    replace all cells in a region (component) that is surrounded with 'X' -> BFS/DFS?
    find all 'O' cells with a path to an edge 'O' cell -> multi-source BFS

    (1) initialize a queue and add all edge 'O' cells
    (2) call BFS to explore all neighbours that are reachable from source nodes
        - mark it as visited by setting grid[i][j] = 'OO' (need to indicate it won't be captured)
    (3) iterate through the entire grid and do the following:
        - if cell is 'OO' then change it to 'O'
        - if cell is 'O' then change it to 'X'
    we visit each node at most twice (once from BFS and once during final iteration) thus total time complexity is O(nxm)
    we use a queue to keep track of nodes to visit next thus total space complexity is O(nxm)
        - DFS has O(1) space complexity but recursion stack is O(nxm)
    '''