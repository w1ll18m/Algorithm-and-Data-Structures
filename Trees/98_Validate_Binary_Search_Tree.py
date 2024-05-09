from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))
    
    def isValid(self, node, min, max):
        if not node:
            return True
        return node.val > min and node.val < max and self.isValid(node.left, min, node.val) and self.isValid(node.right, node.val, max)
    
    '''
    need to check the following edge cases:
        - left child is less than parent, parent is greater than ancestor, child is less than ancestor
        - right child is greater than parent, parent is less than ancestor, child is greater than ancestor
    we can accomplish this by maintaining a range of plausible values at each node (lower, upper)
        - for right child, update the lower bound with value of current node
        - for left child, update the upper bound with value of current node
    '''