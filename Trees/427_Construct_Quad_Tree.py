from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        gridValue = grid[0][0]
        validGrid = True
        
        # check if all values in the grid are the same
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != gridValue:
                    validGrid = False
                    break
        
        # current grid has same value -> stop
        if validGrid:
            return Node(gridValue, True, None, None, None, None)
        
        # current grid does not have same value -> divide current grid into 4 equal subgrids and recurse
        newGridSize = int(len(grid) / 2)
        topLeft = [row[0:newGridSize] for row in grid[0:newGridSize]]
        topRight = [row[newGridSize:len(grid)] for row in grid[0:newGridSize]]
        bottomLeft = [row[0:newGridSize] for row in grid[newGridSize:len(grid)]]
        bottomRight = [row[newGridSize:len(grid)] for row in grid[newGridSize:len(grid)]]

        return Node(gridValue, False, self.construct(topLeft), self.construct(topRight), self.construct(bottomLeft), self.construct(bottomRight))

    '''
    Quad-Tree:
        - each internal node has exactly 4 children
        - each node has a value
            - value is 1 if node represents a grid of 1's
            - value is 0 if node represents a grid of 0's
            - internal nodes can have any value
        - a node is a leaf node if isLeaf is True

    represent nxn grid as a Quad-Tree:
        - if current grid has the same value then setIsLeaf to True
            - set children to None and stop
        - if current grid has different value then setIsLeaf to False
            - set val to 0 or 1 (doesn't matter)
            - divide current grid into 4 equal subgrids and recurse
    
    if n == 2^x then this solution is O(x * n^2)
    we can improve space complexity by creating a helper function that constructs the quad tree but takes row index, column index, and width
        - this allows us to not need to create subgrids every time we recurse
    '''
        