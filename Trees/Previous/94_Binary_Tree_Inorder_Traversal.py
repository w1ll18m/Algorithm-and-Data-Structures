from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        inorder = []
        cur = root
        
        while cur or len(stack) != 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                inorder.append(cur.val)
                cur = cur.right
        
        return inorder
        
        '''
        solution #1: stack
        in order traversal -> process left branch, current node, right branch
        when we encounter a node:
            - if the node is not none then
                - push the node onto the stack
                - traverse to the left child of the tree
            - if the node is none then we are done processing the left subtree 
                - pop from the stack, process the current node, and traverse to right child
        we use a stack because we want to process the nodes in FIFO order
        '''
        