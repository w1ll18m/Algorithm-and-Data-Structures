from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high)
    
    '''
    return the sum of all nodes with values between [low, high]

    recursive solution:
        - if node is none then return 0
        - if node value is between [low, high] then return the sum of the range sum of left/right subtrees and root.val
            - if node value is now between [low, high] then don't include root.val
    since this is a binary search tree:
        - if node.val < low then we must search right subtree (since left subtree contains values less than node.val)
        - if node.val > high then we must seartch left subtree
    '''
        