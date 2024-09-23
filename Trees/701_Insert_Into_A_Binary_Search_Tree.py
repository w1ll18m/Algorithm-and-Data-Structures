from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val, None, None)
        
        cur = root
        while True:
            # case where new value should be in left subtree
            if cur.val > val:
                if cur.left is None:
                    cur.left = TreeNode(val, None, None)
                    break
                else:
                    cur = cur.left
            # case where new value should be in right subtree
            else:
                if cur.right is None:
                    cur.right = TreeNode(val, None, None)
                    break
                else:
                    cur = cur.right
        
        return root
    
    '''
    return the root node of the BST after the insertion
    simplest solution: traverse the BST while comparing node values with val
        - traverse iteratively instead of recursively to save memory (no recursive call stack) 
    '''
        