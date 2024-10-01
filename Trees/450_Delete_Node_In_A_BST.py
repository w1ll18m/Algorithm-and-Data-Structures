from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(10 ** 6, root, None)   # value is 10^6 so value of root is always less than dummy (since root is left child)
        parent = dummy
        current = root
        
        # traverse the tree (iteratively) until we find the node
        while current is not None:
            if current.val == key:
                break

            parent = current
            if current.val > key:
                current = current.left
            else:
                current = current.right
        
        # if node with key is not found then return the tree 
        if current is None:
            return root

        # if node is found and has no children -> remove node
        if current.left is None and current.right is None:
            if key < parent.val:
                parent.left = None
            else:
                parent.right = None

        # if node is found and it has 2 children
        elif current.left is not None and current.right is not None:
            left = current.left
            right = current.right

            # replace the node with the right child
            if key < parent.val:
                parent.left = right
            else:
                parent.right = right

            # traverse through the left branch of the right node until we reach a node without a left child
            while right.left is not None:
                right = right.left
            
            # let the left child of the key node be the left child of the found node
            right.left = left
        
        # node is found but only has left child -> replace node with its left child
        elif current.left is not None:
            if key < parent.val:
                parent.left = current.left
            else:
                parent.right = current.left
        
        # node is found but only has right child -> replace node with its right child
        else:
            if key < parent.val:
                parent.left = current.right
            else:
                parent.right = current.right

        return dummy.left
            
    '''
    keep track of the parent node and current node
    we need to consider the following cases:
    1. node is not found then do nothing
    2. node is found and has no children then remove node
    3. node is found and has 1 child then remove the node from parent and replace with that child
    4. node is found and it has 2 children then 
        - remove the node then replace with the right child
        - traverse through the left branch of the right child until we reach a node without a left child
        - let the left child of the node be the left child of the found node
    '''
        