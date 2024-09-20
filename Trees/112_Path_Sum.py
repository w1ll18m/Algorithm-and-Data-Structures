from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, targetSum):
            if node is None:
                return False
            # case when node is a leaf
            if node.left is None and node.right is None:
                return targetSum == node.val
            # case when node is not a leaf
            return dfs(node.left, targetSum - node.val) or dfs(node.right, targetSum - node.val)

        return dfs(root, targetSum)
    
    '''
    return true if the tree has a root-to-leaf path with sum equal to targetSum
    recursive solution:
        - if node is not a leaf then the tree has a valid path if one of its subtrees has root-to-leaf path with sum equal to targetSum - node.val
        - if node is leaf then the tree has a valid path if targetSum == node.val
    '''
    

        