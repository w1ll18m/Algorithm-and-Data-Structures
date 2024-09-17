from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        def preorderProcess(node):
            if node is None:
                return
            preorder.append(node.val)
            preorderProcess(node.left)
            preorderProcess(node.right)
        
        preorderProcess(root)

        return preorder
    
    '''
    preorder traversal -> process current node, left subtree, then right subtree
    '''
        