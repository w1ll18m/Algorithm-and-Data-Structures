from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = deque()
        nodes.append([root, 0])
        max_width = 0

        while len(nodes) != 0:
            level_size = len(nodes)
            max_pos, min_pos = None, None

            for i in range(level_size):
                node = nodes.popleft()
                node, pos = node[0], node[1]

                # first node in each level should be one with smallest position (due to the order we add nodes to next level)
                if i == 0:
                    min_pos = pos
                # last node in each level should be one with largest position (due to the order we add nodes to next level)
                if i == level_size - 1:
                    max_pos = pos
                
                # add children and their calculated positions to next level
                if node.left: nodes.append([node.left, 2 * pos])
                if node.right: nodes.append([node.right, 2 * pos + 1])

            # compaare current max width and the current level width
            level_width = max_pos - min_pos + 1
            if level_width > max_width:
                max_width = level_width
            
        return max_width

    '''
    find the maximum width among all levels -> width is length between end nodes including null nodes

    process the nodes level by level -> bfs
    in each queue, each entry will consist of (1) the node
                                              (2) its position in the level (0-indexed)
    the queue for the first level will look like [(root, 0)]
    observe that we can calculate:
        - the position of the left child of the node -> 2 * pos
            - there are (pos - 1 + 1) = pos nodes before parent node
            - each have 2 (potential) children thus there are 2 * pos (potential) nodes before the left child
        - the position of the right child of the node -> (2 * pos) + 1
    at each level:
        - add children of current level nodes to queue (+ calculate their positions)
        - keep track of current level node with lowest and highest position
        - subtract those positions to get the width of the current level
    
    this solution visits each node exactly once thus is O(n) time complexity
    we need to store the positions of each node thus is O(n) space complexity
    '''
        