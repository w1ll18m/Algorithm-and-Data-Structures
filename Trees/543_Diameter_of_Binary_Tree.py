from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longestPath = 0

        def depth(node):
            if node is None:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            path = left_depth + right_depth
            if path > self.longestPath:
                self.longestPath = path
            
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        
        return self.longestPath
    
    '''
    diameter of a binary tree is the length of the longest path between any two nodes in a tree
    define a function that recursively calculates the depth of each subtree
        - longest path involving a node is the the sum of the depth of its left tree and its right tree
        - maintain a (global) variable that keep track of the longest path of the entire tree
    '''
        