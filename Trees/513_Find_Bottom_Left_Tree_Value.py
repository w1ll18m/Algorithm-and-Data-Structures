from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = deque()
        nodes.append(root)
        first = root.val

        while len(nodes) != 0:
            for i in range(len(nodes)):
                node = nodes.popleft()
                if i == 0:
                    first = node.val
                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)
        
        return first
    
    '''
    we want to process nodes by row -> BFS
    keep track of first node in each row
    if next row is empty then return the tracked value
    we visit each node once thus O(n) time complexity
    '''