from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def inorderProcess(cur):
            if cur is None:
                return
            inorderProcess(cur.left)
            inorder.append(cur.val)
            inorderProcess(cur.right)
        
        inorderProcess(root)

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

    solution #2: recursion
    if the current node is not None:
        - recurse on the left subtree
        - append val to the inorder array
        - recurse on the right subtree
    if the current node is None:
        - return and do nothing
    '''
        