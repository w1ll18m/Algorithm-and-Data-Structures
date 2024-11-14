from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        noforanges = 0
        nofrotten = 0
        rotten = deque()
        for i in range(rows):
            for j in range(cols):
                # count the total # of oranges
                if grid[i][j] != 0:
                    noforanges += 1
                    # count the # of inital rotten oranges and add to bfs queue
                    if grid[i][j] == 2:
                        nofrotten += 1
                        rotten.append((i, j))
        
        nofmin = 0
        while len(rotten) != 0:
            # explore all the rotten oranges in the current level
            for i in range(len(rotten)):
                cell = rotten.popleft()

                # explore the neighbours
                for direction in directions:
                    ni, nj = cell[0] + direction[0], cell[1] + direction[1]
                    # if the neighbour is valid and fresh then mark it as rotten
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        nofrotten += 1
                        grid[ni][nj] = 2
                        rotten.append((ni, nj))
            
            # if the queue is not empty then we need an additional iteration thus increment # of min
            if len(rotten) != 0: nofmin += 1
        
        # if there is a fresh orange that can not be reached return impossible
        if nofrotten != noforanges:
            return -1
        
        return nofmin

    '''
    mxn grid -> 0 (empty), 1 (fresh), 2 (rotten)
    every minute, neighbours of rotten oranges become rotten too
    return the minimum # of min that must elapse until no cell has a fresh orange
    
    how to know if no cell has fresh orange in O(1) time -> maintain a count of all rotten oranges!!!
        - keep track of the total # of oranges in the grid -> O(mxn) time
        - if: # of rotten == total # of oranges 
          then: no cell in the grid has a fresh orange

    we want to explore rotten oranges of the same level at a time -> BFS (levels)
    observe that min # of minutes = # of iterations of BFS until no cell has fresh orange
    (1) initialize a queue and add initial rotten oranges 
    (2) as long as queue is not empty then explore all neighbours 
        - if neighbour is fresh then add it to the queue and change it to rotten
        - if neighbour is rotten or empty then do nothing
    (3) count the # of iterations until BFS terminates
    (4) if # of rotten != total # of oranges then return impossible
    we visit each cell at most once thus O(nxm) total time complexity
    '''