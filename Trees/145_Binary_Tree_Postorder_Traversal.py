from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []

        def postorderProcess(node):
            if node is None:
                return
            postorderProcess(node.left)
            postorderProcess(node.right)
            postorder.append(node.val)
        
        postorderProcess(root)

        return postorder
    
    '''
    postorder traversal -> process left subtree, current node, then right subtree
    '''
        