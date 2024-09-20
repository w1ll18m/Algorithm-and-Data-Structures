from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is not None and root2 is not None:
            mleft = self.mergeTrees(root1.left, root2.left)
            mright = self.mergeTrees(root1.right, root2.right)
            merged = TreeNode(root1.val + root2.val, mleft, mright)
            return merged
        elif root1 is not None:
            return root1
        else:
            return root2
    
    '''
    if two nodes overlap then sum node values in the merged tree
    recursive approach:
        - if root1 and root2 then new node with val = root1.val + root2.val
        - if !root1 and !root2 then return None (both tree don't have this node)
        - if root1 and !root2 then just return root1 (similar case for if root2)
        - recursively merge left and right subtrees
    '''


        