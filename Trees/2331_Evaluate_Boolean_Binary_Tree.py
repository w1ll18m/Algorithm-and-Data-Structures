from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.val

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
    
    '''
    leaf nodes have value 0 or 1
        - 0 is False and 1 is True
    non-leaf nodes have value 2 or 3
        - 2 is OR and 3 is AND
    every node has either 0 or 2 children

    recursive solution:
        - if leaf node then return True or False depending on the value
        - if non-leaf node then return dfs(left_tree) AND/OR dfs(right_tree)
    '''