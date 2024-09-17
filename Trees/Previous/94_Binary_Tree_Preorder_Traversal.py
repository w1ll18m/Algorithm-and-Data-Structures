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
        stack = []
        cur = root
        
        while cur or len(stack) != 0:
            if cur is not None:
                preorder.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        
        return preorder
    
    '''
    preorder traversal -> process current node, left subtree, then right subtree

    maintain a stack
    if node is not None:
        - append the node value to the preorder array
        - add the node to the stack
        - traverse to the left subtree
    if node is None:
        - pop a node from the stack
        - traverse to the right subtree
    '''
        